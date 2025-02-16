import psutil
import time
from email_utils import get_email_credentials, send_email
from process_utils import is_system_process, restart_application

def monitor_cpu(sender_email, receiver_email, plain_password):
    """Monitor CPU usage and take actions if necessary."""
    try:
        print("CPU Usage Monitoring Started")

        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")

            if cpu_usage > 60:
                top_process = max(psutil.process_iter(["pid", "name", "cpu_percent"]),
                                  key=lambda p: p.info["cpu_percent"])

                pid, name, cpu = top_process.info["pid"], top_process.info["name"], top_process.info["cpu_percent"]

                if pid == 0:
                    continue  

                print(f"High CPU Usage Detected {name} (PID: {pid}) - {cpu}% CPU")
                send_email(sender_email, receiver_email, plain_password, 
                           f"High CPU Usage Alert: {name}", 
                           f"The process {name} (PID: {pid}) is using {cpu}% CPU.")

                if is_system_process(pid):
                    print(f"System process {name} detected. Sending email alert.")
                    send_email(sender_email, receiver_email, plain_password, 
                               f"System Process Alert: {name}", 
                               f"A system process {name} (PID: {pid}) is using {cpu}% CPU.")
                else:
                    print(f"Killing and Restarting Application Process {name} (PID: {pid})")
                    restart_application(pid, name)

            time.sleep(2)

    except KeyboardInterrupt:
        print("Monitoring Stopped")

if __name__ == "__main__":
    sender_email, receiver_email, plain_password, hashed_password = get_email_credentials()
    monitor_cpu(sender_email, receiver_email, plain_password)

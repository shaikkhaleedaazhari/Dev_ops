import psutil
import os
import time
import smtplib
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Configuration
SENDER_EMAIL = "shaikkhaleeda1523@gmail.com"  # Replace with your email
RECEIVER_EMAIL = "shaikxyx@gmail.com"  # Replace with recipient's email
EMAIL_PASSWORD = "your-app-password"  # Replace with your app password

# Define the CPU-Z path (Modify this based on your system)
CPUZ_PATH = "C:\\Program Files\\CPUID\\CPU-Z\\cpuz.exe"

def send_email(subject, body):
    """Send an email notification."""
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print(f"Email sent to {RECEIVER_EMAIL}")
    except Exception as e:
        print(f"Error sending email: {e}")

def is_system_process(pid):
    """Check if a process is a system process."""
    try:
        process = psutil.Process(pid)
        parent_name = psutil.Process(process.ppid()).name()

        # List of known system processes
        system_processes = ["system", "init", "kernel", "wininit.exe", 
                            "winlogon.exe", "services.exe", "csrss.exe", 
                            "smss.exe", "lsass.exe"]

        if process.name().lower() in system_processes or parent_name.lower() in system_processes:
            return True
        return False
    except psutil.NoSuchProcess:
        return False

def restart_application(pid, name):
    """Kill and restart an application process."""
    try:
        process = psutil.Process(pid)
        process.terminate()
        process.wait(timeout=3)
        print(f"Process {name} (PID: {pid}) killed.")

        if name.lower() == "cpuz.exe":  # If the application is CPU-Z, restart it using the known path
            print(f"Restarting {name} from {CPUZ_PATH}...")
            subprocess.Popen([CPUZ_PATH])  # Restart CPU-Z
            print(f"Process {name} restarted.")
        else:
            process_path = get_process_path(name)
            if process_path:
                print(f"Restarting {name} from {process_path}...")
                subprocess.Popen([process_path])
                print(f"Process {name} restarted.")
            else:
                print(f"Could not find executable path for {name}.")
    except psutil.NoSuchProcess:
        print(f"Process {name} not found.")
    except Exception as e:
        print(f"Error: {e}")

def get_process_path(name):
    """Get the executable path of a process."""
    for proc in psutil.process_iter(["pid", "name", "exe"]):
        if proc.info["name"].lower() == name.lower():
            return proc.info["exe"]
    return None

def monitor_cpu():
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
                send_email(f"High CPU Usage Alert: {name}", 
                           f"The process {name} (PID: {pid}) is using {cpu}% CPU.")

                if is_system_process(pid):
                    print(f"System process {name} detected. Sending email alert.")
                    send_email(f"System Process Alert: {name}", 
                               f"A system process {name} (PID: {pid}) is using {cpu}% CPU.")
                else:
                    print(f"Killing and Restarting Application Process {name} (PID: {pid})")
                    restart_application(pid, name)

            time.sleep(2)

    except KeyboardInterrupt:
        print("Monitoring Stopped")
        print("Stopped by User")

if __name__ == "__main__":
    monitor_cpu()

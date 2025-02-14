import psutil
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CPU Threshold
CPU_THRESHOLD = 60

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change if using a different email provider
SMTP_PORT = 587
EMAIL_SENDER = "shaikkhaleeda1@gmail.com"
EMAIL_PASSWORD = "12345678"  # Use App Password if using Gmail
EMAIL_RECEIVER = "khaleedask15@gmail.com"

# Function to send email
def send_email(process_name, pid, cpu_usage):
    subject = "High CPU Usage Alert - System Process"
    body = f"""
    High CPU Usage Alert!

    Process: {process_name}
    PID: {pid}
    CPU Usage: {cpu_usage}%

    This is a system process, so manual intervention may be needed.
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print(f"Email sent successfully for process {process_name} (PID: {pid})")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to restart an application process
def restart_process(process_name):
    print(f"Restarting process: {process_name}")
    os.system(f"{process_name} &")  # Restart process (modify as needed)

# Function to check and handle high CPU usage processes
def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=3)  # Check CPU usage over 3 seconds
        if cpu_usage > CPU_THRESHOLD:
            print(f"High CPU usage detected: {cpu_usage}%")

            # Find the process consuming the most CPU
            high_cpu_processes = sorted(psutil.process_iter(attrs=["pid", "name", "cpu_percent"]), key=lambda p: p.info["cpu_percent"], reverse=True)

            for process in high_cpu_processes:
                try:
                    pid = process.info["pid"]
                    process_name = process.info["name"]
                    process_obj = psutil.Process(pid)

                    # Check if the process is a system process
                    if process_obj.username() == "SYSTEM" or process_obj.username() == "root":
                        print(f"System process detected: {process_name} (PID: {pid}). Sending email alert.")
                        send_email(process_name, pid, cpu_usage)

                    # Check if the process is an application process
                    elif process_name.lower() in ["your_app_name", "chrome", "firefox"]:  # Modify with your application processes
                        print(f"Application process detected: {process_name} (PID: {pid}). Restarting.")
                        process_obj.terminate()  # Kill the process
                        restart_process(process_name)

                    # Other processes - Kill them
                    else:
                        print(f"Killing process: {process_name} (PID: {pid})")
                        process_obj.terminate()

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor_cpu_usage()

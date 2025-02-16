import psutil
import subprocess

cpu_z_path = "C:\\Program Files\\CPUID\\CPU-Z\\cpuz.exe"

def is_system_process(pid):
    """Check if a process is a system process."""
    try:
        process = psutil.Process(pid)
        parent_name = psutil.Process(process.ppid()).name()

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
        print(f"Process {name} (PID: {pid}) killed")

        if name.lower() == "cpuz.exe":
            print(f"Restarting {name} from {cpu_z_path}")
            subprocess.Popen([cpu_z_path])
            print(f"Process {name} restarted")
        else:
            process_path = get_process_path(name)
            if process_path:
                print(f"Restarting {name} from {process_path}")
                subprocess.Popen([process_path])
                print(f"Process {name} restarted")
            else:
                print(f"Could not find executable path for {name}")
    except psutil.NoSuchProcess:
        print(f"Process {name} not found")
    except Exception as e:
        print(f"Error: {e}")

def get_process_path(name):
    """Get the executable path of a process."""
    for proc in psutil.process_iter(["pid", "name", "exe"]):
        if proc.info["name"].lower() == name.lower():
            return proc.info["exe"]
    return None

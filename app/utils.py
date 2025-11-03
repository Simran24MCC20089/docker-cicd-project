import platform
from datetime import datetime

def get_greeting(name: str) -> str:
    if not name:
        name = "Guest"
    return f"👋 Hello, {name}! Welcome to the Docker CI/CD Pipeline App!"

def get_system_info() -> str:
    info = {
        "OS": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Python": platform.python_version(),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return "\n".join([f"{key}: {value}" for key, value in info.items()])

import subprocess
import json
from pathlib import Path


def processes():

    parent_folder = Path(__file__).resolve().parent.parent

    file_folder = parent_folder / "services.json"

    with open (file_folder) as file:
        f = json.load(file)
        services = {}
        for value in f.values():
            for service in value:
            
                services[service] = subprocess.run(["systemctl", "is-active", service], capture_output=True).stdout.decode('utf-8').rstrip()

        return services


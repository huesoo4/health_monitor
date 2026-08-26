import subprocess
import json

def processes():
    with open ("/home/hueso/Documentos/health_monitor/services.json") as file:
        f = json.load(file)
        services = {}
        for value in f.values():
            for service in value:
            
                services[service] = subprocess.run(["systemctl", "is-active", service], capture_output=True).stdout.decode('utf-8')

        return services


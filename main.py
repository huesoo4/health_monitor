from monitor.hostname import get_hostname
from monitor.cpu import get_cpu
from monitor.ram import usage_ram, available_ram
from monitor.disk import usage_disk, available_disk
from monitor.services import processes
from monitor.status import check_status

total_cpu, available_cpu = usage_ram()
total_disk, free_disk = usage_disk()
print(f"""
================================
       SYSTEM HEALTH
================================

Hostname: {get_hostname()}

CPU
Usage: {get_cpu()} %
Status: {check_status(get_cpu())}

MEMORY
Usage: {total_cpu} %
Available: {available_ram(available_cpu)} GB
Status: {check_status(total_cpu)}

DISK /
Usage: {total_disk} %
Available: {available_disk(free_disk)} GB
Status: {check_status(total_disk)}

SERVICES
""")

output = processes()


for key, value in output.items():
    print(f"{key}\t{value}")
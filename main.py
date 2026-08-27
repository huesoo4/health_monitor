from monitor.hostname import get_hostname
from monitor.cpu import get_cpu
from monitor.ram import usage_ram, available_ram
from monitor.disk import usage_disk, available_disk
from monitor.services import processes
from monitor.status import check_status

usage_cpu = get_cpu()
total_ram, free_ram = usage_ram()
total_disk, free_disk = usage_disk()
print(f"""
================================
       SYSTEM HEALTH
================================

Hostname: {get_hostname()}

CPU
Usage: {usage_cpu} %
Status: {check_status(usage_cpu)}

MEMORY
Usage: {total_ram} %
Available: {available_ram(free_ram)} GB
Status: {check_status(total_ram)}

DISK /
Usage: {total_disk} %
Available: {available_disk(free_disk)} GB
Status: {check_status(total_disk)}

SERVICES
""")

output = processes()


for key, value in output.items():
    print(f"{key}\t{value}")
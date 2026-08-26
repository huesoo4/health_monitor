from monitor.hostname import get_hostname
from monitor.cpu import *
from monitor.ram import *
from monitor.disk import *

print(f"""
================================
       SYSTEM HEALTH
================================

Hostname: {get_hostname()}

CPU
Usage: {get_cpu()} %
Satus: {check_status(get_cpu())}

MEMORY
Usage: {usage_ram()} %
Available: {available_ram()} GB
Status: {check_status(usage_ram())}

DISK /
Usage: {usage_disk()} %
Available: {available_disk()} GB
Status: {check_status(usage_disk())}
""")
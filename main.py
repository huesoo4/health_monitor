from monitor.hostname import get_hostname
from monitor.cpu import *

print(f"""
================================
       SYSTEM HEALTH
================================

Hostname: {get_hostname()}

CPU
Usage: {get_cpu()} %
Satus: {check_status(get_cpu())}
""")
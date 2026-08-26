import psutil

def get_cpu():
    cpu = psutil.cpu_percent(interval=1)

    return cpu

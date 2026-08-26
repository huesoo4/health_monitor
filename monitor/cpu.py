import psutil

def get_cpu():
    cpu = psutil.cpu_percent(interval=1)

    return cpu


def check_status(cpu):
    if cpu < 0:
        return "ERROR"
    elif cpu >= 0 and cpu <= 70:
        return "OK"
    elif cpu > 70 and cpu < 85:
        return "WARNING"
    elif cpu >= 85 and cpu <= 100:
        return "DANGER"
    else:
        return "ERROR"
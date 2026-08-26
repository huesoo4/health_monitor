import psutil

def usage_ram():
    total = psutil.virtual_memory()

    return (round((total.total - total.available) / total.total * 100, 2))


def available_ram():
    total = psutil.virtual_memory()
    return (round(total.available / 1024 / 1024 / 1024, 2))

def check_status(ram):
    if ram < 0:
        return "ERROR"
    elif ram >= 0 and ram <= 70:
        return "OK"
    elif ram > 70 and ram < 85:
        return "WARNING"
    elif ram >= 85 and ram <= 100:
        return "DANGER"
    else:
        return "ERROR"


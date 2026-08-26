import psutil

def usage_ram():
    total = psutil.virtual_memory()

    return (round((total.total - total.available) / total.total * 100, 2))


def available_ram():
    total = psutil.virtual_memory()
    return (round(total.available / 1024 / 1024 / 1024, 2))


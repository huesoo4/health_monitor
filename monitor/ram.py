import psutil

def usage_ram():
    total = psutil.virtual_memory()

    return (round((total.total - total.available) / total.total * 100, 2), total.available)


def available_ram(data):
    return (round(data / 1024 / 1024 / 1024, 2))


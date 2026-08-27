import psutil

def usage_disk():
    disk = psutil.disk_usage('/')

    return (round((disk.total - disk.free) / disk.total * 100, 2), disk.free)

def available_disk(data):
    return (round(data / 1024 / 1024 / 1024, 2))



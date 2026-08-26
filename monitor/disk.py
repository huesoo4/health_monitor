import psutil

def usage_disk():
    disk = psutil.disk_usage('/')

    return (round((disk.total - disk.free) / disk.total * 100, 2))

def available_disk():
    disk = psutil.disk_usage('/')
    return (round(disk.free / 1024 / 1024 / 1024, 2))



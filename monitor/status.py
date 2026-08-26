def check_status(data):
    if data < 0:
        return "ERROR"
    elif data >= 0 and data <= 70:
        return "OK"
    elif data > 70 and data < 85:
        return "WARNING"
    elif data >= 85 and data <= 100:
        return "DANGER"
    else:
        return "ERROR"
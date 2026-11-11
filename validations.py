

def check_name(name):
    if len(name) < 1:
        return False
    return True

def is_int(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False

def check_rounds(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1 or number > 10:
        return False
    return True

def choose_checker(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1 or number > 4:
        return False
    return True

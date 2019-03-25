def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


def login(username, password):
    if username == 'vip001' and password == '123456':
        return 'vip'
    else:
        return False
def buy(token):
    if token == 'vip':
        return True
    else:
        return False
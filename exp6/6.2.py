def zero(x='0'):
    if x != '0':
        match x[0]:
            case '+':
                return 0 + int(x[1])
            case '-':
                return 0 - int(x[1])
            case '*':
                return 0 * int(x[1])
            case '/':
                return int(0 / int(x[1]))
    else:
        return '0'


def one(x='1'):
    if x != '1':
        match x[0]:
            case '+':
                return 1 + int(x[1])
            case '-':
                return 1 - int(x[1])
            case '*':
                return 1 * int(x[1])
            case '/':
                return int(1 / int(x[1]))
    else:
        return '1'


def two(x='2'):
    if x != '2':
        match x[0]:
            case '+':
                return 2 + int(x[1])
            case '-':
                return 2 - int(x[1])
            case '*':
                return 2 * int(x[1])
            case '/':
                return int(2 / int(x[1]))
    else:
        return '2'


def three(x='3'):
    if x != '3':
        match x[0]:
            case '+':
                return 3 + int(x[1])
            case '-':
                return 3 - int(x[1])
            case '*':
                return 3 * int(x[1])
            case '/':
                return int(3 / int(x[1]))
    else:
        return '3'


def four(x='4'):
    if x != '4':
        match x[0]:
            case '+':
                return 4 + int(x[1])
            case '-':
                return 4 - int(x[1])
            case '*':
                return 4 * int(x[1])
            case '/':
                return int(4 / int(x[1]))
    else:
        return '4'


def five(x='5'):
    if x != '5':
        match x[0]:
            case '+':
                return 5 + int(x[1])
            case '-':
                return 5 - int(x[1])
            case '*':
                return 5 * int(x[1])
            case '/':
                return int(5 / int(x[1]))
    else:
        return '5'


def six(x='6'):
    if x != '6':
        match x[0]:
            case '+':
                return 6 + int(x[1])
            case '-':
                return 6 - int(x[1])
            case '*':
                return 6 * int(x[1])
            case '/':
                return int(6 / int(x[1]))
    else:
        return '6'


def seven(x='7'):
    if x != '7':
        match x[0]:
            case '+':
                return 7 + int(x[1])
            case '-':
                return 7 - int(x[1])
            case '*':
                return 7 * int(x[1])
            case '/':
                return int(7 / int(x[1]))
    else:
        return '7'


def eight(x='8'):
    if x != '8':
        match x[0]:
            case '+':
                return 8 + int(x[1])
            case '-':
                return 8 - int(x[1])
            case '*':
                return 8 * int(x[1])
            case '/':
                return int(8 / int(x[1]))
    else:
        return '8'


def nine(x='9'):
    if x != '9':
        match x[0]:
            case '+':
                return 9 + int(x[1])
            case '-':
                return 9 - int(x[1])
            case '*':
                return 9 * int(x[1])
            case '/':
                return int(9 / int(x[1]))
    else:
        return '9'


def plus(x):
    return '+' + x


def minus(x):
    return '-' + x


def times(x):
    return '*' + x


def divided_by(x):
    return '/' + x
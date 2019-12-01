

def add(x):
    return x + x


def subtract(x):
    return x - x


def multiply(x):
    return x**x


def divide(x):
    return x/x


def switchMap(arg):
    switcher = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide
    }

    print(switcher[arg](2))


if __name__ == "__main__":

    print(
        '''
        1) Add 2 + 2
        2) Subtract 2 - 2
        3) Multiply 2 * 2
        4) Divide 2 / 2
        '''
    )
    x = input('What would you like to do?')

    switchMap(int(x))

    pass

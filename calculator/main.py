def add(n1, n2):
    return n1 + n2

def mult(n1, n2):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

def div (n1, n2):
    return n1 / n2


operations = {'+' : add, '-' : sub, '*' : mult, '/' : div }

def calculator ():
    should_accumulate = True
    first_number = float(input("please input first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Please input the operator: ')
        second_number = float(input('Please input second number: '))
        answer = operations[operation_symbol](first_number, second_number)
        print(f'{first_number} {operation_symbol} {second_number} = {answer}')

        choice = input(f'If you wish to continue calculation with the {answer} input y, if you wish to start new calculation input n :')

        if choice == 'y':
            first_number = answer
        elif choice == 'n':
            should_accumulate = False
            print('\n' *20)
            calculator()

calculator()
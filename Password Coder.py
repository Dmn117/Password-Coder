import os

def menu(init):
    welcome = init
    options = {
        '1': 1,
        '2': 2,
        '3': 3
    }
    option = 0;
    while (options.get(f'{option}', 0) == 0):

        hello = '│ Bienvenido!!                     │' if welcome else '│ Encantado de ayudarte de nuevo!! │'
        expression = r' ( n.n ) _/' if welcome else r' ( O.O ) _/'
        os.system('cls')
        print(r'CIFRAR │ DESCIFRAR CONTRASEÑAS');
        print('')
        print(r'  /\_/\ ')
        print(expression)
        print(r'  > . < /')
        print('┌─uu─uu────────────────────────────┐')
        print(hello)
        print('│ Que deseas hacer?                │')
        print('│ > 1. Cifrar Password             │')
        print('│ > 2. Descifrar Password          │')
        print('│ > 3. Salir                       │')
        print('└──────────────────────────────────┘')

        option = input('Ingresa una opcion ---> ')
        welcome = False
    
    return int(option)


def catWoow():
    print(r'              ┌─────────────────┐ ')
    print(r'   /\_/\      │ Woooow!         │ ')
    print(r'  ( n .n)    <  Como lo hace!!? │')
    print(r'   /   \      └─────────────────┘')
    print(r'ᘏ( nn nn)')


def catBye():
    print(r'              ┌─────────────────┐ ')
    print(r'   /\_/\      │ Byeeee!         │ ')
    print(r'  ( n .n)    <  Regresa Pronto! │')
    print(r'   /   \      └─────────────────┘')
    print(r'ᘏ( nn nn)')


def coder(password, jumps, characters):
    passEncoded = ''
    for i in password:
        index = characters.index(i.upper())
        length = len(characters)
        if (index >=  (length - jumps)):
            for i in range(jumps):
                if (index == (length - 1) - (i)):
                    passEncoded += characters[jumps-(i+1)]
        else:
            passEncoded += f'{characters[index  + jumps]}'
        passEncoded += '1' if i == f'{i}'.upper() else '0'
    return passEncoded;


def decoder(code, jumps, characters):
    passDecoded = ''
    for i in range(0, len(code), 2):
        aux = f'{characters[characters.index(code[i]) - jumps]}'
        passDecoded += aux if code[i + 1] == '1' else aux.lower()
    return passDecoded;


def app(): 
    option = menu(True)
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,'
    jumps = 10
    
    while (option != 3):
        os.system('cls')
        catWoow()

        if (option == 1):
            password = input('Ingresa la contraseña a cifrar --> ')
            passEncoded = coder(password, jumps, characters)
            print('')
            print(f'Tu Contraseña cifrada es --> {passEncoded}')

        elif (option == 2):
            code = input('Ingresa el codigo a descifrar --> ')
            passDecoded = decoder(code, jumps, characters)
            print('')
            print(f'Tu Contraseña cifrada es --> {passDecoded}')

        print('')
        os.system('pause')
        os.system('cls')
        option = menu(False)
    
    os.system('cls')
    catBye()
    os.system('pause')



if __name__ == '__main__':
    app();
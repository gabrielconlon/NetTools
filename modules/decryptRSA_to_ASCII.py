from resources import colors, menus

# Global Variables
decrypted_string = ''
c = 0
m = 0
d = 0
n = 0
e = 0

# Encryption
def encrypt():
    print(f'{colors.info}Encryption not yet supported.')

# Decryption
def decrypt(*commandStream):
    def options():
        # user input
        #TODO: check if n and d were given in the commandStream Tuple
        #TODO: check length of Tuple, consider what to do next based off that
        print(f'''
        Setup:
        To return to this menu and change values, enter OPTIONS.
        ''')
        usr_n = int(input(f'\tEnter n (default 10403): ') or '10403')
        usr_d = int(input('\tEnter d (default 8743): ') or '8743')

        return usr_n, usr_d

    n, d = options()


    if commandStream[0] in '1234567890':
        for c in commandStream.split(','):
            m = pow(int(c), d, n)
            commandStream = commandStream + chr(m)
        print(f'ASCII: {commandStream}')
    elif commandStream.lower() in 'main':
        return
    elif commandStream.lower() in 'quit':
        print('Goodbye')
        quit()
    elif commandStream.lower() in '-help':
        menus.helpMenu()
    elif commandStream.lower() in 'clear':
        commandStream = ''
        print(f'ASCII: {commandStream}')
    elif commandStream.lower() in 'delete':
        commandStream = commandStream[:-1]
        print(f'ASCII: {commandStream}')
    elif commandStream.lower() in 'options':
        options()

def menu_controller(user_choice):
    if len(user_choice) > 2:
        if user_choice in 'decrypt':
            decrypt()
        elif user_choice in 'encrypt':
            encrypt()
        elif user_choice in 'help':
            print(f"""
            {colors.run}{colors.yellow}Encrypt: {colors.end}open RSA Encryption Toolkit
            {colors.run}{colors.yellow}Decrypt: {colors.end}open RSA Decryption Toolkit
            """)
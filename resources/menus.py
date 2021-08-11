from resources import colors

# Global Variables
fileOptions = {
    '-o': 'read in filename',
    '--open': 'read in filename',
    '-f': 'output filename',
    '--file': 'output filename'
}

menus = {
"decryptRSA": f"""
    {colors.green}RSA Asymetric Decryption with ASCII Translation
    
    Enter Encrypted integers seperated by commas.
    
    {colors.run}{colors.yellow}Delete: {colors.white}remove the last character
    {colors.run}{colors.yellow}Clear: {colors.white}reset the string to null
    {colors.run}{colors.yellow}Main: {colors.white}return to Main Menu
    {colors.run}{colors.yellow}Quit: {colors.white}exit program
    """,
    "mainhelp": "Main Help Menu form menus.py"
}

def helpMenu(menu):
    print(menus[menu])

welcomeRSA = f"""
{colors.green}RSA Asymmetric Toolkit.
Enter HELP for help. 
"""

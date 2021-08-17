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
    
    {colors.run}{colors.yellow}Config: \t{colors.white}open configuration menu
    {colors.run}{colors.yellow}Delete: \t{colors.white}remove the last character
    {colors.run}{colors.yellow}Clear: \t\t{colors.white}reset the string to null
    
    {colors.run}{colors.yellow}Help: \t\t{colors.white}Show this menu
    {colors.run}{colors.yellow}Main: \t\t{colors.white}return to Main Menu
    {colors.run}{colors.yellow}Quit: \t\t{colors.white}exit program
    """,
    "mainhelp": f"""
    {colors.run}{colors.yellow}decryptRSA: \t{colors.white}enter 'n' and 'd' then decrypt 'm' (c = m ^ d % n)
    {colors.run}{colors.yellow}hextodec: \t\t{colors.white}convert hexidecimal to decimal
    {colors.run}{colors.yellow}IPconvert: \t\t{colors.white}converts any integer to binary, returns 8 digit segments
    """
}

def helpMenu(menu):
    print(menus[menu])

welcomeRSA = f"""
{colors.green}RSA Asymmetric Toolkit.
Enter HELP for help. 
"""

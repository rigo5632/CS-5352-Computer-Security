#! /usr/bin/python3

import sys
sys.path.append('./libs')
from Files import Files
from Cracker import CrackHashes
from Online import SubmitForms

# prints menu
def menu():
    print('1. Dictionary Attack')
    print('2. Random Attack')
    print('3. Online Attack')
    print('4. Exit')

if __name__ == '__main__':
    forms = SubmitForms()       # online attack init
    files = Files()             # file manipulation init
    dictionaryAccounts, randomAccounts = None, None     
    cracker = None
    exitCommand = 0

    while not exitCommand:
        menu()
        userInput = int(input('> '))

        if userInput == 1:          # dictionary attack
            if not dictionaryAccounts:
                dictionaryAccounts, _ = files.getUserInformation()
                passwords = files.getPasswordsFromFile()
                cracker = CrackHashes(dictionaryAccounts, '', passwords, files)
            cracker.dictionaryAttack()
        elif userInput == 2:    # random attack
            if not randomAccounts:
                _, randomAccounts = files.getUserInformation()
                cracker = CrackHashes('', randomAccounts, '', files)
            cracker.randomAttack()
        elif userInput == 3:     # online attack
            forms.generatePasswords()
        else:                   # exit
            exitCommand = 1     
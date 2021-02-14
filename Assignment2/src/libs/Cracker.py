#! /usr/bin/ptyhon3
import time, hashlib
from itertools import permutations

class CrackHashes():
    def __init__(self, dictionaryShadow, randomShadow, passwords, files):
        self.dictionaryShadow = dictionaryShadow
        self.randomShadow = randomShadow
        self.passwords = passwords
        self.alphabet = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',       #alphabet contains 64 characters
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_'
        ]
        self.csvFile = files

    def hashPassword(self, password, salt):
        testPassword = password + salt                          # combine salt with string password
        hash256Password = hashlib.sha256(testPassword.encode()) # hash poassword with hash256
        hash256Password = hash256Password.hexdigest()           # get string value of hash256
        hash1Password = hashlib.sha1(hash256Password.encode())  # hash password in hash1
        hash1Password = hash1Password.hexdigest()               # get string value of hash1

        return hash1Password
    
    def getPassword(self, passwords, user, startTime):
        for i in range(len(passwords)):                     # get characters concatinate them into strings
            phrase = ''
            for j in range(len(passwords[i])):
                phrase += passwords[i][j]
            possibleHash = self.hashPassword(phrase, '')   # hash password

            if possibleHash == user['hash']:                # check if hash matches with user
                username = user['username']
                endTime = time.perf_counter()
                totalTime = endTime - startTime
                self.csvFile.addToAnswerSheet(user, phrase, totalTime, 0)   # record data
                return True
        return False

    
    def dictionaryAttack(self):
        print('Brute Force: Dictionary Attack')
        self.csvFile.setUpCSVFile(1)                        # sets the headers for the csv file
        users = list(self.dictionaryShadow.keys())          # gets all usernames from dictionary
        startTimer = time.perf_counter()                    # starts timer

        for user in users:
            for password in self.passwords:
                userSalt = self.dictionaryShadow[user]['salt']
                userHash = self.dictionaryShadow[user]['hash']
                possibleHash = self.hashPassword(password, userSalt) #hashes password
            
                if possibleHash == userHash:                         # verifies that the password and the userpassword is the same
                    stopTimer = time.perf_counter()
                    totalTime = stopTimer - startTimer
                    self.csvFile.addToAnswerSheet(self.dictionaryShadow[user], password, totalTime, 1) #records data in csv file
                    break
    
    def randomAttack(self):
        print('Brute Force: Random Attack')
        self.csvFile.setUpCSVFile(0)                # sets all headers for the csv file
        users = list(self.randomShadow.keys())      # gets all usernames from dictionary
        passwordLength = 1                          # passwords length
        startTimer = time.perf_counter()            # timer start
        cracked = False

        while True:
            for user in users:
                passwords = list(permutations(self.alphabet, passwordLength))               # generate permutations from alphabet
                cracked = self.getPassword(passwords, self.randomShadow[user], startTimer)  # checks if password was found

                if cracked:
                    users.remove(user)              # remove user from dictionary
                    passwordLength += 1             # increase password length to 2
                    cracked = False
            
            if passwordLength == 5: break           # break after five passwords have been found


    

    



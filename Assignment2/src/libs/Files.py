#! /usr/bin/python3
import re, csv

# Files class will extarct data from files and put them in data structures
# This class will also add data to csv files
class Files():
    # file locations
    def __init__(self):
        self.accountsToCrack = '../Passwords/passwords.txt'
        self.passwords = '../Passwords/words_alpha.txt'
        self.dictionaryFile = {
            'path':'../Answers/Dictionary.csv',
            'fields': ['username', 'salt', 'hash', 'password', 'time']
        }
        self.randomFile = {
            'path': '../Answers/Random.csv',
            'fields': ['username', 'hash', 'password', 'time']
        }
    
    #extract data from account files and put sort them if
    #salt was provided or not
    def getUserInformation(self):
        dictionaryAccounts, randomAccounts = {}, {}
        accountsFile = open(self.accountsToCrack, 'r')
        haveSalt = False

        line = accountsFile.readline()
        while line:
            if line == 'Dictionary\n':
                haveSalt = True
                line = accountsFile.readline()
            elif line == 'Random\n':
                haveSalt = False
                line = accountsFile.readline()

            line = re.split('[\s,]', line)

            if haveSalt: dictionaryAccounts[line[0]] = {'username': line[0], 'salt': line[2], 'hash': line[4]}
            else: randomAccounts[line[0]] = {'username': line[0], 'hash': line[2]}

            line = accountsFile.readline()
        return (dictionaryAccounts, randomAccounts)
    
    #extract all passwords from password file
    def getPasswordsFromFile(self):
        passwords = []
        passwordFile = open(self.passwords, 'r')

        line = passwordFile.readline()

        while line:
            password = re.split('\s', line)
            passwords.append(password[0])

            line = passwordFile.readline() 
        return passwords
    
    # adds user information, password, and time to csv file.
    def addToAnswerSheet(self, entry, password, time, entryType):
        entry['password'], entry['time'] = password, time
        path = self.dictionaryFile['path'] if entryType else self.randomFile['path']
        fields = self.dictionaryFile['fields'] if entryType else self.randomFile['fields']
        
        with open(path, 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames = fields)
            writer.writerow(entry)
    
    # creates csv file if it has not been created
    def setUpCSVFile(self, fileType):
        path = self.dictionaryFile['path'] if fileType else self.randomFile['path']
        fields = self.dictionaryFile['fields'] if fileType else self.randomFile['fields']
        
        with open(path, 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames = fields)
            writer.writeheader()


        

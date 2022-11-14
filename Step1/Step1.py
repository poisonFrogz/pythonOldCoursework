from datetime import*
from pprint import *
from json import *



# this function is used to validate integer validation
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('ERROR: Please enter a NUMBER')
            continue
        else:
            return userInput
            break


class Batch:

    def __init__(self,BatchNo,Date):
        self.BatchNo = BatchNo
        self.Date = Date


class Component:
    def __init__(self,componentType,fitmentType):

        self.componentType = componentType
        self.fitmentType = fitmentType

    componentType = {'1': 'Winglet Strut', '2': 'Door Handle', '3': 'Rudder Pin'}
    fitmentType = {'1': 'A320 Series', '2': 'A380 Series'}


def newln():
    print()


print('--WELCOME TO THE PPEC BATCH PROGRAM--')
# newln() just prints a new line

newln()

counter = 0
while True:
    # the counter is to generate the last part of the sequence number
    counter = counter + 1

    # square brackets represent the choice that the user has at this time
    print('[1]Create New Batch')
    print('[2]Quit Program')
    newln()

    userChoice = input('Please Press the key 1 or 2:')
    newln()

    if userChoice == '1':
        date = datetime.now()
        print('--CREATING NEW BATCH--')

        newln()

        # format for batch number is YYYYMMDD9999
        # Another note, str(counter).zfill(4) is what gives us the 4 digit unique sequence
        batchNo = Batch.BatchNo = (date.strftime('%Y')+date.strftime('%m')+date.strftime('%d')+str(counter).zfill(4))
        print('Batch Number: ', Batch.BatchNo)

        noOfComp = inputNumber('Please enter the amount of components in this batch')

        while noOfComp < 1 or noOfComp > 9999:
            print('ERROR: the number of components can only be between 1 and 9999')
            newln()
            noOfComp = int(input('Please enter a revised number of components.'))

        # I will be using this variable to store the corresponding type of component to the number chosen
        compTypeChoice = ''
        fitTypeChoice = ''

        newln()
        print('---TYPE OF COMPONENTS---')
        newln()
        print('[1] Winglet Strut')
        newln()
        print('[2] Door Handle')
        newln()
        print('[3} Rudder Pin')
        newln()
        compType = 0
        fitmentType = 0
        val = ''
        while compType != '1' or compType != '2' or compType != '3':
            compType = input('Please enter what type of component is in this batch')

            newln()

        # Note on the next section of code, the indented code of the if statements calls the values of the dictionaries above

            if compType == '1':
                compTypeChoice = Component.componentType['1']
                break

            elif compType == '2':
                compTypeChoice = Component.componentType['2']
                break
            elif compType == '3':
                compTypeChoice = Component.componentType['3']
                break
            else:
                print('ERROR: Invalid Input, Please try again')
                newln()

        newln()
        print('---TYPE OF FITMENT---')
        newln()
        print('[1] A320 Series')
        newln()
        print('[2] A380 Series')
        newln()

        while fitmentType != '1' or fitmentType != '2':
            fitmentType = input('Please enter the type of fitment')

            if fitmentType == '1':
                fitTypeChoice = Component.fitmentType['1']
                break

            elif fitmentType == '2':
                fitTypeChoice = Component.fitmentType['2']
                break

            else:
                print('ERROR: Invalid Input')
                newln()
                fitmentType = input('Please enter a revised fitment type')

        newln()
        print('---CONFIRMATION OF BATCH---')
        newln()
        print('Does the entered Batch contain the following?')
        print(noOfComp, ' ', fitTypeChoice, ' ', compTypeChoice)

        while val != 'Y' or val != 'y' or val != 'N' or val != 'n':
            val = input('[Y] / [N] ?')
            if val == 'Y' or val == 'y':
                print('Batch and Component details recorded at: ', date.strftime('%H'), date.strftime('%M'), ' On the date: ', date.strftime('%Y'), date.strftime('%m'), date.strftime('%d'))
                newln()
                BatchData = {'Batch Number': batchNo, 'Number of components': noOfComp, 'Component Type': compType}

                break
            elif val == 'N' or val == 'n':
                print('Batch and Component details Scrapped')
                newln()
                # this line is important for correct indexing
                # if the user decides to scrap the batch without this line the program would assume the next batch number to be YYYYMMDD0002
                counter = counter - 1
                break
            else:
                print('ERROR: Invalid Input')
                newln()

        SerialNumbers = []
        # Serial Numbers
        Scounter = 0
        while Scounter < noOfComp:
            Scounter = Scounter + 1
            SerialNumbers.append(batchNo + '-' + str(Scounter).zfill(4))

        val = 0
        while val != 'Y' or val != 'y' or val != 'N' or val != 'n':
            val = input('Would you like to print the batch details? ([Y] / [N]')
            if val == 'Y' or val == 'y':
                print('---BATCH DETAILS---')
                newln()
                print('Batch Number: ', batchNo)
                newln()
                print('Manufacture Date: ', date.strftime('%Y') + '-' + date.strftime('%m') + '-' + date.strftime('%d'))
                newln()
                print('Component Type: ', compTypeChoice)
                newln()
                print('Fitment Type: ', fitTypeChoice)
                newln()
                print('Number of components in batch: ', noOfComp)
                newln()
                print('Serial Numbers: ', SerialNumbers)
                newln()
                Scounter = 0
                while Scounter < noOfComp:
                    Scounter = Scounter + 1
                    print('Component Status: ', SerialNumbers[Scounter-1], ' ', 'Manufactured-Unfinished', '\n')

                break

            elif val == 'N' or val == 'n':
                print('Batch and Component details Scrapped')
                newln()
                # this line is important for correct indexing
                # if the user decides to scrap the batch without this line the program would assume the next batch number to be YYYYMMDD0002
                counter = counter - 1
                break
            else:
                print('ERROR: Invalid Input')
                newln()
        batchNumbers = []
        batchNumbers.append(batchNo)

        outdata={'Batch Numbers: ': batchNumbers}

        with open('BatchIndex.json', 'w') as f:
            dump(outdata, f)

        f.close()

        with open('BatchIndex.json', 'r') as f:
            indata = load(f)

        f.close()


        pprint(indata)

    elif userChoice == '2':
        print('Program Exited')
        # breaks the while True loop therefore terminating the program
        break

    else:
        print('Invalid Input')
        counter = counter - 1


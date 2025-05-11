#Numerology Assignment
class Numerology:
    def __init__(self, sName, sDOB):
        self.name = sName
        self.dob = sDOB

    def getName(self):
        return self.name

    def getBirthdate(self):
        return self.dob

    def reduceNumber(self, number):
        while number > 9:
            number = sum(int(digit) for digit in str(number))
        return number

    def getLifePath(self):

        #Remove any non-digit characters from the date
        digits = ''.join(filter(str.isdigit, self.dob))

        sum_of_digits = sum(int(digit) for digit in digits)
        return self.reduceNumber(sum_of_digits)

    def getBirthDay(self):
        day = int(self.dob[3:5])  #This will extract the day form the total date.
        return self.reduceNumber(day)

    def getAttitude(self):
        month = int(self.dob[0:2])  #This will extract the month from the total date.
        day = int(self.dob[3:5])
        return self.reduceNumber(month + day)

    def convertNameToNumbers(self):
        letter_values = {
            'A': 1, 'J': 1, 'S': 1,
            'B': 2, 'K': 2, 'T': 2,
            'C': 3, 'L': 3, 'U': 3,
            'D': 4, 'M': 4, 'V': 4,
            'E': 5, 'N': 5, 'W': 5,
            'F': 6, 'O': 6, 'X': 6,
            'G': 7, 'P': 7, 'Y': 7,
            'H': 8, 'Q': 8, 'Z': 8,
            'I': 9, 'R': 9
        }
        name = self.name.upper()
        numbers = []
        for char in name:
            if 'A' <= char <= 'Z':
                numbers.append(letter_values[char])
            else:
                numbers.append(0)
        return numbers

    def getSoul(self):
        vowels = "AEIOU"
        numbers = self.convertNameToNumbers()
        vowel_sum = sum(num for i, num in enumerate(numbers) if self.name[i].upper() in vowels)
        return self.reduceNumber(vowel_sum)

    def getPersonality(self):
        vowels = "AEIOU"
        numbers = self.convertNameToNumbers()
        consonant_sum = sum(num for i, num in enumerate(numbers) if self.name[i].upper() not in vowels)
        return self.reduceNumber(consonant_sum)

    def getPowerName(self):
        return self.reduceNumber(self.getSoul() + self.getPersonality())


import re  #Using for date validation


def get_valid_date():
    while True:
        date_str = input("Date of Birth (mm/dd/yyyy or mm-dd-yyyy): ")
        if re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', date_str):
            return date_str
        else:
            print("Invalid date format. Please use mm-dd-yyyy or mm/dd/yyyy.")


def get_valid_name():
    while True:
        name_str = input("Full Name: ")
        if name_str:
            return name_str
        else:
            print("Error. Please enter your name.")


if __name__ == "__main__":
    name = get_valid_name()
    dob = get_valid_date()

    numerology = Numerology(name, dob)

    #Get the calculated numbers and assign them a value.
    life_path = numerology.getLifePath()
    birth_day = numerology.getBirthDay()
    attitude = numerology.getAttitude()
    soul = numerology.getSoul()
    personality = numerology.getPersonality()
    power_name = numerology.getPowerName()

    #Go to screen.
    print("\nClient Name:", name.upper())
    print("Client DOB:", dob)
    print(f"\n {name}'s Numerology Results:")
    print("*****************************************")
    print(f" Life Path Number:......{life_path}")
    print(f" Birth Day Number:......{birth_day}")
    print(f" Attitude Number:.......{attitude}")
    print(f" Soul Number:...........{soul}")
    print(f" Personality Number:....{personality}")
    print(f" Power Name Number:.....{power_name}")
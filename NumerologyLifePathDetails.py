#Numerology II Assignment

class Numerology:
    def __init__(self, sName, sDOB):
        self.name = sName
        self.dob = sDOB

    @property
    def Name(self):
        return self.name

    @property
    def Birthdate(self):
        return self.dob

    def reduceNumber(self, number):
        while number > 9:
            number = sum(int(digit) for digit in str(number))
        return number

    @property
    def LifePath(self):

        #Remove any non-digit characters from the date
        digits = ''.join(filter(str.isdigit, self.dob))

        sum_of_digits = sum(int(digit) for digit in digits)
        return self.reduceNumber(sum_of_digits)

    @property
    def BirthDay(self):
        day = int(self.dob[3:5])  #This will extract the day form the total date.
        return self.reduceNumber(day)

    @property
    def Attitude(self):
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

    @property
    def Soul(self):
        vowels = "AEIOU"
        numbers = self.convertNameToNumbers()
        vowel_sum = sum(num for i, num in enumerate(numbers) if self.name[i].upper() in vowels)
        return self.reduceNumber(vowel_sum)

    @property
    def Personality(self):
        vowels = "AEIOU"
        numbers = self.convertNameToNumbers()
        consonant_sum = sum(num for i, num in enumerate(numbers) if self.name[i].upper() not in vowels)
        return self.reduceNumber(consonant_sum)

    @property
    def PowerName(self):
        return self.reduceNumber(self.Soul + self.Personality)


class NumerologyLifePathDetails(Numerology):
    def __init__(self, sName, sDOB):
        #Call the parent class's constructor
        super().__init__(sName, sDOB)

    @property
    def LifePathDescription(self):
        life_path_number = self.LifePath #To access from the parent class

        #Dictionary to bind Life Path numbers to a given description.
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way",
        }

        #Return the description
        return descriptions.get(life_path_number, "Description not available for this Life Path number.")


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
            print("Error. Please enter your full name.")


if __name__ == "__main__":
    name = get_valid_name()
    dob = get_valid_date()

    #Use the new inherited class
    numerology = NumerologyLifePathDetails(name, dob)

    #Go to screen.
    print("\nClient Name:", name.upper())
    print("Client DOB:", dob)
    print(f"\n {name}'s Numerology Results:")
    print("*****************************************")
    #Access and print results using the new properties
    print(f" Life Path Number:......{numerology.LifePath}")
    #Print the new Life Path Description property
    print(f" Life Path Description:.{numerology.LifePathDescription}")
    print(f" Birth Day Number:......{numerology.BirthDay}")
    print(f" Attitude Number:.......{numerology.Attitude}")
    print(f" Soul Number:...........{numerology.Soul}")
    print(f" Personality Number:....{numerology.Personality}")
    print(f" Power Name Number:.....{numerology.PowerName}")
    print("*****************************************")
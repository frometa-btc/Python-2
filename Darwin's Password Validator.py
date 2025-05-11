# Intro Message
print("** Welcome to Darwin's Password Creation Tool **")
print("------------------------------------------------\n")


def extract_initials(sName):
    # Extracts the first initials from the first and last name.
    first_initial = sName.split()
    last_initial = sName.split()
    return first_initial + last_initial


# Password validator function
def password_validator(sInitials, sPassword):
    # Initialize a list to store error messages
    error_messages = []

    # Check password length
    if not 8 <= len(sPassword) <= 12:
        error_messages.append(" → Password must be between 8 and 12 characters.")

    # Check for starting with "Pass"
    if sPassword.lower().startswith("pass"):
        error_messages.append(" → Password can't start with 'Pass'.")

    # Check for uppercase
    if not any(c.isupper() for c in sPassword):
        error_messages.append(" → Password must contain at least 1 uppercase letter.")

    # Check for lowercase
    if not any(c.islower() for c in sPassword):
        error_messages.append(" → Password must contain at least 1 lowercase letter.")

    # Check for number
    if not any(c.isdigit() for c in sPassword):
        error_messages.append(" → Password must contain at least 1 number.")

    # Check for special character
    special_chars = "!@#$%^"
    if not any(c in special_chars for c in sPassword):
        error_messages.append(" → Password must contain at least 1 of these special characters:! @ # $ % ^")

    # Check for initials
    if 'sInitials' in sPassword:
        error_messages.append(" → Password must not contain user initials.")

    # Check for repeating characters
    char_counts = {}
    for char in sPassword.lower():
        char_counts[char] = char_counts.get(char, 0) + 1

    repeating_chars = {char: count for char, count in char_counts.items() if count > 1}
    if repeating_chars:
        repeat_message = "These characters appear more than once: \n"
        for char, count in repeating_chars.items():
            repeat_message += f"{char}: {count} \n"
        error_messages.append(repeat_message)

    # Return error messages or declare valid
    if error_messages:
        return error_messages
    else:
        return "Password is valid and OK to use."


def main():
    sName = input("Please enter your first and last name: ")

    while True:
        sPassword = input("Please create a password: ")

        # Extract initials
        sInitials = extract_initials(sName)

        # Validate password
        validation_result = password_validator(sInitials, sPassword)

        # Print validation results
        if isinstance(validation_result, list):
            print("Password is not valid:")
            for message in validation_result:
                print(message)
        else:
            print(validation_result)
            break

if __name__ == "__main__":
    main()
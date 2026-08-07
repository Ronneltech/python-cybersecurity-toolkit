# Ronneltech Ltd
# Python Cybersecurity Toolkit
# Tool: Password Strength Analyzer

import string


def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    print("\nPassword Security Analysis")
    print("-------------------------")

    if score == 5:
        print("Strength: Very Strong")
    elif score >= 3:
        print("Strength: Medium")
    else:
        print("Strength: Weak")

    print(f"Security Score: {score}/5")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print("- " + item)


if __name__ == "__main__":
    password = input("Enter password to analyze: ")
    check_password_strength(password)

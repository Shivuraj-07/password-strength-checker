import re


def check_password_strength(password):
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check numbers
    if re.search(r"\d", password):
        score += 1

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Password strength result
    if score == 5:
        return "Very Strong Password"
    elif score >= 4:
        return "Strong Password"
    elif score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"


# User input
password = input("Enter your password: ")

# Display result
strength = check_password_strength(password)

print("\nPassword Strength:", strength)

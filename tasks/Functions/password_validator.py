
def has_minimum_length(password):
    return len(password) >= 8


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def validate_password(password):
    checks = {
        "Minimum length": has_minimum_length(password),
        "Contains digit": has_digit(password),
        "Contains uppercase": has_uppercase(password),
        "Contains lowercase": has_lowercase(password)
    }

    for requirement, passed in checks.items():
        print(f"{requirement}: {passed}")

    return all(checks.values())


password = "Python2026"

if validate_password(password):
    print("Password is valid")
else:
    print("Password is invalid")

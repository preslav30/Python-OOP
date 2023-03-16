class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username



    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        capital_found = False
        digit_found = False
        for n in range(len(value)):
            if value[n].isupper():
                capital_found = True
            elif value[n].isdigit():
                digit_found = True

        if len(value) < 8 or not capital_found or not digit_found:
            raise ValueError(
                "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            self.__password = value

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)


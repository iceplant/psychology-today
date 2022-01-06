from googlevoice import Voice


def main():
    login()


def login():
    username, password = "rockyjkremail", "[2[+h+phVu-VH<_A"
    voice = Voice()
    client = voice.login(username, password)
    return client


NAME = "Rocky Kamen-Rubio"
EMAIL = "rockykamenrubio@gmail.com"
PHONE = "5106204724"
SUBJECT = "Intake Appointment"
THERAPIST_MESSAGE = "Hello, my name is Rocky and I'm looking for a therapist who is in-network with unitedhealthcare. I'm open to telehealth or in-person in Oakland. Are you currently accepting new clients? Thanks! -Rocky"
PSYCH_MESSAGE = "Hello, my name is Rocky and I'm looking for a therapist who is in-network with unitedhealthcare. I'm open to telehealth or in-person in Oakland. Are you currently accepting new clients? Thanks! -Rocky"
TEST_MESSAGE = "Hey Linsay, this is Rocky testing my therapist outreach bot. Hope you're having a magical time in Hawaii! When you get the chance, could you let me know that you got this message? Thanks!"


def submit_email_form():
    # figure out captcha
    pass


# def send_text():

if __name__ == "__main__":
    main()

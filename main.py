import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import json
import getpass
import traceback

sender_address = ""
sender_pass = ""


class Users:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def __eq__(self, o: object) -> bool:
        return self.name == o.name

    def __hash__(self):
        return hash(self.name + self.email)

    def __repr__(self):
        return json.dumps(dict(name=self.name, email=self.email))

    def __str__(self):
        return json.dumps(dict(name=self.name, email=self.email))


def mail_content(user: Users, friend: Users):
    return f"""Hola {user.name}, este es el resultado del amigo invisible. Te toco {friend.name}, exitos con el regalo!"""


def deleteme_from_array(users, user_to_remove):
    user_list = list(filter(lambda user: user != user_to_remove, users))
    assert user_to_remove not in user_list
    return user_list


def get_users_form_data():
    users = []
    with open("data.json", "r") as dfd:
        _data = dfd.read()
        data = json.loads(_data)
    for d in data:
        users.append(Users(**d))
    return users


def main():
    users_selected = []
    matchs = []
    users = get_users_form_data()
    for u in users:
        users_without_me = deleteme_from_array(users, u)
        posibles = set(users_without_me) - set(users_selected)
        user = random.choice(list(posibles))
        match = {"user": u, "friend": user}
        users_selected.append(user)
        matchs.append(match)
    return matchs


def send_mails(matchs):
    session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
    session.starttls()
    session.login(sender_address, sender_pass)  # login with mail_id and password

    for match in matchs:
        receiver_address = match["user"].email

        message = MIMEMultipart()
        message["From"] = sender_address
        message["To"] = receiver_address
        message["Subject"] = "Resultado del Amigo invisible"
        message.attach(MIMEText(mail_content(match["user"], match["friend"]), "plain"))
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)

    session.quit()


if __name__ == "__main__":
    sender_address = input("Email sender account: ")
    sender_pass = getpass.getpass("Email sender password: ")
    tries = 0
    while True:
        try:
            matchs = main()
            send_mails(matchs)
            break
        except Exception as e:
            tries += 1
            if tries == 3:
                traceback.print_exc()
                print("Error many times - %s", e)
                break
            else:
                continue
    print("Done!")

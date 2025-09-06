import random
import smtplib
import datetime as dt
import pandas

PLACEHOLDER = "[NAME]"

birth_day = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays_dict = {
    (row["month"], row["day"]): row for (index, row) in birth_day.iterrows()
}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    name = person["name"]
    email = person["email"]

    letter_file = random.choice(["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                                 "letter_templates/letter_3.txt"])
    with open(letter_file) as lf:
        contents = lf.read()
        contents = contents.replace(PLACEHOLDER, name)

    my_email = "jainchinmay2005@gmail.com"
    with open("password.env") as f:
        password = f.read().strip()

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{contents}")

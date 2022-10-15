import string
import secrets
import pandas as pd
import datetime as dt

symbols = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', '@', '~', '#', '<', '>', '?']
password = ""

for _ in range(4):
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
password += secrets.choice(symbols)
print(password)

path = "C:\\Users\\vinot\\OneDrive\\1. Personal\\3. Pass log\\Pass.xlsx"
history = pd.read_excel(path)
runnow = pd.DataFrame(columns=['Date & Time', 'Password'])
now = dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
runnow.loc[0, ['Date & Time']] = now
runnow.loc[0, ['Password']] = password
history = pd.concat([history, runnow], ignore_index=True)
history.to_excel(path, index=False)

# import secrets
# password_length = 12
# print(secrets.token_urlsafe(password_length) + "@$")
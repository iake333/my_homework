#1.დაუსვამს კითხვებს მომხმარებელს და შექმნის მის ობიექტს სპეციალური კლასისგან.
#გაუკეთებს სერიალიზაციას და შექმნის pickleფაილს რესპოდენტის სახელით.

import pickle

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# მომხმარებელის ინფორმაცია
username = input("Enter username: ")
email = input("Enter email: ")

# User ობიექტის შექმნა
user = User(username, email)

# Pickle ფაილში შენახვა
file_name = f"{user.username}.pickle"
with open(file_name, 'wb') as f:
    pickle.dump(user, f)

print(f"User '{user.username}' შენახულია '{file_name}' ფაილში.")

# დაწერე ფუნქცია რომელიც სასურველი რესპონდენტის ფაილს გახსნის, 
# დესერიალიზაციას გაუკეთებს და შედეგს დაბეჭდავს.
import pickle

def open_and_read_pickle(file_name):
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return None

# ფაილის სახელი
file_name = "desired_recipient.pickle"

# ფაილის გახსნა და დესერიალიზაცია
recipient = open_and_read_pickle(file_name)

# შედეგის დაბეჭდვა
if recipient:
    print("შედეგი:")
    print(recipient)
else:
    print("ფაილი ვერ მოიძებნა ან გამოყენებადი შეცდომა მქონდა.")


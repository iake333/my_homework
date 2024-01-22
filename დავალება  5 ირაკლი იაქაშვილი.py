# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ. თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია დაამატე საერთო ცალრიელ სიას სახელად consumer_info. Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21
# 2.

names = []
surnames = []
ages = []
user_count = 0
while user_count < 3:
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")

    names.append(name)
    surnames.append(surname)
    ages.append(age)

    user_count += 1
    consumer_info_input = list(zip(names, surnames, ages))
print("\nConsumer Information:")
for idx, (name, surname, age) in enumerate(consumer_info_input):
    print(f"Index {idx}: Name: {name}, Surname: {surname}, Age: {age}")

#  user input for index
while True:
    try:
        user_index = int(input("Enter the index to retrieve information: "))
        if 0 <= user_index < len(consumer_info_input):
            break
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")


selected_user = consumer_info_input[user_index]
print("\nSelected Information:")
print(f"\nName: {selected_user[0]},\n Surname: {selected_user[1]}, \n Age: {selected_user[2]}")

#  მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე თუ სახელის ველი არ იქნება ცარიელი,
# ხოლო პაროლი 8 სიმბოლოზე მეტი ან ტოლია. მისი მონაცემები შეინახე ლისთში.
# შემდეგ მიეცი საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე მის მიერ შემოყვანილი ინფორმაცია სიაში შენახულ ინფორმაციას. დაბეჭდე შესაბამისი მესიჯი.


users=[]
passwords=[]
while True:
 user_login=input("user login(note enter least 1 simbol): ")
 user_password=input("user password(password must be more then 8 characters ): ")

 if user_login !=" " and len(user_password) >=8:
   users.append(user_login)
   passwords.append(user_password)
   print(users,"\n",passwords )
   break
 else:print("you entered incorect parameter please try again")  
while True:
 registation_user=input("enter your username to log in: ")
 registation_password=input("enter your registration password: ") 

 if registation_user  in users and registation_password in passwords:
  print("you succesfuly registered")
  break
 else:print("your user or password is incorect try again")
 continue

# შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია. მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდა მის შესახებ არსებული ინფორმაცია რეზუმის სახით.


people_info = [
    ["garry", "oldman", 70, "actor", "active"],
    ["tom", "cruse", 55, "actor", "active"],
    ["pamela", "anderson", 60, "model", "passive"]
]


search_key = input("please enter name or surname: ").lower()

found_person = None
for person in people_info:
    if search_key in [person[0].lower(), person[1].lower()]:
        found_person = person
        break

if found_person:
    print(f"found person:  {found_person[0]}, {found_person[1]}, age: {found_person[2]}, proffesion: {found_person[3]}, status: {found_person[4]}",sep="\n")
else:
    print(f"{search_key}-data not found.")
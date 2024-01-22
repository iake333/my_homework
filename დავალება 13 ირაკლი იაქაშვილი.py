# 1. დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით,
#  მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.


with open("test.txt", "a") as f:
    while True:
        answer = input("Enter Text: ")
        if answer.lower() == "enough":
            break

        f.write(f"{answer}\n")

# 2. დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს,
# შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

import os


location = input("შეიყვანეთ ლოკაცია: ")
file_name = input("შეიყვანეთ ფაილის სახელი: ")
file_path = os.path.join(location, file_name)
with open(file_path, "w") as file:
    file.write("Hello, this is your new file!")

# List files in the specified directory
dir_list = os.listdir(location)
print(f"Files in {location}: {dir_list}")

#1.	რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას, რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)

def greeting(n):
    if n==0:
        return " "
    elif n>=0 :
     return " hello"+greeting(n-1)
    else:
       return "error"
    
print(greeting(10),sep=" ") #nika ver vxvdebi separatori ratom ar mushaobs

# 2.	შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას,
# თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.

def kerdzi(name, number=1):
  message = f"kerdzi dasaxeleba: {name}, raodenoba: {number}"
  print(message) 
  return message

kerdzi("xarcho", )
kerdzi("baje", )
#3.	შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს,  და დააბრუნებს და დაბეჭდავს ნარმავლს.


def calculate_product(*numbers):
    
    try:
        if len(numbers) < 3:
            return "Please provide at least 3 numbers to calculate the product."

        
        if not all(isinstance(num, int) for num in numbers):
            return "Please enter integers only."

        
        product = 1
        for num in numbers:
            product *= num

        return product
    except ValueError:
        return "Invalid input. Please enter valid integers."


try:
    user_input = input("Enter at least 3 integers separated by space: ")
    user_numbers = [int(num) for num in user_input.split()]

    
    result = calculate_product(*user_numbers)

    
    print(result)
except ValueError:
    print("Invalid input. Please enter valid integers.")
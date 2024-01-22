#1.	დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.

list1=[lambda arg=y:arg*3 for y in range(1,5)]
for fun in list1:
    print(fun())

# 2.	დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, 
# მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება.  (გამოიყენე .isupper() მეთოდი)    
    
lis1=["Irakli","sopo","Lasha","levani","salome"]
list_of_functions = [lambda x=x:  x.count(x[0]) for x in lis1 if not x[0].isupper()]
total_sum = sum(fun() for fun in list_of_functions)
print("total number of elements with lowercase: ",total_sum)


#3.	დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter

my_list = [1, -5, 6, 5, -2, -8]


filtered_lists = [
    list(filter(lambda x: x < 0, my_list)),
    list(filter(lambda x: x > 0, my_list))]
print(filtered_lists)
sum_negative = sum(filtered_lists[0])
sum_positive = sum(filtered_lists[1])
print("Sum of negative numbers:", sum_negative)
print("Sum of positive numbers:", sum_positive)

#4.	დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა,
#არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.

usernames = []
passwords = []
balances = []

while True:
    choice = input("Choose an option (1 - Create Account, 2 - Login, Q - Quit): ").upper()

    if choice == '1':
        user = input("Enter your username: ")
        password = input("Choose your password: ")
        initial_balance = float(input("Enter initial balance: "))

        try:
            if initial_balance < 0:
                raise ValueError("Initial balance must be non-negative.")

            usernames.append(user)
            passwords.append(password)
            balances.append(initial_balance)

            print(f"Account created for {user} with balance: {initial_balance}")
        except ValueError as ve:
            print(f"Error: {ve}")

    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in usernames and passwords[usernames.index(username)] == password:
            print(f"Welcome, {username}! Your balance is: {balances[usernames.index(username)]}")
        else:
            print("Incorrect username or password. Please try again.")

    elif choice == 'Q':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
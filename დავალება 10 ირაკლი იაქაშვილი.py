#1.	დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას. 
# 2.	დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით. 
# 3.	დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება. 
# 4.	დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში.


import time
from random import randint
def list_generator(list_size=50000):

    arr = [randint(1, 500) for _ in range(list_size)]  # Concise list generation
    return arr

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execute_time = end_time - start_time
        print(f"Execution time: {execute_time:.20f} seconds")
        return result
    return wrapper

@measure_execution_time
def binary_search(list1, element):
  
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high) // 2
        if list1[mid] == element:
            return mid
        elif list1[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Element not found

list1 = list_generator()
list1.sort()  # Sort for binary search

element = int(input("Enter number: "))

result = binary_search(list1, element)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")
#
#linear search
import time
from random import randint
def list_generator(list_size=50000):

    arr = [randint(1, 500) for _ in range(list_size)]  
    return arr

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execute_time = end_time - start_time
        print(f"Execution time: {execute_time:.20f} seconds")
        return result
    return wrapper

@measure_execution_time
def search_linear(list1, element):
    for i in range(len(list1)):
        if list1[i] == element:
            return i

    return -1
  

list1 = list_generator()
list1.sort()  

element = int(input("Enter number: "))

result = search_linear(list1, element)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")  


#დასკვნა ბინარული ძიება განასაკუთრებით დიდი რაოდენობის მონაცემებზე კოლოსალურად სწრაფია
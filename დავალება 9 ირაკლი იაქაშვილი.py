#1.	დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).
from random import randint
random_list = [randint(1, 100) for i in range(10)]
print(random_list)
random_list.sort()
print("dasortirebuli: ",random_list)

#2.	დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).
from random import randint
random_list = [randint(1, 100) for i in range(10)]
print(random_list)
sorted_list=sorted(random_list,reverse=True)
print("klebadobit: ",sorted_list)
#3.	დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection).
#  დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია მცირე(1000 ელემენტი),
#  საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.
import time
from random import randint
random_list = [randint(1, 1000) for i in range(3000)]


def bubble(random_list):
    start_time=time.time()
    indexing_length = len(random_list) - 1
    sorteed = False
 
    while not sorteed:
        sorteed = True
        for i in range(0, indexing_length):
            if random_list[i] > random_list[i+1]:
                sorteed = False
                random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]
    print("Bubble Sort!")
    end_time=time.time()
    execute_time=end_time-start_time
    print(f"shesrulebis dro,{execute_time:.3f}")
    return list(random_list)



print(random_list)
print("********************")
print(bubble(random_list))
#1000 ze 0.068
#2000 ze 0.240
#3000 ze 0.603

#shell sortis shemtxvevashi
import time
from random import randint
random_list = [randint(1, 1000) for i in range(1000)]

def shell_sort(some_arr):
    start_time=time.time()
    random_list = some_arr
    a = len(random_list)
    gap = a // 2

    while gap > 0:
        for i in range(gap, a):
            anchor = random_list[i]
            j = i
            while j >= gap and random_list[j-gap] > anchor:
                random_list[i] = random_list[j-gap]
                j -= gap

            random_list[j] = anchor
        gap //= 2
    end_time=time.time()
    execute_time=end_time-start_time
    print(f"shesrulebis dro,{execute_time:.3f}")
    print("Shell Sort")
    return random_list

print(shell_sort(random_list))
#1000 ze 0.002
#2000 ze 0.008
#3000 ze 0.017
# დასკვნა მსგავს დავალებას shell სორტირების მეთოდი გაცილებით სწრაფად ართმევს თავს 
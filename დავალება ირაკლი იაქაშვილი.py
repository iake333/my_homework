# 1. ვიქტორინა
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?”
# სავარაუდო პასუხები:
# 1. შუმერთა
# 2. სელჩუკთა
# 3. რომის
# 4. მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი.
# შეცდომის შემთხვევაში იბეჭდება: „არა! სწორი პასუხია რომის!“
# სწორი პასუხის შემთხვევაში იბეჭდება: „სწორია!

#ამოხსნაprint("რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?")
print("1.შუმერთა","2.სელჩუკთა","3.რომის","4.მონღოლთა",sep="\n")
answer=input("შეიყვანეთ რიცხვი ან შესაბამისი პასუხი: ")
if answer=="რომის":
    print("სწორია!")
elif answer=="3":
    print("სწორია!")
else:
    print("არა! სწორი პასუხია რომის!")
   
#    2. ონლაინ მაღაზია
# პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას.
# მაგ.
# 1. ლეპტოპები
# 2. პერსონალური კომპიუტერები
# 3. მობილურები
# მომხმარებელი ირჩევს ერთ-ერთს.
# პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში.
# (თითო კატეგორიაში მინიმუმ 3 პროდუქტი მაინც უნდა იყოს)
# თუ ბიუჯეტი ძალიან მცირეა, პროგრამა ბეჭდავს, რომ ამ თანხაში არ გააჩნია შემოთავაზება.

#2.ამოხსნა
print("Choose the product category from the list below:")
print("Laptop","PC","Phone",sep="\n")
choice = (input(":")).lower()

lpa = "Apple"#laptops
lpb = "HP"
lpc = "Acer"
pca="asus" #pc
pcb="lenovo"
pcc="sony"



if choice == "laptop":
    budget = int(input("Please specify your maximum budget($)"))
    if budget >= 1200:
        print(f"{lpa} is the best we can reccomend")
    elif 1200 >= budget >= 800:
        print(f"{lpb} is in the right price range for your {budget} allocated budget and we absolutely reccomend it") 
    elif 200 <= budget <= 800:
        print(f"We have some good reccomendations in {lpc} for your budget")
    else:
        print("The budget specified is too low for any reccomendations")
elif choice == "pc":
    budget = int(input("Please specify your budget($)"))
    if budget >= 800:
        print(f"{pca}High end PC is within your price range")
    elif 800 >= budget >= 400:
        print(f"Medium tier {pcb} good for gaming and casual use is reccomended for the given budget") 
    elif 200 <= budget <= 400:
        print(f"We can only reccomend {pcc} pc for the {budget} budget")
    else:
        print("The budget specified is too low for any reccomendations")
elif choice == "phone":
    budget = int(input("Please specify your budget($)"))
    if budget >= 800:
        print("we reccomend an Iphone")
    elif 800 >= budget >= 400:
        print("we reccomend samsung") 
    elif 200 <= budget <= 400:
        print(f"We can only reccomend huawei medium-tier android phones or refubrished Iphones for the {budget} budget")
    else:
        print("The budget specified is too low for any reccomendations")
else:
    print("The category specified is not in the list")

# #3. ქუესთის შედგენა (Text Based Adventure Game)
# დაწერე ერთმანეთში ჩასმული if-else კონსტრუქციების
# გამოყენებით მარტივი ტექსტზე დაფუძნებული სათავგადასავლო თამაში.
# მაგ. თავიდან პროგრამა ბეჭდავს მომხმარებლის ადგილსამყოფელს და სთავაზობს მქომედების რამდენიმე ვარიანტს. სხვადასხვა არჩევანის შემთხვევაში თამაშ სხვადასხვანაირად ვითარდება.
    
#3 ამოხსნა
print("Welcome to the Adventure Quest!")
print("You find yourself in a mysterious forest. Your goal is to reach the treasure at the end of the path.")
print("\nOptions:")
print("1. Go left")
print("2. Go right")
    

choice = input("Enter your choice (1-2): ")

if choice == '1':
        print("You went left and met a wolf!")

        print("Options:")
        print("1. Fight the wolves")
        print("2. Run away")

        wolf_choice = input("Enter your choice (1-2): ")

        if wolf_choice == '1':
            print("You fought bravely and defeated the wolf!,congradulations!!!")
        elif wolf_choice == '2':
            print("You chose to run away,  Game over!")
            
        else:
            print("Invalid choice. Please enter 1 or 2.")

elif choice == '2':
        print("You went right and found a hidden cave.")
        print("You entered the cave and found a treasure chest!")
        print("Congratulations, you found the treasure! You win!")
        

   

else:
        print("Invalid choice. Please enter a number between 1 and 2.")
        #comment
        #comment

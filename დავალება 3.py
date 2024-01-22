#2. გამრავლების ტაბულა
#ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.


#ამოხსნა
num = int(input("sheiyvanet ricxvi: "))
    
for i in range(1, num+ 1):
        for j in range(1, num + 1):
            namravli = i * j
            print(f"{i} * {j} = {namravli}", end="\t")
        print()  # axal xazze gadsvla

# 3. საბანკო ანგარიში
# შეადგინე პროგრამა რომელიც განასახიერებს საბანკო ანგარიშს. მასზე განთავსებულია თანხა 3000 ლარის ოდენობით. პროგრამა გეკითხება გაწეულ ხარჯს და აკლებს ანგარიშს მანამ, სანამ არ შეიყვან 0_ს. შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს ფუნქციონირებას. თუ ანგარიშზე არსებული თანხა ნაკლებია დანახარჯის თანხაზე, პროგრამამ უნდა დაბეჭდოს, რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება.

#ამოხსნა
account_balance = 3000

while account_balance > 0:
    
     withdrawal_amount = int(input(f"Your account balance is GEL{account_balance}. Enter the withdrawal amount (or 0 to exit): "))

     if withdrawal_amount == 0:
            break  

     if withdrawal_amount > account_balance:
            print("Insufficient funds. Please enter a valid amount.")
     else:
            # ნაშთი
            account_balance -= withdrawal_amount
            print(f"Withdrawal successful. Remaining balance: GEL{account_balance}")


print(f"Your final account balance is GEL{account_balance}. Program terminated.")

# 3 თუთიყუშის
# დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat!?”
# “User Said Hello”

#ამოხსნაw
while True:
      word=input("enter the word:")
      if word=="quit":
       break
      else:
         print(",,User Said Whaaat!?''")
         print(f",,User Said {word}''")
    
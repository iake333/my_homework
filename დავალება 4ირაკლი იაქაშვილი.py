# 1. მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე რამდენი რიცხვი, ანბანის ასო და სხვა სიმბოლოა მოცემული წინადადებაში. შედეგი დაბეჭდე. გამოიყენე for ციკლი, isalpha და isdigit ფუნქციები
#ამოხსნა
while True:
 asoebi=0
 ricxvebi=0
 simboloebi=0
 word=input("sheiyvanet inpormacia: ")
 for character in word:
     if character.isalpha():
          asoebi+=1
          
     elif character.isdigit(): 
          ricxvebi+=1
          
     else: 
         simboloebi+=1
 print(f"simboloebis raodenoba: {simboloebi}")
 print(f"asoebis raodenoba: {asoebi}")
 print(f"ricxvebis raodenoba: {ricxvebi}")

#  2. მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე შემდეგ წესებზე დაყრდნობით. შექმნილი წინადადება უნდა იწყებოდეს პირველი წინადადების პირველი სიმბოლოთი, რომელსაც ჯერ მოჰყვება მეორე წინადადების ბოლო სიმბოლო, შემდეგ კი პირველი წინადადების მეორე სიმბოლო და მეორე წინადადების ბოლოდან მეორე სიმბოლო.

 sentence_1=input("sheiyvanet tsinadadeba 1:")
 sentence_2=input("sheiyvanet tsinadadeba 2:")
 pirveli_sim=sentence_1[0]
 meores_bolo=sentence_2[-1]
 pirveli_2sim=sentence_1[1]
 meores_bolo2=sentence_2[-2]
 print(pirveli_sim,meores_bolo,pirveli_2sim,meores_bolo2)


 #3. მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე, პირველ წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორე წინადადებაში და პირიქით, მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის პირველ წინადადებაში.
# თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე:
# „Strings are balanced!“
# თუ რომელიმე პირობა დაირღვა, დაბეჭდე:
# „Strings are not balanced!“
 import re        
 sentence_1=input("sheiyvanet tsinadadeba 1:")
 sentence_2=input("sheiyvanet tsinadadeba 2:")
 symbols = re.findall("[^\w\s]", sentence_1)
 symbols2 = re.findall("[^\w\s]", sentence_2) 
 if symbols==symbols2:
  print ("Strings are balanced")
 else:print("Strings are not balanced")

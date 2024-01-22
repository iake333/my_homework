# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად:
# input: “
# Output: Tripled: ablabdabdabablabdabdabablabdabdab

text = input("shiyvanet texti: ")
def triple():
  print("output:",text * 3)
triple()
#22. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

while True:
  weight=int(input("sheiyvanet tsona: "))

  def tsona(weight):
   x=weight /3 
   return x
  tsona_mtvareze=tsona(weight)
  print("tkven itsonit mTvareze:",f"{tsona_mtvareze:.2f}",sep="  ")

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input() ფუნქციის დახმარებით 
# (სამ მონაცემს _ პირველ რიცხვს, მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“. ფუნქცია დაშლის სტრიქონს split() ფუნქციის გამოყენებით. დათვლის და დააბრუნებს შედეგს.
# გაითვალისწინე რომ რიცხვის შეყვანის მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი.
# ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)
  
def calculate_expression(user_input):
  
    try:
        
        parts = user_input.split()
        num1 = float(parts[0])
        symbol = parts[1]
        num2 = float(parts[2])

        
        if symbol == '+':
            result = num1 + num2
        elif symbol == '-':
            result = num1 - num2
        elif symbol == '*':
            result = num1 * num2
        elif symbol == '/' and num2==0:
            return "dividing by zero undefined "
        elif symbol == '/' :
            result = num1 / num2
        else:
            return "Invalid symbol. Supported symbols are +, -, *, /."

        return result
    except (ValueError, IndexError):
        return "Invalid input. Please enter a valid expression."

user_expression = input("Enter an expression (e.g., 2 * 5): ")

result_or_error = calculate_expression(user_expression)
print(result_or_error)

# არასავალდებულო:
# გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური სიმბოლოებით დაწერილ სიტყვას, დაშიფრავს მორწეს ანბანით და დააბრუნებს შედეგს.


import time


code = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }


while True:
    user_input = input("Enter text for translation: ")
    if user_input.isalnum() or (" " in user_input):
        break

for x in user_input.upper():
    if x in code.keys():
        print(code[x])
        time.sleep(0.4)

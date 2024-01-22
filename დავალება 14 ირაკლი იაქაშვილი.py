#1.	დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.

with open("article.txt", "r", encoding="utf-8") as file:
    content = file.read()
words = content.split()
word_frequencies = {}
for word in words:
    word = word.lower()
    word_frequencies[word] = word_frequencies.get(word, 0) + 1
sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

# Check if there is more than one word
if len(sorted_word_frequencies) > 1:
    second_most_frequent_word, frequency = sorted_word_frequencies[1]
    print(f"The second most frequent word is: {second_most_frequent_word} (Frequency: {frequency})")
else:
    print("There is not enough data to find the second most frequent word.")

#2.	names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.
import shutil
shutil.copy("names.csv", "names.txt")


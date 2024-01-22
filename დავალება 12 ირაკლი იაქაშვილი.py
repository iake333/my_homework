#1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.
def remove_duplicates(input_dict):
    unique_values = set()
    result_dict = {}

    for key, value in input_dict.items():
        if value not in unique_values:
            unique_values.add(value)
            result_dict[key] = value

    return result_dict


my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
result = remove_duplicates(my_dict)

print("Original Dictionary:", my_dict)
print("without Duplicate Values:", result)
#2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს
def is_dict_empty(input_dict):
    return not bool(input_dict)
empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

print("Is the dictionary empty?", is_dict_empty(empty_dict)) 
print("Is the dictionary empty?", is_dict_empty(non_empty_dict))  

# 3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს.
# ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას.
# მაგალითად გადავეცით სტრიქონი : 'racoon' უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1
def string_to_dict(input_str):
    char_count = {}
    
    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1# აუ ნიკა ეს ჩერეზ ინტერნეტით ვიწვალე და ლექციაზე იქნებ ამიხსნა კარგად ვერ გავიგე get  ის შემდეგ რაც არის იმის შინაარსი
    
    return char_count

# მაგალითის გაშვება:
input_string = 'racoon'
result_dict = string_to_dict(input_string)

print(f"Input String: '{input_string}'")
print("Result Dictionary:", result_dict)
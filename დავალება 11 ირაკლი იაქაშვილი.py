# 1. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
# def unique_list():
#     ...
#     return ...

def unique_list():
    user_input=input("sheiyvanet monacemebi:")
    list1=list(user_input)
    user_set=set(list1)
    return user_set
result=unique_list()
print(result)

# 2. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).
# def immutable_set():
#     ...
#     return ...
def immutable_set():
    user_input=input("sheiyvanet monacemebi:")
    list1=list(user_input)
    user_set=frozenset(list1)
    return user_set
result=immutable_set()
print(result)

#3. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
# def set_to_tuple():
#     ...
#     return ...
def imset_to_tuple():
    user_input=input("sheiyvanet monacemebi:")
    list1=set(user_input)
    user_input2=input("sheiyvanet monacemebi meore siistvis:")
    list2=set(user_input2)
    join=list1.union(list2)
    user_tuple=tuple(join)
    return user_tuple
result=imset_to_tuple()
print(result)
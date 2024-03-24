# დაწერე ფუნქცია რომელიც არგუმენტად მიიღებს ვებგვერდის მისამართს და გააგზავნის GET request_ს ყოველ 10 წამში
# და დაბეჭდოს ვებგვერდის სახელი და პასუხად მიღებული სტატუსის კოდი. გამოიყენე time მოდულის sleep ფუნქცია.

# Threading_ის გამოყენებით ერთდროულად გაუშვი ზემოხსენებული ფუნქცია სამი განსხვავებული ვებგვერდის შესამოწმებლად.
import time
import requests
import threading


def check(url):
    response = requests.get(url)
    time.sleep(10)

    print(f"მისამართი{url}დაბრუნებული კოდი", response.status_code)


first = threading.Thread(target=check, args=("https://www.youtube.com/",))
second = threading.Thread(target=check, args=("https://www.ambebi.ge/",))
third = threading.Thread(target=check, args=("https://www.google.com/",))
first.start()
second.start()
third.start()
start = time.time()
# check("https://www.youtube.com/")
# check("https://www.ambebi.ge/")
# check("https://www.google.com/")
first.join()
second.join()
third.join()
end = time.time()
result = end - start
print("დაყოვნების დრო:",result)

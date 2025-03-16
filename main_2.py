#1
#qnty = -9
#price = 22
#
#if qnty > 0 and price > 0:
#    print("Valid item")
#else:
#    print("There's something wrong, recheck the quantity and the price")

#2
#temp = float(input("What's the temperature? "))
#
#if temp <= 10:
#    print("It's cold!")
#elif temp <= 24:
#    print("It's normal!")
#else:
#    print("It's hot!")

#3
#log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
#
#if log['level'] == "ERROR":
#    print("There was an error, please check the job!")
#else:
#    print("No errors here!")

#4
#age = int(input("What's your age? "))
#email = str(input("What's your email address? "))
#
#if 18 > age or age > 65:
#    print("Your age must be between 18 and 65")
#elif not (email.__contains__("@") and email.count(".com")):
#    print("Your email is not valid")
#else:
#    print("You can proceed to create your password.")

#5 
#transaction = {'amount': 12000, 'hour': 17}
#
#if transaction['amount'] >= 10000 and transaction['hour'] >= 18:
#    print("Suspicious transaction. Blocked")
#else:
#    pass

#6
#phrase = "I had to run to the store, but the run was longer than I expected."
#words = phrase.split(" ")
#count = {}
#
#for word in words:
#    if word in count:
#        count[word] += 1
#    else:
#        count[word] = 1
#print(count)

#7
#numbers = [10, 20, 30, 40, 50]
#min = min(numbers)
#max = max(numbers)
#normalized = [(x - min) / (max - min) for x in numbers]
#
#print(normalized)

#8
#users = [
#    {"name": "Alice", "email": "alice@example.com"},
#    {"name": "Bob", "email": ""},
#    {"name": "Carol", "email": "carol@example.com"}
#]
#invalid_user = [users for users in users if not users["email"]]
#print(invalid_user)

#9
#numbers = range(1, 11)
#
#even = [n for n in numbers if n % 2 == 0]
#print(even)

#10
#sales = [
#    {"category": "electronics", "total": 1200},
#    {"category": "books", "total": 200},
#    {"category": "electronics", "total": 800}
#]
#total_sales = {}
#
#for i in sales:
#    category = i["category"]
#    total = i["total"]
#    if category in total_sales:
#        total_sales[category] += total
#    else:
#        total_sales[category] = total
#
#print(total_sales)

#11
#text = []
#user_input = ""
#
#while user_input.lower() != "exit":
#    user_input = input("Type an input or 'exit' to leave ")
#    if user_input.lower() != "exit":
#        text.append(user_input)
#print(text)

#12
#
#n = float(input("Type a number: "))
#
#while 10 < n <= 19:
#    n = float(input("Type a number: "))

#13
#total_pages = 15
#current_page = 1
#
#while current_page <= 15:
#    print(f"Processing page {current_page} of {total_pages}")
#    current_page += 1
#print("All pages processed.")

#15
import timeit

itens = [1, 2, 3, "stop", 4, 5]

def for_loop():
    new_itens = []
    for i in itens:
        if i == "stop":
            break
        new_itens.append(i)
    return new_itens

def while_loop():
    new_itens = []
    i = 0
    while i < len(itens):
        if itens[i] == "stop":
            break
        new_itens.append(itens[i])
        i += 1
    return new_itens

print(timeit.timeit(for_loop, number=100000))
print(timeit.timeit(while_loop, number=100000))

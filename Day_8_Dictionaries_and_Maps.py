n = int(input())
phone_book = {}
for _ in range(n):
    name, phone_number = input().split()
    phone_book[name] = phone_number
while True:    
    try:
        name = input()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
    except EOFError:
        break
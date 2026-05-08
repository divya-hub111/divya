'''i = 2
while i <= 10:
    print(i)
    i += 2'''


'''for i in range(1, 51):
    if i % 2 == 0:
        print(i)'''



'''n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)'''





'''n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")'''




'''n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)'''






'''n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed =", rev)'''




'''n = int(input("Enter number: "))
count = 0

while n > 0:
    n //= 10
    count += 1

print("Digits =", count)'''






'''n = int(input("Enter number: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")'''





'''n = int(input("Enter N: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b'''





'''for i in range(1,14):
    print("*" * i)'''






'''import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess number (1-100): "))
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        break'''




'''correct_user = "divya"
correct_pass = "1234"

attempts = 3

while attempts > 0:
    user = input("Username: ")
    password = input("Password: ")

    if user == correct_user and password == correct_pass:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Wrong credentials. Attempts left:", attempts)
else:
    print("Account locked")'''








'''numbers = [10, 45, 2, 99, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)'''





'''text = input("Enter string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowels =", count)'''







'''balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter amount: "))
        balance += amount

    elif choice == 3:
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")'''







'''n = int(input("Enter number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong")'''








'''n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")'''







for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()







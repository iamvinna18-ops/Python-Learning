# Lab Exercise 1: Number guessing game

import random
secret = random.randint(1, 100)
attempts = 0
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break

    # Lab Exercise 2: Prime number and factorial programs

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a non-negative integer: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

if num >= 0:
    print("Factorial:", factorial(num))
else:
    print("Factorial is not defined for negative numbers.")


# Lab Exercise 3: Fibonacci series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
terms = int(input("Enter number of terms: "))
if terms <= 0:
    print("Enter a positive number.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()


# Mini Project: OTP Generator

import random
otp = random.randint(100000, 999999)
print("Your OTP is:", otp)
print("Note: In a real application, an OTP should be sent securely rather than displayed.")


import random
print("Привет, как тебя зовут?")
name = input()
print(f"Что ж, {name}, я загадываю число от 1 до 20.")


number = random.randint(1, 20)
trying = 0
for i in range(6):
    print("Попробуй угадать.")
    guess = int(input())
    trying += 1
    if guess < number:
        print("Твое число слишком маленькое.")

    if guess > number:
        print("Твое число слишком большое.") 

    if guess == number:
        break  
    
if guess == number:
    print(f"Отлично, {name}! Ты справился за {trying} попытки")

if guess != number:
    print(f"Увы. Я загадал число {number}.")
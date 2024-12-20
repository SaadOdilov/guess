import random 


n = random.randit(0, 10)
guess = int(input("guess a anumber between 0 and 10:"))

if n == guess:
    print("Toptingiz")
else:
    print("Topa olmadingiz")

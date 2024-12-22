import random 


n = random.randit(0, 10)
guess = int(input("guess a anumber between 0 and 10:"))


while True:   
   if n == guess:
        print("Toptingiz !!!")
        break
   guesses += 1
    if guess >= 3:
        print("Yutqazdingiz")
        break

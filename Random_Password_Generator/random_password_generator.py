import random
length=int(input("Enter Password length: "))
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password=""
for i in range(length):
    password +=random.choice(characters)
print ("Generated password:",password)
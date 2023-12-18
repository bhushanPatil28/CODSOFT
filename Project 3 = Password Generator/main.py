import string 
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

userInput = input("Enter the length of password: ")

while True:
    try:
        length_of_ch = int(userInput)
    except ValueError:
        print("Entered value is not a number, try again!")
        userInput = input("Enter the length of password: ")
        continue
    break

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(length_of_ch * (30/100))
part2 = round(length_of_ch * (20/100))
part3 = length_of_ch - (part1 + part2)

result = []

for i in range(part1):
    result.append(s1[i])
    result.append(s2[i])

for i in range(part2):
    result.append(s3[i])

for i in range(part3):
    result.append(s4[i])

random.shuffle(result)

password = "".join(result)
print(f"Password: {password}")

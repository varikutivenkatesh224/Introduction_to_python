a = float(input())
b = float(input())
operator = input("operator (+, -, *, //, / ):  ")

if operator == "+":
    result = a+b
elif operator == "-":
    result = a-b
elif operator == "//":
    result = a//b
elif operator == "*":
    result = a*b
elif operator == "/":
    if b == 0:
           print("error")
    else:
           print(a/b)
else:
    print("Unknown operator")





#grades
grade = float(input(" grade /20: "))
if grade <0 or grade >20:
     print("invalide grade")
elif grade >=16:
    print("very good")
elif grade >=14:
    print("good")
elif grade >=12:
    print("failry good")
elif grade >=10:
    print("pass")
else:
    print("fail")



import random
secret_number = random.randint(1, 100)
guess = int(input("guess the number:  "))

while guess != secret_number:
    if guess < secret_number:
        print("too low")
    else:
        print("too high")
    guess = int(input("guess the number:  "))
print(" bravo! It was ", secret_number)




given_scores= [12, 17, 9, 15, 14]
best =0
position =0
for i in enumerate(given_scores, start=1):
    if i[1] > best:
        best = i[1]
        position = i[0]
print(f"best: {best} at position {position}")




answers =["b", "d", "d", "c"]
correct_answers = ["b", "c", "d", "c"]
score =0
for a, c in zip(answers, correct_answers):
    if a == c:
        score +=1
print(f"score: {score}/{len(correct_answers)}")

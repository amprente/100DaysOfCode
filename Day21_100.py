print("~ Math Game! ~")
print()
number = int(input("Name your multiples: "))
score = 0
print()

for i in range(1, 11):
    answer = int(input(str(i) + " X " + str(number) + " = "))
    if answer == i * number:
        print("Great work!")
        print()
        score += 1
    else:
        print("Nope. The answer was " + str(i * number) + ".")
        print()

print("------------")
print("You scored " + str(score) + " out of 10. 😊")

if score == 10:
    print("Congratulations! 🎉 You got all the answers correct! 🎉🎓")
    

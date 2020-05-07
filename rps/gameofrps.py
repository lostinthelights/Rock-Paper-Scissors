import random

win_reward = 100
draw_reward = 50
score = 0

name = input("Enter your name:")
print("Hello,", name)

ratings = open('rating.txt', 'r', encoding='utf-8')
for lines in ratings:
    line = lines.split()
    if str(line[0]) == name:
        score = int(line[1])
        break
    else:
        score = 0
        # ratings.write(f"\n{name} {score}")

li = input().split(",")

if li == "":
    li == "rock,paper,scissors".split(",")

print("Okay, let's start")


def update_score(temp_score):
    for rates in ratings:
        if rates[0] == name:
            rates[1] = str(int(rates[1]) + temp_score)


while 1:
    n = int((len(li) - 1) / 2)
    option1 = input()
    winners = []
    losers = []
    draw = []

    if option1 in li:
        draw.append(option1)
        if li.index(option1) < n:
            for i in range(n):
                winners.append(li[li.index(option1) + i + 1])
            for item in li:
                if item not in draw and item not in winners:
                    losers.append(item)
        elif li.index(option1) > n:
            for i in range(n):
                losers.append(li[li.index(option1) - i - 1])
            for item in li:
                if item not in draw and item not in losers:
                    winners.append(item)
        elif li.index(option1) == n:
            for i in range(n):
                winners.append(li[li.index(option1) + i + 1])
                losers.append(li[li.index(option1) - i - 1])

    if option1 == "!exit":
        print("Bye!")
        break
    elif option1 == "!rating":
        print("Your rating:", score)
    else:
        option2 = random.choice(li)
        if option2 in winners:
            print(f"Sorry, but computer chose {option2}")
        elif option2 in draw:
            print(f"There is a draw ({option2})")
            score += draw_reward
            update_score(score)
        elif option2 in losers:
            print(f"Well done. Computer chose {option2} and failed")
            score += win_reward
            update_score(score)
        elif option2 not in li:
            print("Invalid input")

ratings.close()

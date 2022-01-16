print("Welcome to the Love Calculator!")
name1 = input("What is your full name? \n")
name2 = input("What is your love interest's full name? \n")

combined_names = name1 + name2
lower_name = combined_names.lower()
print("The BuzzFeed article that this is based on states that love compatability can be calculated through counting how many times the letters in 'true love' appear in both your names, concatenated.")

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
true = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score <= 10 or love_score > 90:
    print(f"Your score is {love_score}, it's destiny. Destined to fail or succeed - we're not sure. Check with a licensed professional.")
elif love_score >= 50 and love_score < 90:
    print(f"Your score is {love_score}, you are pretty compatible.")
else:
    print(f"Your score is {love_score}. Average.")

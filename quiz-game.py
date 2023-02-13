print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()

print("Lets play!")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
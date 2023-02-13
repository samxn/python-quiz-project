print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Lets play!")

answer = input("The logo for luxury car maker Porsche features which animal? ")
if answer.lower() == "horse":
    print('Correct!')
else:
    print('Incorrect')

answer = input("Which element is said to keep bones strong? ")
if answer.lower() == "calcium":
    print('Correct!')
else:
    print('Incorrect')

answer = input("What is the first name of the daughter in The Addams Family? ")
if answer.lower() == "wednesday":
    print('Correct!')
else:
    print('Incorrect')

answer = input("What does “www” stand for in a website browser? ")
if answer.lower() == "world wide web":
    print('Correct!')
else:
    print('Incorrect')
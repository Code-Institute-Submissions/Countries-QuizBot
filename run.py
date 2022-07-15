import time

#Introduces the game and prompts user to create a username.
print("Hi! I'm QuizBot. Create a username to start.")
print("---------------------------------")
username = input("Username: ")
print("---------------------------------")
print(f"Hey, {username}! Are you ready to test your country knowledge skills?")
print("---------------------------------")
print("Note: answers should be 'a', 'b', or 'c' in lowercase. 'True/False' are case\n sensitive.")

#Checks to see whether user wants to start quiz or not
start_quiz = input("Type 'y' or 'n' to start: ")

if start_quiz == "y":
    print("Brilliant! Get your quiz hat on!")
    time.sleep(1)
    print("Hang on a sec whilst I think of what questions to ask you...")
    time.sleep(1)
    print("Ok, ready? No pressure but I thought it'd be fun to time you as well. Good luck!")
    print("---------------------------------")
    time.sleep(1)
else:
    print("Oh... I guess this is goodbye then :(")
    raise SystemExit()

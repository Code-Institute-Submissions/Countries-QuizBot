# Quiz Bot
* The idea for this project is a simple general knowledge quiz of countries to test a user's knowledge using a multiple choice format and one 'True/False'. 
* Although anybody could access and run this quiz themselves, the suitability and content is targeted towards the expectations of adults, or people who have a strong knowledge/interest in geography.
* Quiz Bot is intended to come across as having a chatty, informal tone as if you're talking to a friend. This is give a sensation of having fun and being relaxed, rather than the user feel as though they're interacting with a computer.

# Mindmap/Ideas
![](vscode-remote://tkingston-countriesquiz-4hkbdy95x7b.ws-eu54.gitpod.io/workspace/Countries-QuizBot/README_Images/Basic_mindmap.png)

* Seen from the mind map is a simple flowchart of the order of how the code is intended to run:
1. First, introduce the game, and get user interaction as soon as possible by getting them to create and input their username.

2. Once the username has been submitted, prompt with an option whether the quiz should start or not, and have a corresponding 'if' statement based upon the input. If no, the code breaks and the user is directed back to the terminal. If yes, the code proceeds.

3. The code proceeds and presents one question at a time with their relative multiple choice options for the user to read. The idea is to define a function and call it in a 'for loop' to loop between questions 0-9.

4. By this time, a timer has started in the background which the user was notified by a print statement prior to starting. For every question they get correct, the variable 'score' is increased by 1, for a maximum of 10 points. If a question is wrong, the score is not increased.

5. Once the last question has been answered, the timer stops, and a print statement used to show the user how many points they scored, and in what time. This is followed by another print statment telling them which 'category' they're in based on their score.

6. Two options now are given to the user: replay, or quit. By using an 'If Else' statement to determine the outcome based on user input, the quiz, score and time will either restart by calling the 'run_quiz' variable agian, or it will 'raise SystemExit()', kicking the user back to main terminal with a goodbye message.

# Features

## import 

* The 'import' module and importing 'time' allowed to utilise the features in order to create the stop/start timer used to record the time it had taken from the quiz starting to the quiz ending.

* Additionally, between some print statements, there are 'time.sleep()' tags. This determines the time it takes between each print statement to be shown, e.g. display the new message 2 seconds after the previous one. This was done to add some readability for the usern so they have time to read and interact with the code if necessary.

## Print and Input Statements 

* Print statements allow for visual cues or information to be displayed to the user as they play.
* Input statements are used throughout to indicate whether the user wants to start the quiz by pressing 'y' or 'n', to record their answer for questions, and recieve a reply on if they want to replay or quit once the quiz is over. 

## Def, Class, For, and If 

* This code uses a class which is defined as 'Quiz'. This is utilised by calling the class later on when it is manipulated with the 'questions_asked' variable to define which number the question is in the queue, and it's corresponding answer.

* 'Def' is used throughout to define a function (e.g. 'run_quiz') which can be used within the code by calling the function name, with its conditions attached (e.g. the conditions for the quiz to start and loop through.)

* A 'for loop' is used to iterate between the 'questions' variable, in order.

* Multiple 'If/Else' statments tell the code what to process next as a result of the parameters given. In this instace, if the user presses the 'y' key to start the quiz, the quiz starts; if the user gets a question right, their score goes up. If the score is above a set number, a dynamic print statement is displayed (here an elif and else statement are also used to define other parameters, should the 'if' statement conditions not be met)

# Ideas for additional features

* In the mind map there is a section which suggests a 'double or nothing' option. In theory, once all 10 questions have been asked, they would be presented by a gesture - "Do you wish to answer one final question in the hopes to double your score and risk it all, or play it safe and finish with the score you have?" 
    * Implementing this would add an element of risk and competiton becuase if playing against other people and comparing scores, this feature could change the game.
    * Getting this to work would require the use of calling the 'score' variable, and using the multiplication tool either using (score * 2 , or score * 0), triggered by 'if answer == question.answer:' which had be altered to apply to the new question.

* Instead of having the interface display in the terminal, expand the code to work in a GUI (using TKinter). This will make it more user friendly and can be fully customised to any theme/ideology the developer wants. 
* Expand the depth of the game/quiz by having a library of different questions and let the user decide which categories they would like to be quizzed on (for example: only questions about the UK, or world leaders, or historic events.)
* Restriciting input by only allowing ("a, b, or c & t/f"), resulting in an error if another character is input.

# Program Testing

* To confirm all features work as intended, all the possible outcomes in the terminal were testing. These being: 
    * User typing 'y' to start the quiz and the questions appearing in order.
    * User typing 'n' to not start the quiz and being exited back to main terminal with exit statment printed. 
    * User getting all questions correct and '10/10' for score, displaying, likewise with any score they get e.g. 4/10
    * The timer being accurate from when the quiz starts and the final question being answered.
    * User replaying the quiz by typing 'r' when prompted and all questions being redeployed with the timer resetting. 
    * User ending the quiz after running it once and second exit statement being printed as they're placed back into the main terminal.

# User Testing

* After a couple runs of user testing without the developer's input (me), a couple key points of feedback were made: 
    * A misinterpretation of how this sentence (see image below) was interpreted. The test user read it as 'test your country knowledge' as if the test is knowledge about their country, and not a test about their knowledge on countries as general. This has been changed to be more specific and clear - "Are you ready to test your knowledge of countries?"
    ![](vscode-remote://tkingston-countriesquiz-4hkbdy95x7b.ws-eu54.gitpod.io/workspace/Countries-QuizBot/README_Images/misinterpretation.png)
    * Additionally, question number 7 is a true/false question. Originally the code was written to accept 'true' as an answer, however the user naturally typed 't', assuming it followed suit of all the other questions being 'a, b, or c'. This has been changed to reflect the feedback in both the code which checks the answer against user's input, and in the 'notes' section which is displayed before the quiz starts.
    ![](vscode-remote://tkingston-countriesquiz-4hkbdy95x7b.ws-eu54.gitpod.io/workspace/Countries-QuizBot/README_Images/old_answer_format.png)

    # Bugs

    * Implementing the (dot)lower attribute to the user's input for answers, the terminal kept returning 'the object has no attribute.' Having worked in the previous draft test IDE, the attribute was removed and a contingency of advising the user in the 'notes' section, that all answers are case sensitive and lowercase.
    ![](vscode-remote://tkingston-countriesquiz-4hkbdy95x7b.ws-eu54.gitpod.io/workspace/Countries-QuizBot/README_Images/lower_attribute_bug.png)

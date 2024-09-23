#Introduction to the quiz
print("Welcome to the ultimate quiz challenge!\n")
print("Get ready to test your knowledge and show off your skills!\n")
print("You'll be asked a series of questions, and you'll have to answer them correctly to win!\n")
#explaining the user how the score is calculated
print("You will  earn 4 point for each correct answer.")
print("You will lose 1 point for each incorrect answer.")
print("Let's start the quiz\n")
questions=[
    {
        "question": "What is the capital of Australia?",
        "options":['1.  Sydney', '2. Melbourne', '3. Canberra', '4. Perth'],
        "answer":"3"

    },
    {
      "question": "Who wrote the play 'Romeo and Juliet'?",
      "options":['1.  Charles Dickens', '2. William Shakespeare', '3. Mark Twain', '4. Leo Tolstoy'],
      "answer":"2"  
    },
    {
      "question": "In which year did the Titanic sink?",
      "options":['1. 1927', '2. 1943', '3. 1897', '4. 1912'],
      "answer":"4"  
    },
    {
      "question": "Which country is known as the Land of the Rising Sun?",
      "options":['1. China', '2. South Korea', '3. Japan', '4. Thailand'],
      "answer":"3"  
    },
    {
      "question": "What is the currency of Turkey?",
      "options":['1. Lira', '2. Ruble', '3. Shekel', '4. Real'],
      "answer":"1"  
    }

]

def  quiz(questions): #defining function to run the quiz
    correct = 0
    wrong = 0
    #printing all the questions
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input('Enter the suitable option here: ').strip().upper()
         #Accepting user input 
        if  answer == question["answer"]: #Checking if the answer is correct or wrong
            print()
            print('Well Done...Your Answer is Correct\n')
            print()
            correct += 1
        else:
            print()
            print('Sorry...Your Answer is Wrong\n')
            print()
            wrong += 1
    print(f'You got {correct} out of {len(questions)} questions correct\n') #Showing how many questions the user got correct
    print(f'You got {wrong} out of {len(questions)} questions wrong\n') #Showing how many questions the user got wrong
    print('You have scored ',(correct*4)-wrong) #Showing the user's score
    print()
    print()
    print('DISCLAIMER: This quiz is for entertainment purposes only')
    print('            The verdict given by this quiz is not to be taken seriously\n')
    if correct > 3:  #If the user's score is above 3, they are a Braniac
        print('Final Verdict: You are a Genius\n')
    else:   #If the user's score is equal and below 3, they need to improve
        print('Final Verdict: You need to work harder\n')

def run(): #Defining a funtion to check if the user is eligible and ready  to play the quiz
    name = input("What is your name? ") #Accepting user's name
    age = int(input("How old are you? ")) #Accepting  user's age
    #To check if the  user is eligible to play the quiz
    if age > 10:
        print("You are eligible to play the quiz\n")
        ready = input("Are you ready to start the quiz? (yes/no): ")
        if ready.lower() == 'yes':
            print()
            quiz(questions)
        else:
            print('Quiz cancelled')
        #thanking the user for playing the quiz
        print('Thank you for playing the quiz')
        print('We hope you enjoyed it')
    else:
        print('Sorry, You are not eligible to play the quiz') 

if __name__ == '__main__':
    run()


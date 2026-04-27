user = input("Enter your name: ")
intro = (f"Welcome {user}! there are five questions, each has two attempts only and carries 2 marks.")
print(f"{intro}")
print("Goodluck!")
Questions = ["What is 5 + 3?","What is the capital of France?","Which continent is the coldest?","What is (5 X 3)^2?","What part of the body never stops growing?"]
answers = [(f"{5 + 3}"),(f"{"Paris"}"),(f"{"Antarctica"}"),(f"{(5*3)**2}"),(f"{"Ears"}")]
correct_answers = []
attempt = 0
x = Questions.index(Questions[-1]) # the index for the last question

for i in range(len(Questions)):
    print(f"Question {i+1}: {Questions[i]}")
    answer = input("Enter your answer: ")

    if answer.capitalize() != answers[i]:
        print("Wrong answer! one attempt left")
        attempt = 1
        
        while attempt == 1:
            max_attempt = 2
            answer = input("Enter your answer: ")
            attempt +=1
            
            if answer.capitalize() != answers[i] and attempt == max_attempt and i == x:
                break
            elif answer.capitalize() != answers[i] and attempt == max_attempt:
                print("Wrong! try the next question")
                break
            elif answer.capitalize() == answers[i]:
                print("Correct")
                correct_answers.append(answer)
                break

    elif answer.capitalize() == answers[i]:
        print("Correct")
        correct_answers.append(answer)
    


print("****************** FINAL SCORE ***********************")
print("")
print(f"{user}, your final score is: {2*(len(correct_answers))}/{2*(len(Questions))}")
print("")
print("******************************************************")
import json

allq = {}
correctq = {}
wrongq = {}
previous_attempts = {}

with open("memory.json" , "r") as f:
    last_attempt_raw = json.load(f)
with open("correct.json", "r") as f:
    retry_correct_raw = json.load(f)
with open("wrong.json", "r") as f:
    retry_incorrect_raw = json.load(f)

last_attempt_correct = list(last_attempt_raw.values()).count(True)
improvement_count1 = list(retry_incorrect_raw.values()).count(1)
improvement_count2 = list(retry_incorrect_raw.values()).count(2)
improvement_count3 = list(retry_incorrect_raw.values()).count(3)
improvement_count = (improvement_count1 + improvement_count2 + improvement_count3)/2
retry_correct_count = last_attempt_correct + improvement_count

if improvement_count == 0:
    print(f"You score 20 / 20 last time! Let's see if you can do it again!")
else:
    print(f"""In your last attempt, you scored {last_attempt_correct} / 20. 
Then you improved your score by {improvement_count}, making your final score {retry_correct_count} / 20.
Let's see how you do this time!""")

correct = 0
total = 0
questions = {"What color is grass?": "Green",
             "What is the derivative of x³ (x^3)": "3x^2",
             "How many days are in a year?": "365",
             "What country has the largest population in the world?": "India",
             "What is the largest desert in the world": "Antarctica",
             "What is the name for the second year of high school?": "Sophomore",
             "Who should you vote for treasurer in the upcoming Stu-Gov election?": "Jordan",
             "Fill in the blank: Roses are red, violets are ____": "blue",
             "What is kehillah replacing AP classes with? (___ classes)": "KAT",
             "What is the chemical compound for water?": "H2O",
             "What video game company created Mario?": "Nintendo",
             "Which US president is on the $1 bill?": "George Washington",
             "How many states are in the United States?": "50",
             "How many days are in 1 week?": "7",
             "What fruit is also the name of a large tech company?": "Apple",
             "What is the freezing point of water (__°C)": "0",
             "What line seperates the northern and southern hemispheres on Earth?": "Equator",
             "What is 7²": "49",
             "What coding language is this program written in?": "Python",
             "What are the 2 components needed for a simple sentence?": "Subject and Predicate"
             }

for i, q in enumerate(questions, start=1):
    fail = 0
    print(q)
    answer = input("Answer: ")
    if answer == questions[q]:
        print("Correct!")
        correct += 1
        correctq[f"q{i}"] = 1
        allq[f"q{i}"] = True
    else:
        print("Incorrect :/")
        fail += 1
        allq[f"q{i}"] = False
    total += 1
ogscore = f"{correct}/{total}"
print(f"""You answered {correct}/{total} questions correctly. Let's review the ones you missed.
      You can get half your points back if you get them right this time!""")

for q in allq:
    if allq[q] == False:
        question_index = int(q[1:]) - 1
        question_text = list(questions.keys())[question_index]

        for i in range(3):
            print(question_text)
            answer = input("Answer: ")
            if answer == questions[question_text]:
                print("Correct!")
                correct += 0.5
                wrongq[q] = i + 1
                break
            else:
                if i == 2:
                    print("Incorrect. No more tries left.")
                    print(f"The correct answer was: {questions[question_text]}")
                    wrongq[q] = False
                else:
                    print(f"Incorrect. You have {2 - i} tries left.")

finalscore = f"{correct}/{total}"

previous_attempts["attempt"] = f"{correct} / {total}: {correct/total}%"

# attempt_number = len(previous_attempts) + 1  # Determine the next attempt number
# previous_attempts[f"attempt_{attempt_number}"] = f"{correct} / {total}: {correct/total:.2%}"

with open("memory.json" , "w") as f:
    json.dump(allq, f, indent=True)

with open("correct.json", "w") as f:
    json.dump(correctq, f, indent=True)

with open("wrong.json", "w") as f:
    json.dump(wrongq, f, indent=True)

with open("all-memory.json", "w") as f:
    json.dump(previous_attempts, f, indent=True)

print (f"Original Score: {ogscore}")
print (f"Final Score: {finalscore}")
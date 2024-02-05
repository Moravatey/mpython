# file name is Quizz_app.py

#get user respond :: Input function
name = input("What is your name? ")
print("Hello", name)

#Compare respond and answer
#total_point = 0
#question = input("2 + 2? ") 

#if question == "4":
    #print('Correct')
#else:
    #print('Incorrect')

total_point = 0
question = input("if 2 cookies are eaten from a dozen of cookies, how much cookies are left? ")
if question.lower() == "10":
    total_point = total_point + 1
    print('CORRECT')
else:
    print('INCORRECT')

question = input("Am i pretty? ")
if question.lower() == "yes":
    total_point = total_point + 1
    print('CORRECT')
else:
    print('INCORRECT')

question = input("Is mars our second earth? ")
if question.lower() == "no":
    total_point = total_point + 1
    print('CORRECT')
else:
    print('INCORRECT')

question = input("Are you acoustic? ")
if question.lower() == "yes":
    total_point = total_point + 1
    print('CORRECT')
else:
    print('INCORRECT')

question = input("How old is old enough to be old enough? ")
if question.lower() == "99.5":
    total_point = total_point + 1
    print('CORRECT')
else:
    print('INCORRECT')

print(f"Your total point is: {int(total_point/5*100)}%")
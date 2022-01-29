#-----------------------------------#
def new_game():
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print('-----------------------------')
    print(key)
    for i in options[question_num - 2]:
      print(i)
    guess = input('Enter (A, B, C, D): ')
    guess = guess.upper()
    guesses.append(guess)

    correct_guesses += check_answer(questions.get(key),guess)#(answer,guess)
    question_num += 1
  display_score(correct_guesses,guesses) 

#------------------------------------#
def check_answer(answer,guess):
  if answer == guess:
    print('CORRECT!')
    return 1
  else:
    print('WroNg!')
    return 0

#------------------------------------#
def display_score(correct_guesses,guesses):
  print('-----------------------------------')
  print('RESULTS')
  print('------------------------------------')

  print('Answers: ',end=" ")
  for i in questions:
    print(questions.get(i), end=" ")
  print()

  print('Guesses: ',end=" ")
  for i in guesses:
    print(i, end=" ")
  print()

  score = int((correct_guesses/len(questions))*100)
  print("your score is "+ str(score)+"%")

#------------------------------------#
def play_again():
  responce = input('Do you want to play again?(yes/no): ')
  responce = responce.upper()

  if responce == "YES":
    return True
  else:
    return False

#-------------------------------------#
#dictionary
questions = {
  "who created python?":"A",
  "what year was python created?":"B",
  "python is tributed to which comedy group?":"C",
  "is the earth round?":"A"
}

#2D lists
options = [["A, Guido ven Rossam","B, Elon musk","C, Bill gates","D, Mark zuckerburg"],
["A, 1089","B, Smosh","C, Monty python","D, SNL"],
["A, True","B, False","C, sometimes","D, What's the earth? are you round?"]]

new_game()

while play_again():
  new_game()
print("Byeeeeeee!!!!")
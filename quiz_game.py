#-------------------
def new_game():

  guesses = []
  correct_guesses = 0
  num_question = 1

  for key in questions:
      print("--------------------------------------")
      print(key)
      for i in options[num_question-1]:
       print(i)
      guess = input("Enter (A)or(B)or(C)or(D): ")
      guess = guess.upper()
      guesses.append(guess)
      correct_guesses +=check_answer(questions.get(key),guess)
      num_question += 1
  display_score(correct_guesses,guesses)
#-------------------
def check_answer(answer,guess):
  if answer == guess:
    print("CORRECT!✅")
    return 1
  else:
    print("WRONG!❌")
    return 0

#-------------------
def display_score(correct_guesses,guesses):
  print("--------------------------------------")
  print("RESULTS")
  print("--------------------------------------")
  print("ANSWERS :",end=" ")
  for i in questions:
    print(questions.get(i),end=" ")
  print()
  print("GUESSES :",end=" ")
  for i in guesses:
    print(i,end=" ")
  print()
  score = (correct_guesses/len(questions))*100
  print("YOUR SCORE IS: " + str(int(score))+"%")

#-------------------
def play_again():
  again = input("PLAY AGAIN? ENTER(yes/no): ")
  again = again.upper()
  if again == "YES":
    return True
  else:
    return False
#-------------------

#your Questions should be like that
questions = {
    "Which Moroccan city hosts the annual Gnaoua World Music Festival?": "D",
    "What is the highest mountain in Morocco?": "B",
    "Which Moroccan dish is made of steamed semolina grains?": "A",
    "In which year did Morocco gain independence from France?": "D",
    "Which Moroccan city is known as the Blue Pearl?": "D",
    "What is the traditional Moroccan dish made of slow-cooked meat and vegetables in a clay pot?": "A",
    "Which Moroccan football club has won the most CAF Champions League titles?": "B",
    "Which ancient Moroccan city was once the capital of the Almoravid and Almohad empires?": "C",
     "What is the name of the Moroccan traditional music style that originated from African slaves?": "A",
    "Which Moroccan mountain range extends across the country?": "D",
    "What is the name of the traditional Moroccan soup often eaten during Ramadan?": "B",
    "Which Moroccan city is famous for its annual international film festival?": "D",
    "Which body of water borders Morocco to the west?": "A"
}
#and options too
options = [
    ["A. Ouarzazate ", "B. Marrakech", "C. Fes", "D. Essaouira "],
    ["A. Rif Mountains", "B. M'Toubkal ", "C. Jebel Ayachi", "D. M'Goun"],
    ["A. Couscous", "B. Mechoui", "C. Harira", "D. Bissara"],
    ["A. 1923", "B. 1945", "C. 1950", "D. 1956"],
    ["A. Tangier", "B. Meknes", "C. Agadir", "D. Chefchaouen"],
    ["A. Tagine", "B. Mechoui", "C. Bissara", "D. Couscous"],
    ["A. Raja Casablanca", "B. Wydad AC", "C. FUS Rabat", "D. AS FAR"],
    ["A. Ouarzazate", "B. Tetouan", "C. Marrakech", "D. Rabat"],
    ["A. Gnaoua", "B. Chaabi", "C. Malhun", "D. Amazigh music"],
    ["A. Rif", "B. Middle Atlas", "C. Anti-Atlas", "D. High Atlas"],
    ["A. Tajine", "B. Harira", "C. Mechoui", "D. Bissara"],
    ["A. Casablanca", "B. Tangier", "C. Agadir", "D. Marrakech"],
    ["A. Atlantic Ocean", "B. Mediterranean Sea", "C. Red Sea", "D. Gulf of Guinea"]
]
new_game() 
#for start the game

while play_again():
  #if play_again true the game will start again
   new_game()

print("BYE!👋🏽")
import random

print("hello! Im here to help you with memorizing some answers to questions!")
input("ready to start?")

questions = ["j'", "Nous","tu","Vous","Il/elle/on","Ils/Elles","voyager",'acheter','ranger','trouver','choisir','finir','vomir','reussir','entendre','attendre','fondre','perdre','tu _ _ les devoirs', "j'_ _ un ordinateur",'nous _ _ la chambre','on _ _ le chocolat','vous _ _ le chanson','ils _ _ la maison','chateaux','Moyen Age(Fort) _','Renaissance (rebirth) _','_ valley- The _ of france','le val deloire - le _ de france']

for i in questions:
    quizQuestion = random.choice(questions)
    print(quizQuestion)
    isTheAnsCorrect = input("What is the answer: ")
    questions.remove(quizQuestion)
    len(questions)
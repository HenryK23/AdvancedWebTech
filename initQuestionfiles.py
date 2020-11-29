biologyQuestions = ['What is the short form of deoxyribonucliec acid', 'what type of animal becomes pregnant','what type of animal produces hard shelled eggs']
norwegianQuestions =  ['How do you say "Thanks you very much"', 'How do you say "Hello"', 'How do you say "Who am I?"']
computingQuestions = ['What does HCI stand for', 'What part of the computer holds long term memory', 'What does the u in CPU stand for']

biologyAnswers = ['DNA', 'Mammals', 'birds']
norwegianAnswers = ['Tusen takk', 'Hallo', 'hvem er jeg']
computingAnswers = ['Human computer interaction', 'Hard drive', 'unit']


def initBiology():
    fo=open("Biology.txt", "w")
    for question in biologyQuestions:
        fo.write(question)
        fo.write("\n")
    fo.close()
    fa=open("BiologyAnswers.txt","w")
    for answer in biologyAnswers:
        fa.write(answer)
        fa.write("\n")
    fa.close()

def initNorwegian():
    fo=open("Norwegian.txt","w")
    for question in norwegianQuestions:
        fo.write(question)
        fo.write("\n")
    fo.close()
    fa=open("NorwegianAnswers.txt","w")
    for answer in norwegianAnswers:
        fa.write(answer)
        fa.write("\n")
    fa.close()

def initComputing():
    fo=open("Computing.txt","w")
    for question in computingQuestions:
        fo.write(question)
        fo.write("\n")
    fo.close()
    fa=open("ComputingAnswers.txt","w")
    for answer in computingAnswers:
        fa.write(answer)
        fa.write("\n")
    fa.close()


def optionList():
    fo=open("optionList","w")
    fo.write("Biology")
    fo.write("\n")
    fo.write("Norwegian")
    fo.write("\n")
    fo.write("Computing")
    fo.write("\n")
    fo.close()


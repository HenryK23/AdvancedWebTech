from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from initQuestionfiles import initBiology, initComputing, initNorwegian, optionList
app = Flask(__name__)
#secret key is required for the use of sessions. 
app.secret_key = 'A0Zr98j /3 yX R~XHH!jmN]LWX / ,? RT'

#initialising the pre-made flashcard sets and the option list, this pulls from initQuestionfiles.py 
initBiology()
initComputing()
initNorwegian()
optionList()

#This will make sure that anyone going to the root page will be redirected to the home page. 
@app.route('/')
def base():
    return redirect(url_for("home"))

#to inspect the masterpage without any content 
@app.route('/flashycards/')
def root():
    return render_template('MasterPage.html')

#Home page 
@app.route('/flashycards/home/')
def home():
    return render_template('homePage.html')

#redundant code, decided to remove the about page. 
@app.route('/flashycards/home/about/<text>')
def about(text):
    return render_template('aboutPage.html',text=text)

#Create set page, will ask for the set name and the number of questions so they can be used in the questions page. 
@app.route('/flashycards/home/createset/', methods=['GET', 'POST'])
def createset():
    if request.method == 'POST':
        session['setName'] = request.form['setName']
        strQuestionCount="1"
        strQuestionCount = request.form['questionCount']
        intQuestionCount = int(strQuestionCount)
        return redirect(url_for("questions", intQuestionCount=intQuestionCount,setName=session['setName']))
    else:
        return render_template('createSet.html')

# Open set page, this will use the option list file to take the option selected in the dropdown and use that to open a flashcard set. 
@app.route('/flashycards/home/openset/', methods=['GET','POST'])
def openset():
    if request.method == 'POST':
        session['option'] = request.form['option']
        
        for option in session['optionList']:
            option = option.replace("\n", "")#blackslash n would get added to the string although it was only being used to create a new line, so it needs removed before the if statement
            if session['option'] == option:
                fo=open(option+".txt","r") # all the file naming schemes are the same so this allows for the option to be used to determine the file to open
                session['questionlist']=fo.readlines()
                fo.close()

                fr=open(option+"Answers.txt") # again all the file naming conventions are the same so adding Answers to the option selected will always load the answers file. 
                session['answerlist']=fr.readlines()
                fr.close()
                #return(jsonify(session['answerList'], session['questionlist'])) # this was to test the returned values 
        return redirect(url_for("flashcard"))
    else:

        fo=open("optionList","r")
        session['optionList']=fo.readlines()
        fo.close()
        return render_template('openSet.html', optionList=session['optionList'])


#this is the questions page where the user sets the questions and answers for their flashcard set. 
@app.route('/flashycards/home/createset/questions/<int:intQuestionCount><setName>', methods=['GET', 'POST'])
def questions(intQuestionCount,setName):

    if request.method == 'POST':
        session['questionlist'] = request.form.getlist('question[]')
        session['answerlist'] = request.form.getlist('answer[]')
        return redirect(url_for("flashcard"))
    else:
        return render_template('createQuestion.html', questionCount=intQuestionCount,Name=session['setName'])

#this is the flashcard page, it displays the list of questions and once the check answer button is pressed will return check answer page
@app.route('/flashycards/home/openset/flashcard/', methods=['GET', 'POST'])
def flashcard():
    if request.method == 'POST':
        session['formAnswers'] = request.form.getlist("cardAnswer")
        return redirect(url_for("checkAnswer"))
    else:
        return render_template('flashCard.html', questionlist=session['questionlist'])


#check answer page will calculate the grade and show it on screen
@app.route('/flashycards/home/openset/flashcard/checkanswer/', methods=['GET','POST'])
def checkAnswer():
    grade=0
    gradePercentage = 0
    for formAnswer in session['formAnswers']:
        for actualAnswer in session['answerlist']:
            actualAnswer = actualAnswer.replace("\n", "")
            if formAnswer.casefold() == actualAnswer.casefold():
                grade+=1
        gradePercentage = (grade/len(session['formAnswers']))*100

        if gradePercentage >= 75:
            letterGrade = "A"
            gradeMessage = "Congradulations! you achieved a mark over 75%, this shows you have great knowledge of the flashcard set. But don't stop there, practising everyday will help you remember the answers."
        elif gradePercentage >= 60 and gradePercentage < 75:
            letterGrade = "B"
            gradeMessage = "well done! you achieved a mark over 60%. This shows you have good knowledge of the flashcard set. But don't stop there, practising everyday will help you remember the answers."
        elif gradePercentage >= 50 and gradePercentage < 60:
            letterGrade = "c"
            gradeMessage = "There's room for improvement! you achieved a mark over 50%, this shows you have decent knowledge of the flashcard set. But don't stop there, practising everyday will help you remember the answers."
        else:
            letterGrade = "D"
            gradeMessage = "oh no! you achieved a mark of less than 50%, this shows you have bad knowledge of the flashcard set. But don't worry, practising everyday will help you remember the answers."

    if request.method == "POST":
        return redirect(url_for("flashcard"))
    else:
        return render_template('checkAnswer.html', gradePercentage=gradePercentage, gradeMessage=gradeMessage, letterGrade=letterGrade)


#this is just a reroute, doesnt open a html file. Will take the current session data and write it into a file which openset page can open. will return to the openset page. 
@app.route('/flashycards/home/openset/flashcard/checkanswer/save/', methods=['GET','POST'])
def save():
    if request.method == 'GET':
        save=open(session['setName']+".txt", "w")
        for question in session['questionlist']:
            save.write(question)
            save.write("\n")

        save.close()
        saveA=open(session['setName']+"Answers.txt", "w")
        for answer in session['answerlist']:
            saveA.write(answer)
            saveA.write("\n")
        saveA.close()

        fo=open("optionList","a")
        fo.write(session['setName'])
        fo.write("\n")
        fo.close()

        return redirect(url_for("openset"))




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


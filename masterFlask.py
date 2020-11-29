from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from initQuestionfiles import initBiology, initComputing, initNorwegian, optionList
app = Flask(__name__)
app.secret_key = 'A0Zr98j /3 yX R~XHH!jmN]LWX / ,? RT'


initBiology()
initComputing()
initNorwegian()
optionList()

@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route('/flashycards/')
def root():
    return render_template('MasterPage.html')

@app.route('/flashycards/home/')
def home():
    return render_template('homePage.html')

@app.route('/flashycards/home/about/<text>')
def about(text):
    return render_template('aboutPage.html',text=text)

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

@app.route('/flashycards/home/openset/', methods=['GET','POST'])
def openset():
    if request.method == 'POST':
        session['option'] = request.form['option']
        
        for option in session['optionList']:
            option = option.replace("\n", "")
            if session['option'] == option:
                fo=open(option+".txt","r")
                session['questionlist']=fo.readlines()
                fo.close()

                fr=open(option+"Answers.txt")
                session['answerlist']=fr.readlines()
                fr.close()
                #return(jsonify(session['answerList'], session['questionlist']))
        return redirect(url_for("flashcard"))
    else:

        fo=open("optionList","r")
        session['optionList']=fo.readlines()
        fo.close()
        return render_template('openSet.html', optionList=session['optionList'])



@app.route('/flashycards/home/createset/questions/<int:intQuestionCount><setName>', methods=['GET', 'POST'])
def questions(intQuestionCount,setName):

    if request.method == 'POST':
        session['questionlist'] = request.form.getlist('question[]')
        session['answerlist'] = request.form.getlist('answer[]')
        return redirect(url_for("flashcard"))
    else:
        return render_template('createQuestion.html', questionCount=intQuestionCount,Name=session['setName'])


@app.route('/flashycards/home/openset/flashcard/', methods=['GET', 'POST'])
def flashcard():
    if request.method == 'POST':
        session['formAnswers'] = request.form.getlist("cardAnswer")
        return redirect(url_for("checkAnswer"))
    else:
        return render_template('flashCard.html', questionlist=session['questionlist'])


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


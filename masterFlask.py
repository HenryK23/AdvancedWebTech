from flask import Flask, render_template, redirect, url_for, request, jsonify, session
import re
app = Flask(__name__)
app . secret_key = 'A0Zr98j /3 yX R~XHH!jmN]LWX / ,? RT '

@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route('/flashycards/')
def root():
    return render_template('MasterPage.html'), 200

@app.route('/flashycards/home/')
def home():
    return render_template('homePage.html'), 200

@app.route('/flashycards/home/about/<text>')
def about(text):
    return render_template('aboutPage.html',text=text)

@app.route('/flashycards/home/createset/', methods=['GET', 'POST'])
def createset():
    if request.method == 'POST':
        setName = request.form['setName']
        print(setName)
        strQuestionCount="1"
        strQuestionCount = request.form['questionCount']
        intQuestionCount = int(strQuestionCount)
        return redirect(url_for("questions", intQuestionCount=intQuestionCount,setName=setName))
    else:
        return render_template('createSet.html')

@app.route('/flashycards/home/openset/')
def openset():
    return render_template('openSet.html')



@app.route('/flashycards/home/createset/questions/<int:intQuestionCount><setName>', methods=['GET', 'POST'])
def questions(intQuestionCount,setName):
    if request.method == 'POST':
        session['questionlist'] = request.form.getlist('question[]')
        session['answerlist'] = request.form.getlist('answer[]')
        return redirect(url_for("flashcard"))
    else:
        return render_template('createQuestion.html', questionCount=intQuestionCount,Name=setName)


@app.route('/flashycards/home/openset/flashcard/', methods=['GET', 'POST'])
def flashcard():
    if request.method == 'POST':
        session['formAnswers'] = request.form.getlist("cardAnswer")
        return redirect(url_for("checkAnswer"))
    else:
        return render_template('flashCard.html', questionlist=session['questionlist'], answerlist=session['answerlist'])


@app.route('/flashycards/home/openset/flashcard/checkanswer/')
def checkAnswer():
    grade=0
    for formAnswer in session['formAnswers']:
        for actualAnswer in session['answerlist']:
            if formAnswer == actualAnswer:
                grade+=1
        gradePercentage = (grade/len(session['formAnswers']))*100

    return render_template('checkAnswer.html', gradePercentage=gradePercentage)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


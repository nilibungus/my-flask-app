# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        # Get selected operation and value
        question1 = request.form['question1']  # 'square', 'cube', or 'sqrt'
        resultstu = 0
        resultcookie = 0
        resultambie = 0
        resultjoey = 0

        # Process like a mathematical function
        if question1 == 'one':
            resultstu += 1
        elif question1 == 'two':
            resultcookie += 1
        elif question1 == 'three':
            resultambie += 1
        elif question1 == 'four':
            resultjoey += 1


        question2 = request.form['question2']  # 'square', 'cube', or 'sqrt'


        # Process like a mathematical function
        if question2 == 'one':
            resultstu += 1
        elif question2 == 'two':
            resultcookie += 1
        elif question2 == 'three':
            resultambie += 1
        elif question2 == 'four':
            resultjoey += 1

        question3 = request.form['question3']  # 'square', 'cube', or 'sqrt'


        # Process like a mathematical function
        if question3 == 'one':
            resultstu += 1
        elif question3 == 'two':
            resultcookie += 1
        elif question3 == 'three':
            resultambie += 1
        elif question3 == 'four':
            resultjoey += 1

        question4 = request.form['question3']  # 'square', 'cube', or 'sqrt'


        # Process like a mathematical function
        if question4 == 'one':
            resultstu += 1
        elif question4 == 'two':
            resultcookie += 1
        elif question4 == 'three':
            resultambie += 1
        elif question4 == 'four':
            resultjoey += 1

        question5 = request.form['question3']  # 'square', 'cube', or 'sqrt'


        # Process like a mathematical function
        if question5 == 'one':
            resultstu += 1
        elif question5 == 'two':
            resultcookie += 1
        elif question5 == 'three':
            resultambie += 1
        elif question5 == 'four':
            resultjoey += 1

        question6 = request.form['question3']  # 'square', 'cube', or 'sqrt'


        # Process like a mathematical function
        if question6 == 'one':
            resultstu += 1
        elif question6 == 'two':
            resultcookie += 1
        elif question6 == 'three':
            resultambie += 1
        elif question6 == 'four':
            resultjoey += 1

        question7 = request.form['question3']  # 'square', 'cube', or 'sqrt'


        # Process like a mathematical function
        if question7 == 'one':
            resultstu += 1
        elif question7 == 'two':
            resultcookie += 1
        elif question7 == 'three':
            resultambie += 1
        elif question7 == 'four':
            resultjoey += 1
    # Show form for GET requests

        results = [resultstu, resultcookie, resultambie, resultjoey]
        if max(results) == resultstu:
            #return f"You're Stu"
            return render_template('result1.html')
        if max(results) == resultcookie:
            #return f"You're Cookie"
            return render_template('result2.html')
        elif max(results) == resultambie:
            #return f"You're Ambie"
            return render_template('result3.html')
        elif max(results) == resultjoey:
            #return f"You're Joey"
            return render_template('result4.html')


    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Simple Calculator</h2>

    <form action="/calculate" method="post">
        Number 1: <input type="number" name="num1"><br><br>

        Number 2: <input type="number" name="num2"><br><br>

        Operation:
        <select name="operation">
            <option value="add">Addition</option>
            <option value="sub">Subtraction</option>
            <option value="mul">Multiplication</option>
            <option value="div">Division</option>
        </select>

        <br><br>

        <input type="submit" value="Calculate">
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2

    return f"<h2>Result = {result}</h2>"

if __name__ == '__main__':
    app.run()

//pip install flask
//python app.py
//npm install -g vercel
//vercel login
//vercel
//vercel --prod

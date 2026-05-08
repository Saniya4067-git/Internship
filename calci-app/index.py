from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """
    <!DOCTYPE html>
    <html>

    <head>

        <title>Simple Calculator</title>

        <style>

            body{
                font-family: Arial;
                text-align:center;
                margin-top:50px;
                background:#f2f2f2;
            }

            .calculator{
                width:300px;
                margin:auto;
                padding:20px;
                background:white;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;
            }

            input{
                width:90%;
                height:40px;
                font-size:20px;
                margin-bottom:15px;
                text-align:right;
            }

            button{
                width:60px;
                height:50px;
                margin:5px;
                font-size:20px;
                cursor:pointer;
            }

        </style>

    </head>

    <body>

        <div class="calculator">

            <h1>Calculator</h1>

            <input type="text" id="display" readonly>

            <br>

            <button onclick="clearDisplay()">C</button>
            <button onclick="appendValue('/')">/</button>
            <button onclick="appendValue('*')">*</button>
            <button onclick="deleteLast()">⌫</button>

            <br>

            <button onclick="appendValue('7')">7</button>
            <button onclick="appendValue('8')">8</button>
            <button onclick="appendValue('9')">9</button>
            <button onclick="appendValue('-')">-</button>

            <br>

            <button onclick="appendValue('4')">4</button>
            <button onclick="appendValue('5')">5</button>
            <button onclick="appendValue('6')">6</button>
            <button onclick="appendValue('+')">+</button>

            <br>

            <button onclick="appendValue('1')">1</button>
            <button onclick="appendValue('2')">2</button>
            <button onclick="appendValue('3')">3</button>
            <button onclick="calculate()">=</button>

            <br>

            <button onclick="appendValue('0')">0</button>
            <button onclick="appendValue('.')">.</button>
            <button onclick="appendValue('%')">%</button>

        </div>

        <script>

            function appendValue(value){
                document.getElementById("display").value += value;
            }

            function clearDisplay(){
                document.getElementById("display").value = "";
            }

            function deleteLast(){
                let display =
                document.getElementById("display");

                display.value =
                display.value.slice(0,-1);
            }

            function calculate(){

                let display =
                document.getElementById("display");

                try{
                    display.value =
                    eval(display.value);
                }

                catch{
                    display.value = "Error";
                }
            }

        </script>

    </body>
    </html>
    """

app = app
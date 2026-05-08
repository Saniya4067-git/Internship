from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        html = """
        <html>
        <head>
            <title>Online Quiz App</title>
        </head>

        <body style="font-family: Arial; text-align:center;">

            <h1>Online Quiz Application</h1>

            <form>

                <h3>1. What is the capital of India?</h3>

                <input type="radio" name="q1"> Mumbai<br>
                <input type="radio" name="q1" id="correct1"> New Delhi<br>
                <input type="radio" name="q1"> Pune<br><br>

                <h3>2. Which language is used for web apps?</h3>

                <input type="radio" name="q2"> Python<br>
                <input type="radio" name="q2"> Java<br>
                <input type="radio" name="q2" id="correct2"> JavaScript<br><br>

                <button type="button" onclick="checkAnswers()">
                    Submit Quiz
                </button>

            </form>

            <h2 id="result"></h2>

            <script>

                function checkAnswers(){

                    let score = 0;

                    if(document.getElementById('correct1').checked){
                        score++;
                    }

                    if(document.getElementById('correct2').checked){
                        score++;
                    }

                    document.getElementById('result').innerHTML =
                    "Your Score: " + score + "/2";
                }

            </script>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
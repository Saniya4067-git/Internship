from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        html = """
        <html>
        <head>
            <title>CGPA Calculator</title>
        </head>
        <body>
            <h2>Student CGPA Calculator</h2>

            <form onsubmit="calculateCGPA(event)">
                Subject 1:
                <input type="number" id="s1" step="0.01"><br><br>

                Subject 2:
                <input type="number" id="s2" step="0.01"><br><br>

                Subject 3:
                <input type="number" id="s3" step="0.01"><br><br>

                Subject 4:
                <input type="number" id="s4" step="0.01"><br><br>

                <button type="submit">Calculate</button>
            </form>

            <h3 id="result"></h3>

            <script>
                function calculateCGPA(event){
                    event.preventDefault();

                    let s1 = parseFloat(document.getElementById('s1').value);
                    let s2 = parseFloat(document.getElementById('s2').value);
                    let s3 = parseFloat(document.getElementById('s3').value);
                    let s4 = parseFloat(document.getElementById('s4').value);

                    let cgpa = (s1+s2+s3+s4)/4;

                    document.getElementById('result').innerHTML =
                    "CGPA = " + cgpa.toFixed(2);
                }
            </script>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        html = """
        <html>

        <head>
            <title>Currency Converter</title>
        </head>

        <body style="font-family: Arial; text-align:center;">

            <h1>Currency Converter Application</h1>

            <p>Convert USD to INR</p>

            <input type="number" id="usd" placeholder="Enter USD">

            <button onclick="convertCurrency()">
                Convert
            </button>

            <h2 id="result"></h2>

            <script>

                function convertCurrency(){

                    let usd =
                    document.getElementById("usd").value;

                    let rate = 83;

                    let inr = usd * rate;

                    document.getElementById("result").innerHTML =
                    usd + " USD = " + inr + " INR";
                }

            </script>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
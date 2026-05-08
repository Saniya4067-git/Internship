from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        html = """
        <html>
        <head>
            <title>Weather Forecast App</title>
        </head>

        <body style="font-family: Arial; text-align:center;">

            <h1>Weather Forecast Web App</h1>

            <h2>Pune Weather</h2>

            <p>Temperature: 30°C</p>
            <p>Condition: Sunny</p>
            <p>Humidity: 45%</p>
            <p>Wind Speed: 12 km/h</p>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
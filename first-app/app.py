from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World from Python on Vercel!"

if __name__ == '__main__':
    app.run()

//pip install flask
//python app.py
//npm install -g vercel
//vercel login
//vercel
//vercel --prod

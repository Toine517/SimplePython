from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_clever():
    return "Hello from Clever Cloud and Python!"

if __name__ == '__main__':
    app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def catchat():
    return "catchat"

if __name__ == '__main__':
    app.run()
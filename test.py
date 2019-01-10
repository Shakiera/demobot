from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def another_word():
    return 'tggggggggggdwhey'

@app.route('/greet')
def greet_person():
    name = request.values.get('text')
    return f'hi {name}!'

if __name__ == '__main__':
    app.run('/greet', methods=['GET', 'POST'])

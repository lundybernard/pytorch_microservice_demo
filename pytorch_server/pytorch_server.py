from flask import Flask

from services import cuda_is_available

app = Flask(__name__)


@app.route('/')
def hello_api():
    return 'Hello World!\n'


@app.route('/cuda_is_available')
def cuda_is_available_api():
    return cuda_is_available()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

from app import create_app
from flask import jsonify

app = create_app('DEV')

@app.route('/')
def index():
    return jsonify('Flask Web API demo')


if __name__ == '__main__':
    app.run()

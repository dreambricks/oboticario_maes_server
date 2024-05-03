from flask import Flask

from letter import letter

app = Flask(__name__)

# configuration
app.secret_key = 'db_secret'

# init apps


# register blueprints
app.register_blueprint(letter)

@app.route('/alive')
def hello():
    return "alive"


def main():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    main()
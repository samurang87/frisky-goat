from flask import Flask


goat_bot = Flask(__name__)


@goat_bot.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    goat_bot.run()

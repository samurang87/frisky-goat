from flask import Flask, render_template
import requests


goat_bot = Flask(__name__)


def get_gif_by_tag(tag):
    request = requests.get('http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag={}&fmt=json'.format(tag))
    return request.json()['data']['image_url']

@goat_bot.context_processor
def get_goat():
    gif_goat = get_gif_by_tag("goat")
    return dict(gif=gif_goat)

@goat_bot.route('/')
def inspiration_goat():
    return render_template('youve_goat_this.html')


if __name__ == '__main__':
    goat_bot.run()

from flask import Flask, render_template
import requests
import json


goat_bot = Flask(__name__)


def get_gif_by_tag(tag):
    request = requests.get('http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag={}&fmt=json'.format(tag))
    return request.json()['data']['image_url']

@goat_bot.route('/')
def inspiration_goat():
    gif = get_gif_by_tag("goat")
    return render_template('youve_goat_this.html')

if __name__ == '__main__':
    # print(get_gif_by_tag("goat"))
    goat_bot.run()

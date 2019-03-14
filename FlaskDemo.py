
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!11111'

@app.route('/get_pics')
def getBlogPics():
    r = requests.get('https://bing.getlove.cn/latelyBingImageStory')
    return r.text



if __name__ == '__main__':
    app.run()
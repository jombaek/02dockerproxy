from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if 'url' in request.args:
        r = request.args.get('url')
        x = requests.get(r)
        return x.content
    else:
        return '<form method="get"><input name="url" type="text"><input type="submit"></form>'

if __name__ == '__main__':
    app.run()

from flask import Flask
from flask import request
import requests
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def get_page():
    if 'url' in request.args:
        r = requests.get(request.args['url'])
        return r.content
    else:
        return '''
        <form method="get" autocomplete="off">
            <input name="url" type="text">
            <input type="submit">
        <form>'''

if __name__ == '__main__':
    app.run()

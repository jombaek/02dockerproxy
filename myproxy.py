from flask import Flask
from flask import request
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_page():
    f = open('/var/log/proxy.log', 'a')
    if 'url' in request.args:
        r = requests.get(request.args['url'])
        f.write("ROUTE: " + request.access_route[0] +
                ", " + request.args['url'] + "\n")
        return r.content
    else:
        return '''
        <form method="get" autocomplete="off">
            <input name="url" type="text">
            <input type="submit">
        <form>'''
    f.close()


if __name__ == '__main__':
    app.run()

from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if 'url' in request.args:
        r = request.args.get('url')
        temp = requests.get(r)
        return temp.content
    else:
        return'''
    <head>
        <meta charset="UTF-8">
        <title>Клондайк</title>
        <style>
            .center {
            padding: 50px;
            position: fixed; top: 50%; left: 50%;
            -webkit-transform: translate(-50%, -50%);
            -ms-transform: translate(-50%, -50%);
            transform: translate(-50%, -50%);
            }
        </style>
    </head>
    <body>
        <form class="center">
            <center>
            <strong>СВОБОДНЫЙ ИНТЕРНЕТ</strong><br><br>
            <input placeholder="Введите URL:" name="url" type="text">
            <input type="submit" value="Перейти"><br><br>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Anonymous_SVG.svg/1200px-Anonymous_SVG.svg.png" width="100">
            </center>
        <form>
    </body>
'''


if __name__ == '__main__':
    app.run()

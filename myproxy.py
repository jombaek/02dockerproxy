from flask import Flask, request
import requests
import webbrowser
import codecs
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if 'url' in request.args:
        r = request.args.get('url')
        temp = requests.get(r)
        return temp.content
    else:
        if 'site' in request.args:
            f=codecs.open("test1.php", 'r')
            print(f.read())
        else:
            return '''
<form>
    <input name="url" type="text">
    <input type="submit">
</form>
<form>
    <input name='site' value="Открыть сайт" type="submit">
    <a href="test1.php">site</a>
</form>
'''
if __name__== '__name__':
    app.run()
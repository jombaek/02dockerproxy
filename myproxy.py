from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
	if 'url' in request.args:
		r = requests.get(request.args['url'])
		bts = r.content
		return bts
	else :
		return '''
		
			<form method = 'get'>
			<input name = "url" type = "text">
			<input type = "submit">
			</form>
			
		'''

if __name__ == '__main__':
    app.run()

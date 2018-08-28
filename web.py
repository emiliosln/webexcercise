from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
	#hora = time.strftime('%H:%M:%S')
	list = []
	list.append(time.strftime('%H:%M:%S'))
	list.append(time.strftime('%B'))
	list.append(time.strftime('%d'))
	list.append(time.strftime('%Y'))
	return render_template('web.html', list=list)

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')
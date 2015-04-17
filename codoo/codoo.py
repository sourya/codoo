from flask import Flask, request, session, g, render_template
from check import check_answer

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	#DATABASE = os.path.join(app.root_path, 'flaskr.db'),
	DEBUG = True,
	SECRET_KEY = 'development key',
	#USERNAME = 'admin',
	#PASSWORD = 'default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/submit')
def submit():
	session['username'] = "sourya";
	if not(hasattr(g, 'prob_code')):
		g.prob_code = ""
	return render_template('submit.html', prob_code=g.prob_code)

@app.route('/result', methods=['POST'])
def show_results():
	g.prob_code = request.form['code']
	f = open('../code/%s%s.py' %(session['username'], g.prob_code), 'w')
	f.write(request.form['solution'])
	f.close()
	result = check_answer(g.prob_code)
	return result
		
if __name__ == '__main__':
	app.run()

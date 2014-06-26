from flask import Flask
import flask.views, os
from numeral_converter import getNumerals

app = Flask(__name__)
class View(flask.views.MethodView):
    def get(self):
		return flask.render_template('index.html')
    def post(self):
		n = int(flask.request.form['expression'])
		result = getNumerals(n)
		display = "%s = %s" % (n, result)
		flask.flash(display)
		return self.get()		
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])
app.secret_key = os.urandom(24)
if __name__ == "__main__":
    app.run()
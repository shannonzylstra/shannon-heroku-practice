from flask import Flask
import flask.views
import os
app = Flask(__name__)
class View(flask.views.MethodView):
    def get(self):
		return flask.render_template('index.html')
    def post(self):
		n = int(flask.request.form['expression'])
		result = n**2
		display = "%s^2 = %s" % (n, result)
		flask.flash(display)
		return self.get()		
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])
app.secret_key = os.urandom(24)
if __name__ == "__main__":
    app.run()
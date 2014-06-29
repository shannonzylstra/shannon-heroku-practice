from flask import Flask, request, render_template
import os
from numeral_converter import getNumerals

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        n = int(request.form['expression'])
        result = getNumerals(n)
        return render_template('after.html', title="Roman Numeral Converter", number=n, roman=result)

    return render_template('index.html', title="Roman Numeral Converter")
    
app.secret_key = os.urandom(24)

if __name__ == "__main__":
    app.run()

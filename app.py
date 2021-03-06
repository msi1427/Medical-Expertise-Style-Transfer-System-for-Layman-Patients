from flask import Flask, render_template
from flask import request, url_for, redirect

import style_classifier,style_transfer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classifier',methods=['GET','POST'])
def classifier():
    if request.method == 'POST':
        text = request.form['name']
        expertise = style_classifier.classifier(text).item() * 100.0
        style = "Expert" if expertise > 50.0 else "Layman"
        return render_template('classifier_results.html',text = text,expertise = expertise, style=style)
    else :
        return render_template('classifier_input.html')
        

@app.route('/transfer',methods=['GET','POST'])
def transfer():
    if request.method == 'POST':
        expert = request.form['name']
        layman = style_transfer.transfer_to_layman(expert)
        return render_template('transfer_results.html',expert=expert,layman=layman)
    else :
        return render_template('transfer_input.html')

if __name__ == "__main__":
    app.run(debug=True)
    
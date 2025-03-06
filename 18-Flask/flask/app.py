from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/form", methods= ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello {name}"
    return render_template('form.html')

@app.route("/submit", methods= ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello {name}"
    return render_template('form.html')

## Variable rule

@app.route("/success/<int:score>")
def success(score):
    return f"You got " + str(score)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'score': score, 'result': res}
    return render_template('result1.html', results = exp)

@app.route('/final', methods = ['POST', 'GET'])
def final():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science+maths+c+data_science)/4
    else:
        return render_template('final.html')
    return redirect(url_for('successres', score = total_score))

if __name__ == "__main__":
    app.run(debug=True)
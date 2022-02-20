from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("start.html")

@app.route('/say/<msg>')
def say(msg):
 return render_template("result.html", message = msg)

@app.route('/say')
def say2():
 val = request.args.get("msg", "Not defined")
 return render_template("result.html", message = val)

@app.route('/procForm', methods=['POST'])
def processPost():
 msg1 = int(request.form['msg1'])
 msg2 = int(request.form['msg2'])
 return render_template("result.html", message = int(msg1+msg2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

app.run(host="0.0.0.0", port=8000, debug = true)

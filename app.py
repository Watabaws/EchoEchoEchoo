from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hidere():
    return render_template('text_input.html')

@app.route("/eko")
def lessee():
    return render_template("eko.html", user = request.args['user'])


if __name__ == "__main__":
    app.debug = True
    app.run()



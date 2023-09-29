from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def helloworld():
    return render_template('index.html', text="hello world 1")
if __name__ == "__main__":
    app.run()
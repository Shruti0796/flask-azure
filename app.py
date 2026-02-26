from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello it's shruti shanklesha"

if __name__ == "__main__":
    app.run()
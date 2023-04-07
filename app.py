from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path="", static_folder="")

@app.route("/")
def index():
    return send_from_directory("public", "index.html")

if __name__ == "__main__":
    app.run(debug=True)

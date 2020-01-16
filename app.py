from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

USERS = {
    "foo": "bar"
}


def auth(login, password):
    try:
        valid = USERS[login] == password
    except KeyError:
        valid = False
    return valid


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        return render_template("logged.html", logged=auth(login, password))

    return render_template("login.html")


if __name__ == "__main__":
    app.run()

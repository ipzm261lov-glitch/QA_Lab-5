from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "privat24-taf-training-secret"

# Навчальні тестові дані
TEST_USER = {
    "username": "test_user_01",
    "password": "TestPass123"
}

ACCOUNT = {
    "balance": 17000.00
}


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if (
            username == TEST_USER["username"]
            and password == TEST_USER["password"]
        ):
            session["authenticated"] = True
            return redirect(url_for("dashboard"))

        error = "Invalid credentials"

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():

    if not session.get("authenticated"):
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        balance=ACCOUNT["balance"]
    )


@app.route("/transfer", methods=["GET", "POST"])
def transfer():

    if not session.get("authenticated"):
        return redirect(url_for("login"))

    error = None
    success = None

    if request.method == "POST":
        recipient = request.form.get("recipient", "")
        amount = request.form.get("amount", type=float)

        if not recipient:
            error = "Recipient is required"

        elif amount is None or amount <= 0:
            error = "Invalid amount"

        elif amount > ACCOUNT["balance"]:
            error = "Insufficient funds"

        else:
            ACCOUNT["balance"] -= amount
            success = "Transfer completed successfully"

    return render_template(
        "transfer.html",
        balance=ACCOUNT["balance"],
        error=error,
        success=success
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )

from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__)

#game setup
number = random.randint(1, 10)
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def game():
    global attempts
    message = ""
    won = False

    if request.method == 'POST':
        guess = int(request.form["guess"])
        attempts += 1
        if guess < number:
            message = "Too low! Try again."
        elif guess > number:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You've guessed the number {number} in {attempts} attempts."
            won = True
    return render_template("index.html", message=message, won=won)

@app.route("/restart")
def restart():
    global number, attempts
    number = random.randint(1, 10)
    attempts = 0
    return redirect(url_for("game"))
@app.route("/reset", methods=["POST"])
def reset():
    global number, attempts
    number = random.randint(1, 10)
    attempts = 0
    return redirect(url_for("game"))
if __name__ == '__main__':
    app.run(debug=True)
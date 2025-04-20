from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for flashing messages

# Connect to XAMPP MySQL database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Default for XAMPP
        database="portfolio"
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
    exit()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            message = request.form["message"]

            sql = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
            values = (name, email, message)
            cursor.execute(sql, values)
            db.commit()

            flash("Message sent successfully!", "success")
            return redirect(url_for("index"))
        except Exception as e:
            print(f" Error inserting into DB: {e}")
            flash(" Failed to send message.", "error")
            return redirect(url_for("index"))

    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("saran-resume.html")


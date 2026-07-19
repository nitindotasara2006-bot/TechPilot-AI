from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "techpilot_secret"

@app.route("/")
def home():
    return render_template("indexx.html")

@app.route("/Cybersecurity.html")
def cyber():
    return render_template("Cybersecurity.html")

@app.route("/CyberCertificates.html")
def certificates():
    return render_template("CyberCertificates.html")

@app.route("/bccertificates.html")
def bc_certificates():
    return render_template("bccertificates.html")

@app.route("/Blockchain.html")
def blockchain():
    return render_template("blockchain.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404

@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    if request.method == "POST":

        name = request.form.get("Name")
        email = request.form.get("Email")
        message = request.form.get("message")

        with open("feedback.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Message: {message}\n")
            file.write("----------------------\n")

        flash("✅ Thank you for your feedback! Visit Again.")
        return redirect(url_for("home"))

    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
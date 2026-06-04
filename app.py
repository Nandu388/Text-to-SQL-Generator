from flask import Flask, render_template, request
from sql_generator import generate_sql

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    sql_query = ""
    prompt = ""

    if request.method == "POST":

        prompt = request.form["prompt"]

        sql_query = generate_sql(prompt)

    return render_template(
        "index.html",
        sql_query=sql_query,
        prompt=prompt
    )

if __name__ == "__main__":
    app.run(debug=True)
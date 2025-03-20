from flask import Flask, render_template, request
from langflow_flows.answer_faq_flow import ask_faq
from langflow_flows.recommend_products_flow import recommend_products

app = Flask(__name__)


@app.route("/")
def dashboard():
    """
    Rota para a página inicial (Dashboard).
    """
    return render_template("dashboard.html")


@app.route("/faq", methods=["GET", "POST"])
def faq():
    """
    Rota para responder a perguntas frequentes.
    """
    response = None
    if request.method == "POST":
        customer_question = request.form["question"]
        response = ask_faq(customer_question)
    return render_template("faq.html", response=response)


@app.route("/recommendations", methods=["GET", "POST"])
def recommendations():
    """
    Rota para recomendar produtos com base nas preferências do usuário.
    """
    recommendations = None
    if request.method == "POST":
        preferences = request.form["preferences"]
        recommendations = recommend_products(preferences)
    return render_template("recommendations.html", recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)

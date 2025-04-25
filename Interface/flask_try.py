from flask import Flask, render_template, request, redirect, url_for
import datetime
from pymongo import MongoClient
from dateutil.relativedelta import relativedelta


from MongoDB.Total_Money_In import In_monthly
from MongoDB.Total_Money_Out import Out_monthly
from MongoDB.T2_chart_data import retrieve_expense_data
from Graphs.categories_pie_chart import draw_pie_chart
from Graphs.categories_bar_chart import draw_T2_chart
from Graphs.categories import create_expense_plot
from Graphs.sankey import sankey

client = MongoClient("mongodb://localhost:27018/")
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print("MongoDB connection error:", e)

app = Flask(__name__)

today = datetime.datetime.now()
categories = ["Toll", "Food", "Parking", "Transport", "Accommodation", "Gasoline", "Telecom", "Miscellaneous"]
user_budget = [1500, 250, 200, 300, 100, 150, 300, 100, 50, 300, 250]

today= datetime.datetime(2025, 3, 13)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for("home", username=username))
    return render_template("Login.html")


@app.route("/<username>")
def home(username):
    current_month = "2025-02" ##rmb
    total_income = In_monthly(current_month)
    total_expense = Out_monthly(current_month)
    budget = sum(user_budget[2:-1]) - total_expense
    
    current_month = today.strftime("%Y-%m")
    draw_pie_chart(current_month)

    return render_template("Dashboard.html", username=username, date=today, income=total_income, expense=total_expense, budget=budget)


@app.route("/<username>/Trend_1", methods=["GET", "POST"])
def trend_1(username):
    if request.method == "POST":
        mode = request.form.get('time_period')
        create_expense_plot(today, mode)
    else:
        create_expense_plot(today)
    return render_template("Trend_1.html", username=username, categories=categories)


@app.route("/<username>/Trend_2")
def trend_2(username):
    last_month = today - relativedelta(months=1)
    date = last_month.strftime("%B")
    chart_data = retrieve_expense_data(today)
    budget = user_budget[2:-1]

    draw_T2_chart(today,budget)
       
    return render_template("Trend_2.html", username=username, date=date, chart_data = chart_data, categories=categories, budget = budget)


@app.route("/<username>/Budget",  methods=["GET", "POST"])
def budget(username):
    date = today.strftime("%B")
    global user_budget
    income = [user_budget[0], user_budget[1]]
    
    if request.method == "POST":
        wadge = float(request.form.get("wadge", 0))
        other = float(request.form.get("other", 0))
        income = [wadge, other]

        expenses = []
        for i in range(len(categories)): 
            val = request.form.get(f'expense_{i}', 0)
            expenses.append(float(val))

        saving = float(request.form.get("saving", 0))

        # Reconstruct full budget list
        new_budget = [wadge, other] + expenses + [saving]

        sankey(new_budget)
        user_budget= new_budget
        print("Updated Budget:", user_budget)
        
    else:
        sankey(user_budget)

    return render_template("Budget.html", username=username, date=date, budget = user_budget, categories=categories, income = income)



if __name__ == "__main__":
    app.run(debug=True)

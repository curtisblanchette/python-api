from flask import Flask, jsonify, request, render_template
from dynaconf import FlaskDynaconf

from app.models.expense import ExpenseSchema, Expense
from app.models.income import IncomeSchema, Income
from app.models.transaction_type import TransactionType

import os
import pprint

app = Flask(__name__)
# this module bakes our dynaconf settings into the Flask app
# placing them on app.config
FlaskDynaconf(app, settings_files=["settings.toml"])

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]


@app.route('/')
def get_index():
    # renders a template with delimited replacements
    return render_template('index.html', name="Flask", config=app.config)


@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return '', 204


@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return '', 204


# allows the code to execute when run as a script
# but not when imported as a module.
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = str(os.environ.get('HOST', '0.0.0.0'))
    app.run(port=port, host=host)




from flask import Flask, url_for, request, redirect, render_template, flash, session
from forms import RegistrationForm, LoginForm, ExpenseForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = "chQRQUcWGuf7eGRGJ9IytSLKIx5rI"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# user_expenses = [
#     {'id':1, 'description': 'Groceries', 'amount': 1350.9959, 'category': 'Food', 'date': '2026-11-01'},
#     {'id':2, 'description': 'Uber ride', 'amount': 600, 'category': 'Transport', 'date': '2026-11-02'},
#     {'id':3, 'description': 'Lunch', 'amount': 630, 'category': 'Food', 'date': '2026-11-03'},
#     {'id':4, 'description': 'Electricity bill', 'amount': 340, 'category': 'Bills', 'date': '2026-11-04'},
#     {'id':5, 'description': 'Internet bill', 'amount': 800, 'category': 'Bills', 'date': '2026-11-05'}
# ]

# users = []

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    expenses = db.relationship("Expense", backref='owner', lazy=True)

    def __str__(self):
        return f"<User {self.username}>"


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return f"<Expense {self.description}, Amount: {self.amount}>"


def check_login():
    if session.get("user_id"):
        return True 
    return False 

@app.route('/')
def home():
    # flash("Welcome to Expense Tracker App", 'success')
    breakdown = {}
    # for exp in user_expenses:
    #     if exp['category'] in breakdown:
    #         breakdown[exp['category']] += exp['amount']
    #     else:
    #         breakdown[exp['category']] = exp['amount']
    return render_template('home.html', spend_by_cat=breakdown)

@app.route('/dashboard')
def dashboard():
    if check_login():
        total = 0
        current_user = session['user_id']
        user_expenses = Expense.query.filter_by(user_id=current_user).all()

        for exp in user_expenses: 
            total += exp.amount
        
        transaction_count = len(user_expenses)

        categories = []
        breakdown = {}

        for exp in user_expenses:
            categories.append(exp.category)

            if exp.category in breakdown:
                breakdown[exp.category] += exp.amount
            else:
                breakdown[exp.category] = exp.amount
            


        return render_template('dashboard.html', monthly_income = 27000,total_balance=total, count=transaction_count, spend_by_cat=breakdown)
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))

@app.route('/expenses')
def expenses():
    if check_login():
        current_user = session["user_id"]
        user_expenses = Expense.query.filter_by(user_id=current_user).order_by(Expense.date.desc()).all()
        total = 0
        for exp in user_expenses:
            total += exp.amount
        n_transaction_count = len(user_expenses) # we can not use count as it is already used in dashboard function, so we can use n_transaction_count instead of count
        return render_template('expenses.html', expenses=user_expenses, count=n_transaction_count, total=total)
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        phone = form.phone.data
        password = form.password.data

        # validating if the user/email already exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("Account with the email already exists! Try login.", "error")
            return render_template("register.html", form=form)

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash("Account with username already exists! Try a new username", "error")
            return render_template("register.html", form=form)      

        # Register teh user/Add the user in the database
        user = User(username=username, email=email, phone=phone, password=generate_password_hash(password))

        #save to db
        db.session.add(user)
        db.session.commit()

        flash(f"Account created for {username}!", "success")
        return redirect(url_for('login'))  #redirect to login page after successful registration

    return render_template('register.html', form=form)

@app.route('/expense/<int:expense_id>')
def expense_details(expense_id):
    if check_login():
        expense = Expense.query.get_or_404(expense_id)
        if expense.user_id == session["user_id"]:
            return render_template('single_expense.html', expense=expense)
        flash("Unauthorized user!", "error")
        return redirect(url_for("expenses"))
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))    

@app.route('/expense/<int:expense_id>/delete', methods=["POST"])
def delete_expense(expense_id):
    if check_login():
        #return f"<h3>Expense Deleted: {expense_id}</h3>"
        expense = Expense.query.get_or_404(expense_id)
        if expense.user_id == session["user_id"]:
            db.session.delete(expense)
            db.session.commit()
            flash(f"Expense {expense.description} Rs. {expense.amount} Deleted", "error")
            return redirect(url_for('expenses'))  #redirect to expenses page after deleting the expense
        else:
            flash("Unauthorized user!", "error")
            return redirect(url_for("expenses"))
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))

@app.route('/expense/<int:expense_id>/edit', methods=["GET", "POST"])
def edit_expense(expense_id):
    if check_login():
        expense = Expense.query.filter_by(
            id = expense_id,
            user_id = session['user_id']
        ).first_or_404()
        form = ExpenseForm(obj=expense)

        if form.validate_on_submit():
            expense.description = form.description.data
            expense.amount = form.amount.data
            expense.category = form.category.data

            db.session.commit()
            flash('Expense Update successfully!','success')
            return redirect(url_for("expense_details", expense_id=expense.id))
        else:
            return render_template('edit_expense.html', form=form, expense=expense)
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))

@app.route('/expenses/category/<string:category_name>')
def expenses_by_category(category_name):
    if check_login():
        return f"<h2>Expenses in category: {category_name}</h2>"
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))

@app.route('/add-expense', methods=["GET", "POST"])
def add_expense():
    if check_login():
        form = ExpenseForm()

        if form.validate_on_submit():
            description = form.description.data
            amount = form.amount.data
            category = form.category.data
            # date = form.date.data
            current_user = session['user_id']
            
            # Save to DB
            expense = Expense(description=description, amount=amount, category=category, user_id=current_user)
            db.session.add(expense)
            db.session.commit()

            flash(f"Expense of amount Rs.{amount} added.", "success")
            return redirect(url_for('expenses'))

        return render_template('add_expense.html', form=form)
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        entered_mail = form.email.data 
        entered_password = form.password.data

        existing_user = User.query.filter_by(email=entered_mail).first()
            
        if existing_user and check_password_hash(existing_user.password, entered_password):
            # session define 
            session["user_id"] = existing_user.id
            session["username"] = existing_user.username
            flash(f"Welcome back, {existing_user.username}!!","success")
            return redirect(url_for('dashboard'))
        
        flash("Invalid email or password!!", "error")

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    if check_login():
        session.clear()
        flash("You have been logged out!","success")
        return redirect(url_for("home"))
    else:
        flash("Please login to continue.", "error")
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)   #this is use in development mode only, in production mode use gunicorn or uwsgi


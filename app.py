from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Category, Expense

app = Flask(__name__)
app.secret_key = 'unique_secret_key_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def dashboard():
    categories = Category.query.all()
    summary_report = []
    
    for cat in categories:
        current_spent = sum([item.cost for item in cat.expense_list])
        balance = cat.monthly_limit - current_spent
        
        summary_report.append({
            'title': cat.title,
            'limit': cat.monthly_limit,
            'spent': current_spent,
            'balance': balance,
            'alert_status': current_spent > cat.monthly_limit
        })

    return render_template('index.html', summary=summary_report, categories=categories)

@app.route('/create-category', methods=['POST'])
def create_category():
    name_input = request.form.get('category_name')
    limit_input = float(request.form.get('budget_limit'))
    
    new_cat = Category(title=name_input, monthly_limit=limit_input)
    db.session.add(new_cat)
    db.session.commit()
    
    return redirect(url_for('dashboard'))

@app.route('/log-expense', methods=['POST'])
def log_expense():
    cost_input = float(request.form.get('expense_cost'))
    reason_input = request.form.get('expense_reason')
    cat_id_input = int(request.form.get('category_select'))
    
    entry = Expense(cost=cost_input, reason=reason_input, category_id=cat_id_input)
    db.session.add(entry)
    db.session.commit()
    
    cat_check = Category.query.get(cat_id_input)
    total_spent = sum([x.cost for x in cat_check.expense_list])
    limit = cat_check.monthly_limit
    
    if total_spent > limit:
        flash(f"CRITICAL: You have exceeded the budget for {cat_check.title}!", "danger")
    elif total_spent >= (limit * 0.9):
        flash(f"Watch out! Less than 10% budget remaining for {cat_check.title}.", "warning")
    else:
        flash("Expense saved successfully.", "success")
        
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# from flask import Flask, render_template, request, redirect, url_for
# from database import db
# from models import Food

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calories.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

# # Example daily calorie limit
# DAILY_CALORIE_LIMIT = 2000

# @app.route('/')
# def index():
#     foods = Food.query.all()
#     total_calories = sum(food.calories for food in foods)  # Calculate total consumed calories
#     remaining_calories = DAILY_CALORIE_LIMIT - total_calories
#     return render_template('index.html', total_calories=total_calories, remaining_calories=remaining_calories, foods=foods)

# @app.route('/add_food', methods=['GET', 'POST'])
# def add_food():
#     if request.method == 'POST':
#         name = request.form['name']
#         calories = float(request.form['calories'])
#         meal_type = request.form['meal_type']

#         new_food = Food(name=name, calories=calories, meal_type=meal_type)
#         db.session.add(new_food)
#         db.session.commit()
#         return redirect(url_for('index'))

#     return render_template('add_food.html')

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create tables if they don't exist
#     app.run(debug=True)


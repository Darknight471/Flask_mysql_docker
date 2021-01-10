from flask import Flask, request, flash, url_for, redirect, render_template  
from flask_sqlalchemy import SQLAlchemy  
  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:dbpassword@db/Employees'  
app.config['SECRET_KEY'] = "secret key"  
  
db = SQLAlchemy(app)  
  
class Employees(db.Model):  
   id = db.Column('employee_id', db.Integer, primary_key = True)  
   name = db.Column(db.String(100)) 
  
   def __init__(self, name):
      self.name = name
 
@app.route('/')  
def list_employees():  
   return render_template('list_employees.html', Employees = Employees.query.all() )  
 
@app.route('/add', methods = ['GET', 'POST'])  
def addEmployee():  
   if request.method == 'POST':  
      if not request.form['name']:  
         flash('Please enter the fields', 'error')  
      else:  
         employee = Employees(request.form['name'])
           
         db.session.add(employee)  
         db.session.commit()  
         flash('Record was successfully added')  
         return redirect(url_for('list_employees'))  
   return render_template('add.html')  
  
if __name__ == '__main__':  
   db.create_all()  
   app.run(debug = True)

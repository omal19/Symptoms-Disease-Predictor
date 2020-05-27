from flask import Flask, render_template, request, redirect
import os
#Developer - Omal Bharuka

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("symptom.html")


import Random_forest as rf 
value=[]

@app.route('/symptom',methods=['GET', 'POST'])
def symptom():
     return render_template("symptom.html")
     

@app.route('/symptoms_result', methods=['GET', 'POST'])
def symptom_result():
     value = request.form.getlist('sympt')
     print(value)
     result = rf.RandomForest(value)
     return render_template("symptoms_result.html", pred=result, symptoms=value)
     
#Developer - Omal Bharuka
if __name__ == '__main__':
    app.run()

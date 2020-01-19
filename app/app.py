from flask import Flask, render_template 
from flask_bootstrap import Bootstrap 
from Controller.ListaParalizacao import *


app = Flask(__name__) 
bootstrap = Bootstrap(app)          

@app.route("/")                   
def hello():        
    cListar = ListaParalizacao()
    Result = cListar.Listar()               
    return render_template('home.html', data =Result)   

@app.route('/home')
def welcome():
    return render_template('index.html')      
if __name__ == "__main__":        
    app.run(debug=True)                     
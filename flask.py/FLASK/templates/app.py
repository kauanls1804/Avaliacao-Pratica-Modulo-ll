from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/soma')
def soma():

    n1 = int(request.args.get('valor1', '0'))
    n2 = int(request.args.get('valor2', '0'))


    conta = n1 + n2 


    return {
        
        'resultado': conta
    }




@app.route('/subitrair')
def conta2():

    n1 = int(request.args.get('valor1', '0'))
    n2 = int(request.args.get('valor2', '0'))
 

    conta = n1 - n2 


    return {
    
        'resultado': conta
    }


@app.route('/multiplcar')
def multiplicar():

    n1 = int(request.args.get('valor1', '0'))
    n2 = int(request.args.get('valor2', '0'))


    conta = n1 * n2 


    return {
       
        'resultado': conta
    }


@app.route('/dividir')
def dividir():

    n1 = int(request.args.get('valor1', '0'))
    n2 = int(request.args.get('valor2', '0'))
  

    conta = n1 / n2 


    return {
       
        'resultado': conta
    }
    

if __name__ == '__main__':
    app.run(debug=True)
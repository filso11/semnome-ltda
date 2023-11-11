from flask import Flask, render_template, request,flash, redirect

app = Flask(__name__)

dados = []

def calcular_imc(peso, altura):
    imc = peso / ((altura / 100) ** 2)
    return int(imc)

@app.route("/", methods=['GET', 'POST'])
def index():
    nome = ''
    email = ''
    peso = 0
    altura = 0
    imc = 0
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            imc = calcular_imc(peso,altura)
            if 'calcular' in request.form:
                return render_template("imc-page.html", imc=imc, nome=nome, email=email, peso=peso, altura=altura, dados=dados)
            elif 'limpar' in request.form:
                return render_template("imc-page.html", imc=0, dados=dados)
            elif 'salvar' in request.form:
                dados.append({'nome': nome, 'email': email, 'imc': imc})
                return render_template("imc-page.html", dados=dados, imc=0)
        except Exception as e:
            print(e)
            return render_template("imc-page.html", dados=dados, imc=0)

            
    else: 
        return render_template("imc-page.html", imc=0, dados=dados)
    return render_template("imc-page.html", dados=dados)
            

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
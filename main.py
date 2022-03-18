from flask import Flask
app = Flask('app')

@app.route('/')
def principal():
  return '<h1>Olá Mundo!</h1>'
@app.route('/unifran')
def unifran():
  return '<h2>Universidade de Franca</h2>'
@app.route('/dashboard/<nome>')
def dashboard(nome):
  return f'Olá, {nome}'

if __name__ =='__main__':
  app.run(host='0.0.0.0', port=8080)
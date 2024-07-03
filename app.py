from flask import Flask, render_template, request, jsonify, render_template
import cotizador

app = Flask(__name__)

@app.route('/')
def index():
    return ('index.html')
    #render_template('index.html')

@app.route('/cotizar', methods=['GET'])
def cotizar():
    marca = request.form['marca']
    modelo = request.form['modelo']
    version = request.form['version']
    año = int(request.form['año'])
    pvp_mercado = float(request.form['pvp_mercado'])
    kilometraje = int(request.form['kilometraje'])
    rotacion = request.form['rotacion'].lower()

    valor_final = cotizador.cotizar_auto(pvp_mercado, kilometraje, rotacion)
    return jsonify(valor_final=valor_final)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)






























#from flask import Flask, render_template, request
#import cotizador

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/cotizar', methods=['POST'])
#def cotizar():
 #   marca = request.form['marca']
  #  modelo = request.form['modelo']
   # version = request.form['version']
   # año = int(request.form['año'])
   ## pvp_mercado = float(request.form['pvp_mercado'])
   # kilometraje = int(request.form['kilometraje'])
   # rotacion = request.form['rotacion'].lower()


    #valor_final = cotizador.cotizar_auto(pvp_mercado, kilometraje, rotacion)
    #return valor_final

#if __name__ == "__main__":
 #   app.run(debug=True)



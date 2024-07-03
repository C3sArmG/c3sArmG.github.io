from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cotizar', methods=['POST'])
def cotizar():
    try:
        data = request.form
        marca = data.get('marca')
        modelo = data.get('modelo')
        version = data.get('version')
        año = data.get('año')
        pvp_mercado = data.get('pvp_mercado')
        kilometraje = data.get('kilometraje')
        rotacion = data.get('rotacion')

        # Importar función de cotización desde cotizador.py
        from cotizador import calcular_valor_auto

        valor_final = calcular_valor_auto(marca, modelo, version, año, pvp_mercado, kilometraje, rotacion)

        return jsonify({'valor_final': valor_final})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)






























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



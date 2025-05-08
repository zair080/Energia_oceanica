from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO

matplotlib.use('Agg')

app = Flask(__name__)

# Ruta principal que renderiza la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graficas')
def graficas():
    return render_template('graficas.html')

@app.route('/calculo')
def calculo():
    return render_template('calculo.html')

@app.route('/tipos')
def tipos():
    return render_template('tipos.html')

@app.route('/desventajas')
def desventajas():
    return render_template('desventajas.html')

@app.route('/ventajas')
def ventajas():
    return render_template('ventajas.html')




# Ruta para el cálculo de consumo energético
@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.json
    resultado = {}

    if datos.get("computadora"):
        resultado["computadora"] = 0.1 * datos["horas_pc"]

    resultado["celular"] = 0.01 * datos["cargas_celular"]

    if datos.get("tv"):
        resultado["tv"] = 0.15 * datos["cantidad_tv"]

    resultado["total"] = sum(resultado.values())

    return jsonify(resultado)

# Ruta para la generación de gráficos de energía renovable
@app.route("/grafico/<pais>")
def grafico(pais):
    df = pd.read_csv("BaseLaboratorio1.csv")
    df_pais = df[(df["Country"] == pais) & (df["Year"].between(2000, 2023))]

    if df_pais.empty:
        return "No hay datos", 404


    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df_pais["Year"], df_pais["TotalRenewableEnergy"], label="Total Energy", color="cyan")
    ax.bar(df_pais["Year"], df_pais["HydroEnergy"], label="Hydro", color="purple")
    ax.bar(df_pais["Year"], df_pais["WindEnergy"], label="Wind", color="yellow")
    ax.bar(df_pais["Year"], df_pais["SolarEnergy"], label="Solar", color="blue")
    ax.bar(df_pais["Year"], df_pais["OtherRenewableEnergy"], label="Other", color="green")

    ax.set_title(f"Energía Renovable en {pais}")
    ax.set_xlabel("Año")
    ax.set_ylabel("Producción (kWh)")
    ax.set_xticks(df_pais["Year"])
    ax.set_xticklabels(df_pais["Year"], rotation=45, ha="right")
    ax.legend(loc="upper left", fontsize="small", framealpha=0.9)
    plt.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)

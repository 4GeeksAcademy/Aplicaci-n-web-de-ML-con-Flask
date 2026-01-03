
import numpy as np
import pickle
import os
from flask import Flask, request, render_template
import joblib

import os
import numpy as np
import joblib
from flask import Flask, request, render_template

# Localización exacta de la carpeta actual (src)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Localización exacta de la carpeta templates
template_path = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_path)

# Cargar modelo con ruta absoluta
model_path = os.path.join(current_dir, 'modelo_diabetes.joblib')
model = joblib.load(model_path)

@app.route('/')
def home():
    # Añadimos un print para depurar en la consola
    print(f"Buscando templates en: {template_path}")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(data)])
    output = "Paciente con DIABETES" if prediction[0] == 1 else "Paciente SIN diabetes"
    return render_template('index.html', prediction_text=f'Resultado: {output}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



import re

def extract_info_from_json(data):
    fmi = f"{data['circulo']}-{data['numeroMatricula']}"
    anotaciones = []

    for texto in data['textoAnotaciones']:
        match = re.search(r"ANOTACION: Nro (\d+).*ESPECIFICACION: (\d{3,5})", texto)
        if match:
            anotaciones.append({
                "numero": int(match.group(1)),
                "codigo_especificacion": match.group(2)
            })

    return {
        "fmi": fmi,
        "anotaciones": anotaciones
    }

TIPO_CHOICES = [
        ('Urbano', 'Urbano'),
        ('Rural', 'Rural'),
    ]
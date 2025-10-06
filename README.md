# Trabajo-Pr-ctico-Integrador-TPI-

### REST Countries

https://restcountries.com/v3.1/all?fields=name,population,area,region,subregion

De aqui se pueden obtener los datos necesarios 


<hr>

## Ejecutar el generador de datos (CSV)

```sh
# se crea en entorno virtual
python3 -m venv venv
# se activa el entorno virtual
source venv/bin/activate
# se instalan las dependencias
pip install -r requirements.txt
# se ejecuta el script
python generate_csv.py
```
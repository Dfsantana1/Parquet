import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

data = [
    {"pregunta": "¿Cuál es la capital de Colombia?", "respuesta": "Bogotá"},
    {"pregunta": "¿Cuál es la moneda de Japón?", "respuesta": "Yen"},
    {"pregunta": "¿Cuál es el río más largo del mundo?", "respuesta": "Amazonas"},
    {"pregunta": "¿Cuál es el animal más rápido?", "respuesta": "Guepardo"},
]

df = pd.json_normalize(data)

table = pa.Table.from_pandas(df)

pq.write_table(table, 'C:\\Users\\Diego\\OneDrive\\Escritorio\\serverpy\\tu_archivo.parquet')

table = pq.read_table('C:\\Users\\Diego\\OneDrive\\Escritorio\\serverpy\\tu_archivo.parquet')



print(df)

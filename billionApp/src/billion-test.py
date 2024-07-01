import pandas as pd
from google.cloud import storage
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def process_data():
    file_name = 'World_Billionaire_2024.csv'
    file_path = f'gs://bucket_billion/{file_name}'

    # Leer el archivo directamente desde GCS2
    df = pd.read_csv(file_path)
    df_cleaned = df.dropna()

    # Guardar los datos procesados en un nuevo archivo CSV
    processed_file_name = f'processed_{file_name}'
    processed_file_path = f'gs://bucket_billion_process/{processed_file_name}'
    df_cleaned.to_csv(processed_file_path, index=False)

    print(f"procesado documento: {processed_file_name}")
    return 'Data processed and saved successfully!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
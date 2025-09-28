import pandas as pd
import numpy as np

def limpiar_dataset_encuesta(df):
    df = df.copy()

    # 1. Nombres
    df['Nombre'] = df['Nombre'].replace('', np.nan)
    df['Nombre'] = df['Nombre'].apply(lambda x: str(x).title() if pd.notna(x) else x)

    # 2. Edades
    mapa_edades = {'treinta y dos': 32, 'cuarenta': 40}
    df['Edad'] = df['Edad'].replace(mapa_edades)
    df['Edad'] = pd.to_numeric(df['Edad'], errors='coerce')

    # 3. Puntuaciones
    df['Puntuación'] = pd.to_numeric(df['Puntuación'], errors='coerce')

    # 4. Fechas
    df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce', dayfirst=True)

    # 5. Comentarios + nulos
    df['Comentario'] = df['Comentario'].replace('', np.nan)
    df = df.fillna({'Nombre': 'Desconocido', 'Comentario': 'Sin comentario'})

    return df

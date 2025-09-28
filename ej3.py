import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt

# ===== Dataset =====
np.random.seed(42); n=100
df = pd.DataFrame({
 'ID': range(1,n+1),
 'Superficie_m2': np.random.normal(120,40,n).astype(int),
 'Habitaciones': np.random.choice([1,2,3,4,5],n,p=[.1,.25,.35,.25,.05]),
 'Baños': np.random.choice([1,2,3],n,p=[.3,.5,.2]),
 'Antigüedad_años': np.random.randint(0,50,n),
 'Distancia_Metro_km': np.random.exponential(2,n).round(1),
 'Zona': np.random.choice(['Centro','Norte','Sur','Este','Oeste'],n),
 'Parking': np.random.choice([1,0],n,p=[.6,.4])
})
precio = (df.Superficie_m2*2000 + df.Habitaciones*15000 + df.Baños*10000
          - df.Antigüedad_años*500 - df.Distancia_Metro_km*5000 + df.Parking*20000)
df['Precio_EUR'] = np.maximum(precio+np.random.normal(0,20000,n),50000).astype(int)

# ===== Análisis =====
corr = df.corr(numeric_only=True)['Precio_EUR'].sort_values(ascending=False)
print("\nCorrelaciones con el precio:\n",corr)
print("\nTop 3 variables influyentes:", list(corr.index[1:4]))

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm"); plt.show()
print("\nPrecio promedio por zona:\n", df.groupby('Zona')['Precio_EUR'].mean())
sns.barplot(x='Zona', y='Precio_EUR', data=df, estimator='mean'); plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos
df = pd.DataFrame({
    'Vendedor': ['Carmen','Diego','Elena']*6,
    'Región': ['Norte','Sur','Centro']*6,
    'Mes': ['Enero']*3+['Febrero']*3+['Marzo']*3+['Enero']*3+['Febrero']*3+['Marzo']*3,
    'Ventas':[25000,30000,28000,27000,32000,30000,29000,35000,31000,
              26000,31000,29500,28000,33000,32000,30000,36000,33500],
    'Meta':[25000]*18
})

# 1. Ventas totales por vendedor
ventas_v = df.groupby('Vendedor')['Ventas'].agg(Total='sum', Promedio='mean', Registros='count')
print("\n=== Ventas por Vendedor ===\n", ventas_v)
print("Mejor vendedor:", ventas_v['Total'].idxmax())

# 2. Región más rentable
ventas_r = df.groupby('Región')['Ventas'].sum()
print("\n=== Ventas por Región ===\n", ventas_r)
print("Región más rentable:", ventas_r.idxmax())

# 3. Crecimiento mensual
orden = ['Enero','Febrero','Marzo']
ventas_m = df.groupby('Mes')['Ventas'].sum().reindex(orden)
print("\n=== Ventas Mensuales ===\n", ventas_m)
ventas_m.plot(marker='o', title="Tendencia de Ventas"); plt.show()

# 4. Cumplimiento de metas
df['Cumplimiento_%'] = df['Ventas']/df['Meta']*100
print("\n=== Cumplimiento de Metas ===\n", df[['Vendedor','Mes','Ventas','Cumplimiento_%']].head())

# 5. Visualizaciones
for x,t in [('Vendedor',"Ventas Totales por Vendedor"),('Región',"Ventas Totales por Región")]:
    sns.barplot(x=x,y='Ventas',data=df,estimator=sum,ci=None); plt.title(t); plt.show()

sns.boxplot(x='Vendedor',y='Cumplimiento_%',data=df); plt.title("Cumplimiento de Metas por Vendedor"); plt.show()

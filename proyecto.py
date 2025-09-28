import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt, os
from sqlalchemy import create_engine
from datetime import datetime

class Analizador:
    def __init__(self, cfg=None): self.cfg,self.df={},pd.DataFrame()
    def conectar(self):
        try:
            url=f"postgresql://{self.cfg['user']}:{self.cfg['password']}@{self.cfg['host']}:{self.cfg.get('port',5432)}/{self.cfg['database']}"
            self.df=pd.read_sql("select * from ventas v join empleados e on v.empleado_id=e.empleado_id",create_engine(url))
            print("Conexión establecida.")
        except: self.simular()
    def simular(self,n=300):
        np.random.seed(1)
        e=pd.DataFrame({'empleado_id':range(1,11),'dpto':np.random.choice(['Ventas','TI'],10),'ciudad':np.random.choice(['Bogotá','Cali'],10)})
        v=pd.DataFrame({'empleado_id':np.random.choice(e.empleado_id,n),'monto':np.random.exponential(1000,n),'fecha':pd.date_range('2024-01-01',periods=n,freq='D')})
        self.df=v.merge(e,on='empleado_id'); print("Datos simulados.")
    def kpis(self): print("KPIs:",self.df.monto.sum(),self.df.monto.mean())
    def dashboard(self):
        fig,ax=plt.subplots(1,2,figsize=(10,4))
        sns.barplot(x='dpto',y='monto',data=self.df,ax=ax[0]); self.df.set_index('fecha').resample('M').monto.sum().plot(ax=ax[1])
        plt.tight_layout(); os.makedirs("reporte",exist_ok=True)
        fig.savefig(f"reporte/dash_{datetime.now().strftime('%Y%m%d')}.png"); plt.show()
    def run(self): self.conectar(); self.kpis(); print(self.df.corr()); self.dashboard(); self.df.to_csv("reporte/datos.csv",index=False)

# Uso
a=Analizador(); a.run()

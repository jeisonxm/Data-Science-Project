
# **Nombre: Jeison Sang Wu Mitre\
# **Cedula: 6-722-2428
# **Grupo: Grupo 09

# ! Imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import numpy as np

#! Leyendos las bases de datos
df_mat = pd.read_csv('student-mat.csv', sep=';')
df_por = pd.read_csv('student-por.csv', sep=';')

#! Creando el script que muestre mi fecha actual
from datetime import date
MyDate = date.today()
print(MyDate)

#! Creando los dataframes para cada escuela
def schoolFilter(df,school):
    return df['school'] == school

columns = ['school', 'sex', 'age', 'address', 'Pstatus', 'guardian', 'traveltime', 'studytime', 'failures', 'paid', 'internet', 'health', 'absences', 'G1','G2','G3']

GabrielPereira_mat = df_mat[schoolFilter(df_mat,'GP')].loc[:,columns].dropna()
GabrielPereira_por = df_por[schoolFilter(df_por,'GP')].loc[:,columns].dropna()

Mousinho_mat = df_mat[schoolFilter(df_mat,'MS')].loc[:,columns].dropna()
Mousinho_por = df_por[schoolFilter(df_por,'MS')].loc[:,columns].dropna()

#! Creando Grafico de Pastel para cantidad de estudiantes hombres y mujeres.

#? Colegio Gabriel Pereira
rcParams['font.family'] = 'Verdana'
fig1, axes = plt.subplots(1,2, figsize=(8,8),constrained_layout=True, )
plt.style.use('seaborn-white')
fig1.suptitle('Colegio Gabriel Pereira\n Hombres vs Mujeres', fontsize=20, weight='bold',y=0.83)

# Clase de Matematicas
axes[0].pie(data=GabrielPereira_mat,
        labels=['Mujeres','Hombres'], 
        x=GabrielPereira_mat['sex'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#FFCACA','#47B5FF']);
axes[0].set_title('Clase: Matematicas',fontsize=18, weight='roman')
axes[0].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

# Clase de Portugues
axes[1].pie(data=GabrielPereira_por,
        labels=['Mujeres','Hombres'], 
        x=GabrielPereira_por['sex'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#FFCACA','#47B5FF']);
axes[1].set_title('Clase: Portugues', fontsize=18)
axes[1].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

#? Colegio Mousinho da Silveira
fig2, axes = plt.subplots(1,2, figsize=(8,8),constrained_layout=True,)
plt.style.use('seaborn-white')
fig2.suptitle('Colegio Mousinho da Silveira\n Hombres vs Mujeres', fontsize=20, weight='bold',y=0.83)

# Clase de Matematicas
axes[0].pie(data=Mousinho_mat,
        labels=['Mujeres','Hombres'], 
        x=Mousinho_mat['sex'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#FFCACA','#47B5FF']);
axes[0].set_title('Clase: Matematicas',fontsize=18, weight='roman')
axes[0].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

# Clase de Portugues
axes[1].pie(data=Mousinho_por,
        labels=['Mujeres','Hombres'], 
        x=Mousinho_por['sex'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#FFCACA','#47B5FF']);
axes[1].set_title('Clase: Portugues', fontsize=18)
axes[1].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

#! Creando Grafico de barras que muestre la cantidad de estudiantes con la misma edad

#?  Colegio Gabriel Pereira
sns.set(
    style='darkgrid', # Definimos estilo de la grafica, su fondo, sus grillas, etc.
    palette='muted', # Definimos los colores que tendran las barras
    font='Verdana', # La fuente que usara para mostrar los numeros, etc.
    font_scale=1 # el tamano en escala de las fuentes
    )

fig3, axes = plt.subplots(1,2, figsize=(8,8),constrained_layout=True, )
fig3.suptitle('Colegio Gabriel Pereira\n Cantidad de estudiantes con misma edad', fontsize=15, weight='bold')



ax1 = sns.barplot(data=GabrielPereira_mat,
        y=GabrielPereira_mat['age'].value_counts(),
        x=GabrielPereira_mat['age'].unique(),
        ax=axes[0])
ax1.set(
    xlabel='Edades',
    ylabel='Cantidad de estudiantes',
    title='Clase: Matematicaas'
)
ax2 = sns.barplot(data=GabrielPereira_por,
        y=GabrielPereira_por['age'].value_counts(),
        x=GabrielPereira_por['age'].unique(),
        ax=axes[1])
ax2.set(
    xlabel='Edades',
    ylabel='Cantidad de estudiantes',
    title='Clase: Portuges'
)


#?  Colegio Mousinho da Silveira
fig4, axes = plt.subplots(1,2, figsize=(8,8),constrained_layout=True, )
fig4.suptitle('Colegio Mousinho da Silveira\n Cantidad de estudiantes con misma edad', fontsize=15, weight='bold')


ax1 = sns.barplot(data=Mousinho_mat,
        y=Mousinho_mat['age'].value_counts(),
        x=Mousinho_mat['age'].unique(),
        ax=axes[0])
ax1.set(
    xlabel='Edades',
    ylabel='Cantidad de estudiantes',
    title='Clase: Matematicaas'
)
ax2 = sns.barplot(data=Mousinho_por,
        y=Mousinho_por['age'].value_counts(),
        x=Mousinho_por['age'].unique(),
        ax=axes[1])
ax2.set(
    xlabel='Edades',
    ylabel='Cantidad de estudiantes',
    title='Clase: Portuges'
)

#! Sacando promedio de edad en los colegios
print(
'Promedio de Edad en Colegio Gabriel Pereira:\n',
'Clase Matematicas:',
GabrielPereira_mat['age'].mean(),
'\nClase Portugues:',
GabrielPereira_por['age'].mean(),
'-----------------------------------------------',
'\nPromedio de Edad en Colegio Moushinho da Silveira:\n',
'Clase Matematicas:',
Mousinho_mat['age'].mean(),
'\nClase Portugues:',
Mousinho_por['age'].mean(),
sep='\n'
)

#! Sacando Promedio de Notas
#? Colegio Gabriel Pereira
print(
'Promedio de Notas en Colegio Gabriel Pereira:\n',
'Clase Matematicas:',
GabrielPereira_mat.loc[:,['G1','G2','G3']].mean(),


'\nClase Portugues:',
GabrielPereira_por.loc[:,['G1','G2','G3']].mean(),
sep='\n'
)

#? Colegio Mousinho da Silveira
print(
'\nPromedio de Notas en Colegio Moushinho da Silveira:\n',
'Clase Matematicas:',
Mousinho_mat.loc[:,['G1','G2','G3']].mean(),


'\nClase Portugues:',
Mousinho_por.loc[:,['G1','G2','G3']].mean(),
sep='\n'
)

#! Creando grafico de barra horizontal para promedio de notas por periodo

fig5, axes = plt.subplots(1,2, figsize=(8,8),constrained_layout=True, )
fig5.suptitle('Colegio Gabriel Pereira\n Promedio de notas por periodo', fontsize=15, weight='bold')

ax1 = sns.barplot(data=GabrielPereira_mat,
        y=['Primer Periodo','Segundo Periodo','Tercer Periodo'],
        x=list(GabrielPereira_mat.loc[:,['G1','G2','G3']].mean()),

        ax=axes[0])
ax1.set(
    title='Clase: Matematicas',
    xlim=(9.5,12.8),
    xlabel='Promedio de notas'
)

ax2 = sns.barplot(data=GabrielPereira_por,
        y=['Primer Periodo','Segundo Periodo','Tercer Periodo'],
        x=list(GabrielPereira_por.loc[:,['G1','G2','G3']].mean()),

        ax=axes[1])
ax2.set(
    title='Clase: Portuges',
    xlim=(9.5,12.8),
    xlabel='Promedio de notas'
)


fig6, axes = plt.subplots(1,2, figsize=(8,8),constrained_layout=True,)
fig6.suptitle('Colegio Mousinho da Silveira\n Promedio de notas por periodo', fontsize=15, weight='bold')

ax1 = sns.barplot(data=Mousinho_mat,
        y=['Primer Periodo','Segundo Periodo','Tercer Periodo'],
        x=list(Mousinho_mat.loc[:,['G1','G2','G3']].mean()),

        ax=axes[0])
ax1.set(
    title='Clase: Matematicas',
    xlim=(9.5,12.8),
    xlabel='Promedio de notas'
)

ax2 = sns.barplot(data=Mousinho_por,
        y=['Primer Periodo','Segundo Periodo','Tercer Periodo'],
        x=list(Mousinho_por.loc[:,['G1','G2','G3']].mean()),

        ax=axes[1])
ax2.set(
    title='Clase: Portuges',
    xlim=(9.5,12.8),
    xlabel='Promedio de notas'
)

#! Creando columna 'Extra'
def createExra(df):
    maxAbsences = df['absences'].max()
    df['extra'] = (maxAbsences - df['absences'])/maxAbsences
    
createExra(GabrielPereira_mat)
createExra(GabrielPereira_por)
createExra(Mousinho_por)
createExra(Mousinho_mat)
createExra(df_mat)
createExra(df_por)

#! Creando columna 'approved'
def createApproved(df):
    # Utilizo el try para que este codigo solo se ejecute una vez, para evitar que las condiciones del approved se cambien por los cambios en extra.
    try:
        if len(df['approved']):
            None
    except:
        m1 = df['extra'] < 0.8
        m2 = df['G3'] < 10
        m3 = df['G3'].between(10,15)
        m4 = df['G3'] > 15
        
        df['approved'] = np.select([m1 | m2, m4| m3], [0,1], default=None)
        df['extra']=np.select([m4 & ~m1,m3 & ~m1],[0,1],default=df['extra'])
        return df

createApproved(GabrielPereira_mat)
createApproved(GabrielPereira_por)
createApproved(Mousinho_mat)
createApproved(Mousinho_por)
createApproved(df_mat)
createApproved(df_por)

#! Creando grafico de pastel que muestre la cantidad de aprobados

fig7, axes = plt.subplots(1,2, figsize=(10,10),constrained_layout=True, )
plt.style.use('seaborn-white')
fig7.suptitle('Colegio Gabriel Pereira\n Estudiantes Aprobados', fontsize=20, weight='bold',y=0.8)

# Clase de Matematicas
axes[0].pie(data=GabrielPereira_mat,
        labels=['No Aprobado','Aprobado'], 
        x=GabrielPereira_mat['approved'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#E8DFCA','#AEBDCA']);
axes[0].set_title('Clase: Matematicas',fontsize=18, weight='roman')
axes[0].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

axes[1].pie(data=GabrielPereira_por,
        labels=['No Aprobado','Aprobado'], 
        x=GabrielPereira_por['approved'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#E8DFCA','#AEBDCA']);

axes[1].set_title('Clase: Portugues',fontsize=18, weight='roman')
axes[1].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

# 
fig8, axes = plt.subplots(1,2, figsize=(10,10),constrained_layout=True,)
plt.style.use('seaborn-white')
fig8.suptitle('Colegio Mousinho da Silveira\n Estudiantes Aprobados', fontsize=20, weight='bold',y=0.8)

# Clase de Matematicas
axes[0].pie(data=Mousinho_mat,
        labels=['No Aprobado','Aprobado'], 
        x=Mousinho_mat['approved'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#E8DFCA','#AEBDCA']);
axes[0].set_title('Clase: Matematicas',fontsize=18, weight='roman')
axes[0].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

axes[1].pie(data=Mousinho_por,
        labels=['No Aprobado','Aprobado'], 
        x=Mousinho_por['approved'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#E8DFCA','#AEBDCA']);

axes[1].set_title('Clase: Portugues',fontsize=18, weight='roman')
axes[1].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

# 
fig9, axes = plt.subplots(1,2, figsize=(10,10),constrained_layout=True, )
plt.style.use('seaborn-white')
fig9.suptitle('General\n Estudiantes Aprobados', fontsize=20, weight='bold',y=0.8)

# Clase de Matematicas
axes[0].pie(data=df_mat,
        labels=['No Aprobado','Aprobado'], 
        x=df_mat['approved'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#E8DFCA','#AEBDCA']);
axes[0].set_title('Clase: Matematicas',fontsize=18, weight='roman')
axes[0].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))

axes[1].pie(data=df_por,
        labels=['No Aprobado','Aprobado'], 
        x=df_por['approved'].value_counts(),
        autopct='%1.1f%%',
        colors = ['#E8DFCA','#AEBDCA']);

axes[1].set_title('Clase: Portugues',fontsize=18, weight='roman')
axes[1].legend(fontsize=14,loc='upper left',bbox_to_anchor=(0.85,0.9))


#! Creando un pdf con todos los graficos

from matplotlib.backends.backend_pdf import PdfPages
figs = [fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9]

pdf = PdfPages(f"Graficas Resultado - {MyDate} .pdf")
for fig in figs:
    pdf.savefig(fig)
pdf.close()

#! Creando el resultado.csv con todas los dataframes trabajados.
Result = pd.concat([GabrielPereira_mat,GabrielPereira_por,Mousinho_mat,Mousinho_por],keys=('GP_Mat','GP_Por','MS_Mat','MS_Por'))
Result.to_csv(f'Resultados-{MyDate}')



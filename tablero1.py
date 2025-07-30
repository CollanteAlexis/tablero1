import pandas as pd
import numpy as np
import streamlit as st


st.set_page_config(layout="centered", page_title="Talento_Tech2", page_icon=":smile:")

t1, t2 = st.columns([0.3, 0.7])
t1.image('TT1.jpg')#, width = 200)
t2.title('Tablero de prueba')
t2.markdown('**tel:** 3207996687 | **email:** alexis.collante@udea.edu.co')

campanhas_df = pd.read_csv('Campanhas.csv', encoding='latin-1', sep=';')
audiencias_df = pd.read_csv('Audiencias.csv', encoding='latin-1', sep=';')
metricas_df = pd.read_csv('Metricas.csv', encoding='latin-1', sep=';')

steps = st.tabs(['Pestaña 1', 'Pestaña 2', 'Pestaña 3'])
with steps[0]:
    st.markdown('# **Pestaña 1**')
    
    st.image('TT2.jpg', width=10000)
    
    df = pd.DataFrame({'Nombre': ['Adán', 'Eva'], 
                      'Edad': [30, 28],
                      'Ciudad': ['Edén', 'Edén']})
    st.table(df)
    st.dataframe(df)
    
    campaña_select = st.selectbox('Selecciona una campaña:', campanhas_df['ID_Campana'], help = 'Selecciona una campaña para ver sus detalles')
    
    st.markdown('##### Métricas de la Campaña seleccionada')
    
    # metricas_df = st.dataframe(metricas_df)
    m1, m2, m3 = st.columns([1, 1, 1])
    id1 = metricas_df[(metricas_df['ID_Campana'] == campaña_select)|(metricas_df['ID_Campana'] == 1)]
    id2 = metricas_df[metricas_df['ID_Campana'] == campaña_select]
    

    m1.metric(label = "Métrica 1", value = sum(id1['Rebotes']), delta = 'Total de rebotes', delta_color = 'inverse')
    m1.dataframe(id1[['ID_Metrica', 'Rebotes']])
    m2.metric(label = "Métrica 2", value = round(np.mean(id1['Clics']), 2), delta = 'Promedio de Clics', delta_color = 'inverse')
    m2.dataframe(id1[['ID_Metrica', 'Clics']]) 

    m3.metric(label = "Métrica 3", value = sum(id1['Clics']), delta = 'Total de Impresiones', delta_color = 'normal')
    m3.dataframe(id1[['ID_Metrica', 'Impresiones']]) 


with steps[1]:
    st.markdown('# **Pestaña 2**')
    
    n = st.button('Botón de prueba')
    if n:
        st.write('¡Botón presionado!')
    
    campana = st.selectbox('Selecciona un ID de campaña:', campanhas_df['ID_Campana'], help = 'Selecciona una campaña para ver sus métricas')
    id3 = metricas_df[(metricas_df['ID_Campana'] == campana)|(metricas_df['ID_Campana'] == 1)]
    
    varx = st.selectbox('Selecciona una métrica de la campaña:', id3.ID_Metrica, help = 'Selecciona una métrica para gráficar')
    id4 = metricas_df[(metricas_df['ID_Metrica'] == varx)]#|(metricas_df['ID_Campana'] == 1)]
    
    fig, ax = pd.subplots()
    
    ax = pd.scatterplot(
    data=id4,
    x='ID_Metrica',
    y='Conversiones',
    hue='ID_Campana'
    )
    
    ax.set_xlabel('Métrica')
    
    pd.ylim(0, 20)
    pd.xlim(0, 80)
    
    st.pyplot(fig)
    
with steps[2]:
    st.markdown('# **Pestaña 3**')
    
    st.selectbox('Selecciona una opción:', ['Opción 1', 'Opción 2', 'Opción 3'])
    
    st.select_slider('Selecciona un rango:',
                     options=np.arange(0, 101, 1))

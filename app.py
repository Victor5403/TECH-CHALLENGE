########### Importação das bibliotecas ########### 
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

########### Configuração do layout ########### 
st.set_page_config(
    page_title="Portal de Preços do Petróleo",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

# Opções de navegação
navegacao = ['Portal', 'Dashboard', 'Previsões']
pagina = st.sidebar.selectbox('Navegação', navegacao)

########### Carregar dados ########### 
df_streamlit = pd.read_csv('df_streamlit.csv')

########### Funções utilitárias ########### 
def calcula_ultimo_valor_atual(df):
    """Calcula o último valor de fechamento, data e variação percentual."""
    return df['preco'].iloc[-1], df['data'].iloc[-1], df['variacao_%'].iloc[-1]

def calcula_maior_menor_valor(df):
    """Calcula o maior e menor valor de fechamento e as respectivas datas."""
    maior_valor = df['preco'].max()
    maior_valor_data = df[df['preco'] == maior_valor]['data'].max()
    menor_valor = df['preco'].min()
    menor_valor_data = df[df['preco'] == menor_valor]['data'].max()
    return maior_valor, maior_valor_data, menor_valor, menor_valor_data

def calcula_valor_medio(df):
    """Calcula o valor médio anual."""
    return df['preco'].mean().round(2)

def aplica_modelo(df, lags=5):
    """Treina o modelo de previsão e retorna resultados."""
    base_modelo = df[['data', 'preco']].sort_values(by='data').reset_index(drop=True)
    for lag in range(1, lags + 1):
        base_modelo[f'preco_lag_{lag}'] = base_modelo['preco'].shift(lag)
    base_modelo.dropna(inplace=True)

    X = base_modelo[[f'preco_lag_{lag}' for lag in range(1, lags + 1)]]
    y = base_modelo['preco']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False, random_state=42)

    reg_gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42, loss='squared_error')
    reg_gb.fit(X_train, y_train)

    previsoes = reg_gb.predict(X_test)
    MSE = mean_squared_error(y_test, previsoes)
    MAE = mean_absolute_error(y_test, previsoes)

    ultimo_valor = X.iloc[-1].values.reshape(1, -1)
    valores_previstos = []
    for _ in range(lags):
        proximo_valor = reg_gb.predict(ultimo_valor)[0]
        valores_previstos.append(proximo_valor)
        ultimo_valor = np.roll(ultimo_valor, -1)
        ultimo_valor[0, -1] = proximo_valor

    datas_previstas = pd.date_range(base_modelo['data'].iloc[-1], periods=lags + 1)[1:]
    base_prevista = pd.DataFrame({
        'datas_previstas': datas_previstas,
        'valores_previstos': valores_previstos
    })

    return base_modelo, base_prevista, MSE, MAE

########### Configuração das páginas ########### 
if pagina == 'Portal':
    st.header('Portal de Preços do Petróleo')
    st.subheader('Definição')
    st.write('O Portal de Preços do Petróleo é o aplicativo de gerenciamento do preço bruto do barril de petróleo brent.')
    st.subheader('Dados')
    st.write('Os dados foram obtidos no site do Instituto de Pesquisa Econômica Aplicada (Ipea).')
    st.write('Acesse os dados [aqui](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view).')
    st.subheader('O que é o Ipea?')
    st.write('O Instituto de Pesquisa Econômica Aplicada (Ipea) é uma fundação pública federal.')
    st.subheader('O que é o Petróleo Brent?')
    st.write('Produzido no Mar do Norte (Europa), o Brent é um tipo de petróleo bruto que serve como benchmark internacional.')
    st.subheader('Autores')
    st.write('Victor Ventura' , 'Nicolas Ventura')

elif pagina == 'Dashboard':
    st.header('Evolução Preço Bruto do Petróleo Brent (FOB)')
    with st.sidebar:
        lista_ano = sorted(df_streamlit['ano'].unique())
        ano_selecionado = st.selectbox('Selecione o Ano', lista_ano, index=len(lista_ano) - 1)
        df_ano_selecionado = df_streamlit[df_streamlit['ano'] == ano_selecionado].sort_values(by='data')

    col = st.columns((2.5, 8))

    with col[0]:
        st.markdown('#### Último Fechamento')
        valor, data, delta = calcula_ultimo_valor_atual(df_ano_selecionado)
        st.metric(label=data, value=f'{valor} US$', delta=f'{delta} %')

        st.markdown('#### Maior Valor Fechado')
        maior_valor, maior_data, _, _ = calcula_maior_menor_valor(df_ano_selecionado)
        st.metric(label=maior_data, value=f'{maior_valor} US$')

        st.markdown('#### Menor Valor Fechado')
        _, _, menor_valor, menor_data = calcula_maior_menor_valor(df_ano_selecionado)
        st.metric(label=menor_data, value=f'{menor_valor} US$')

        st.markdown('#### Valor Médio Anual')
        valor_medio = calcula_valor_medio(df_ano_selecionado)
        st.metric(label=str(ano_selecionado), value=f'{valor_medio} US$')

    with col[1]:
        st.markdown('#### Preço Histórico (US$)')
        df_ano_selecionado_grafico = df_ano_selecionado.rename(columns={'data': 'Data', 'preco': 'Preço (US$)'})
        st.line_chart(df_ano_selecionado_grafico, x='Data', y='Preço (US$)', use_container_width=True)

        st.markdown('#### Variação Percentual (%)')
        df_ano_selecionado_grafico = df_ano_selecionado.rename(columns={'data': 'Data', 'variacao_%': 'Variação (%)'})
        st.line_chart(df_ano_selecionado_grafico, x='Data', y='Variação (%)', use_container_width=True)

elif pagina == 'Previsões':
    st.header('Previsões')
    col = st.columns((3, 7))

    with col[0]:
        st.markdown('#### Datas e Valores Previstos')
        numero_lags = st.slider("Selecione quantos dias de previsão deseja obter:", 5, 30, 5)
        base_modelo, df_previsao, erro_mse, erro_mae = aplica_modelo(df_streamlit, numero_lags)

        st.table(df_previsao.rename(columns={'datas_previstas': 'Data Prevista', 'valores_previstos': 'Preço Previsto (US$)'}))

    with col[1]:
        st.markdown('#### Evolução dos Valores Previstos')
        st.line_chart(df_previsao, x='datas_previstas', y='valores_previstos', use_container_width=True)


# TECH-CHALLENGE - FASE 4 - APLICAÇÃO COM STREAMLIT
# Tópicos
O Problema
Fomos contratados por um consultoria para analisar os dados de preço do petróleo brent. Um grande cliente do segmento pediu que a consultoria desenvolvesse um dashboard interativo e que gere insights relevantes para a tomada de decisão. Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo.

# Objetivo
Nosso objetivo consiste em:

Criar um dashboard interativo;
Gerar um strorytelling que traga insights relevantes sobre a variação do preço do petróleo brent, como situações geopolíticas, crises econômicas, demanda global por energia e etc;
Criar um modelo de Machine Learning que faça a previsão do preço do petróleo brent diariamente;
Criar um plano para fazer o deploy do modelo em produção;
Gerar um MVP (Minimum Viable Product) do modelo em produção por meio do Streamlit.
# Introdução
# O que é o Ipea ?¶
O Instituto de Pesquisa Econômica Aplicada (Ipea) é uma fundação pública federal vinculada ao Ministério do Planejamento e Orçamento. As atividades de pesquisa fornecem suporte técnico e institucional para as ações governamentais a fim de formular e reformular políticas públicas e programas de desenvolvimento. O Ipea disponibiliza seus trabalhos por meio de publicações eletrônicas, impressas, e eventos.

# O que é o Petróleo Brent ?
Produzido no Mar do Norte (Europa), Brent é uma classe de petróleo bruto que serve como benchmark para o preço internacional de diferentes tipos de petróleo. Neste caso, é valorado no chamado preço FOB (free on board), que não inclui despesa de frete e seguro no preço.

# Obtenção dos Dados
Os dados foram obtidos no site do Instituto de Pesquisa Econômica Aplicada (Ipea) e podem ser acessados por meio do link:

http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view

# Apresentação dos Dados
Nesta seção iremos observar de forma geral os dados presentes no dataset. Assim, teremos uma noção maior dos dados que possuímos e como eles nos são apresentados.

# Visualização e Tratamento dos Dados
Aqui realizaremos o tratamento dos dados, verificando a presença de dados missings, correções e eliminações de dados.

# Análise Exploratória dos Dados
Este tópico contém a análise exploratória do comportamento dos nossos dados e das relações entre as variáveis. Realização da análise de outliers, estatísticas descritivas e qual o nosso intervalo temporal.

# Análise de Séries Temporais
Nesta seção iremos analisar nossos dados como séries temporais, realizando toda a decomposição da série e verificando sua estacionaridade por meio da regra de Dickey-Fuller.

# Construção do Modelo
Após a análise, criaremos os modelos que queremos testas e realizaremos uma comparação entre eles a fim de verificar qual performa melhor.

Dentre os modelos estão:

Modelo ARIMA
Modelo Gradient Boosting
Base para Aplicação no Streamlit
Iremos criar uma base de dados tratada para facilitar a aplicação no Streamlit.

# Referências
INSTITUTO DE PESQUISA ECONÔMICA APLICADA. Quem somos. Disponível em: https://www.ipea.gov.br/portal/coluna-3/institucional-sep/quem-somos. Acesso em: 01 de maio de 2024.

BRASIL DE FATO. Pandemia da covid-19 gera maior crise do mercado mundial de petróleo em 30 anos. Disponível em: https://www.brasildefato.com.br/2020/04/08/pandemia-da-covid-19-gera-maior-crise-do-mercado-mundial-de-petroleo-em-30-anos. Acesso em: 02 de maio de 2024.

SEGOVIA SPADINI, Allan. "Séries temporais e suas aplicações": Atualizado em 22/01/2021. Disponível em: https://www.alura.com.br/artigos/series-temporais-e-suas-aplicacoes. Acesso em: 15 de janeiro de 2024.

FERNANDES CUNHA, Ana Raquel. "Predicting stock values with machine learning and deep learning algorithms". Disponível em: https://medium.com/@anaraquel.fiap/predicting-stock-values-with-machine-learning-and-deep-learning-algorithms-5eb028892888. Acesso em: 24 de janeiro de 2024.

SILVA, Jonhy. Uma breve introdução ao algoritmo de Machine Learning Gradient Boosting utilizando a biblioteca Scikit-Learn. Atualizado em: 22 de junho de 2020. Disponível em: https://medium.com/equals-lab/uma-breve-introdu%C3%A7%C3%A3o-ao-algoritmo-de-machine-learning-gradient-boosting-utilizando-a-biblioteca-311285783099. Acesso em: 04 de maio de 2024.

FILIPE, Kauã. Introdução à Feature Engineering para Previsão com Séries Temporais. Atualizado em: 09 de outubro de 2022. Disponível em: https://medium.com/turing-talks/introdu%C3%A7%C3%A3o-%C3%A0-feature-engineering-para-previs%C3%A3o-com-s%C3%A9ries-temporais-bf8bd3d0397d#:~:text=Utilizamos%20lag%20time%20features%20quando,de%20a%C3%A7%C3%B5es%20de%20uma%20empresa. Acesso em: 04 de maio de 2024.

# Técnicas e Tecnologias Utilizadas
Python

Jupyter Notebook

Time Series

ARIMA

Gradient Boosting

Machine Learning

# Autores

Victor Ventura 

Nicolas Ventura

# TECH-CHALLENGE - FASE 4 - APLICAÇÃO COM STREAMLIT
# Tópicos
O Problema
Fomos contratados por uma consultoria para analisar os dados de preço do petróleo Brent. Um importante cliente do setor solicitou o desenvolvimento de um dashboard interativo que forneça insights valiosos para apoiar a tomada de decisões estratégicas. Além disso, foi requisitado o desenvolvimento de um modelo de Machine Learning para realizar previsões (forecasting) do preço do petróleo, visando otimizar a gestão e os planos futuros do cliente.

# Objetivo
Nosso objetivo consiste em:

Criar um dashboard interativo;
Gerar um strorytelling que traga insights relevantes sobre a variação do preço do petróleo brent, como situações geopolíticas, crises econômicas, demanda global por energia e etc;
Criar um modelo de Machine Learning que faça a previsão do preço do petróleo brent diariamente;
Criar um plano para fazer o deploy do modelo em produção;
Gerar um MVP (Minimum Viable Product) do modelo em produção por meio do Streamlit.
# Introdução
# O que é o Ipea ?
O Instituto de Pesquisa Econômica Aplicada (Ipea) é uma fundação pública federal vinculada ao Ministério do Planejamento e Orçamento, que desempenha um papel essencial no suporte técnico e institucional às ações governamentais. Sua missão é contribuir para a formulação e aprimoramento de políticas públicas e programas de desenvolvimento por meio de pesquisas e análises detalhadas. O Ipea dissemina seu trabalho por meio de publicações eletrônicas, impressas e da realização de eventos, promovendo o acesso a informações de alta relevância para gestores, acadêmicos e o público em geral.

# O que é o Petróleo Brent ?
O petróleo Brent, produzido no Mar do Norte, é um benchmark importante para o preço internacional do petróleo. Ele é avaliado pelo preço FOB (free on board), que não inclui despesas de frete e seguro. O Brent serve como referência para a precificação de diversos tipos de petróleo no mercado global.

# Obtenção dos Dados
Os dados utilizados neste trabalho foram obtidos a partir do site do Instituto de Pesquisa Econômica Aplicada (Ipea). Eles podem ser acessados diretamente por meio do seguinte link:

http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view

Essa fonte garante a confiabilidade e a relevância das informações para análises econômicas aprofundadas.

# Apresentação dos Dados
Nesta seção, vamos realizar uma análise geral dos dados presentes no conjunto de dados. O objetivo é entender melhor as informações disponíveis, explorar suas características e identificar como os dados são estruturados e apresentados. Isso nos ajudará a obter uma visão mais clara sobre o conteúdo do dataset e como ele pode ser utilizado para análise posterior.

# Visualização e Tratamento dos Dados
Nesta etapa, vamos realizar o tratamento dos dados, identificando e lidando com a presença de valores ausentes (missing data). Faremos as correções necessárias e, quando apropriado, eliminaremos registros ou variáveis que possam comprometer a qualidade da análise. O objetivo é garantir que os dados estejam limpos e prontos para a modelagem ou análise subsequente.

# Análise Exploratória dos Dados
Este tópico aborda a análise exploratória dos dados, com foco no comportamento das variáveis e nas relações entre elas. Inclui a identificação de outliers, a realização de estatísticas descritivas e a definição do intervalo temporal dos dados, visando entender melhor a estrutura e as características do conjunto de dados.

# Análise de Séries Temporais
Nesta seção, realizaremos a análise dos dados como séries temporais, conduzindo a decomposição da série para entender seus componentes e avaliar sua estacionaridade utilizando o teste de Dickey-Fuller. Essa análise permitirá identificar tendências, sazonalidades e comportamentos que possam influenciar a modelagem e previsão da série temporal.

# Construção do Modelo
Após a análise dos dados, iremos desenvolver e treinar os modelos que serão testados. Em seguida, realizaremos uma comparação entre as diferentes abordagens para avaliar qual delas apresenta o melhor desempenho, com base em métricas de avaliação adequadas. Isso nos permitirá identificar o modelo mais eficaz para o problema em questão.

Dentre os modelos estão:

Modelo ARIMA
Modelo Gradient Boosting
Base para Aplicação no Streamlit
Iremos criar uma base de dados tratada para facilitar a aplicação no Streamlit.

# Referências

INSTITUTO DE PESQUISA ECONÔMICA APLICADA. Quem somos. Disponível em: https://www.ipea.gov.br/portal/coluna-3/institucional-sep/quem-somos. Acesso em: 01 de Outubro de 2024.

BRASIL DE FATO. Pandemia da covid-19 gera maior crise do mercado mundial de petróleo em 30 anos. Disponível em: https://www.brasildefato.com.br/2020/04/08/pandemia-da-covid-19-gera-maior-crise-do-mercado-mundial-de-petroleo-em-30-anos. Acesso em: 02 de maio de 2024.

SEGOVIA SPADINI, Allan. "Séries temporais e suas aplicações": Atualizado em 22/01/2021. Disponível em: https://www.alura.com.br/artigos/series-temporais-e-suas-aplicacoes. Acesso em: 15 de Outubro de 2024.

FERNANDES CUNHA, Ana Raquel. "Predicting stock values with machine learning and deep learning algorithms". Disponível em: https://medium.com/@anaraquel.fiap/predicting-stock-values-with-machine-learning-and-deep-learning-algorithms-5eb028892888. Acesso em: 24 de Outubro de 2024.

SILVA, Jonhy. Uma breve introdução ao algoritmo de Machine Learning Gradient Boosting utilizando a biblioteca Scikit-Learn. Atualizado em: 22 de junho de 2020. Disponível em: https://medium.com/equals-lab/uma-breve-introdu%C3%A7%C3%A3o-ao-algoritmo-de-machine-learning-gradient-boosting-utilizando-a-biblioteca-311285783099. Acesso em: 04 de Outubro de 2024.

FILIPE, Kauã. Introdução à Feature Engineering para Previsão com Séries Temporais. Atualizado em: 09 de outubro de 2022. Disponível em: https://medium.com/turing-talks/introdu%C3%A7%C3%A3o-%C3%A0-feature-engineering-para-previs%C3%A3o-com-s%C3%A9ries-temporais-bf8bd3d0397d#:~:text=Utilizamos%20lag%20time%20features%20quando,de%20a%C3%A7%C3%B5es%20de%20uma%20empresa. Acesso em: 04 de Outubro de 2024.

# Técnicas e Tecnologias Empregadas

Python

Jupyter Notebook

Time Series

ARIMA

Gradient Boosting

Machine Learning

# Autores

Victor Ventura dos Santos

Nicolas Ventura dos Santos

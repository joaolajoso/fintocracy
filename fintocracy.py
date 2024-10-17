#fintocracy
import streamlit as st
import yfinance as yf
import datetime as dt

# Função para simular o retorno de um investimento em ações
def simulacao_investimento_acao(ticker, valor_investido, data_inicial, data_final):
    # Obter os dados históricos do ticker
    dados = yf.download(ticker, start=data_inicial, end=data_final)
    
    # Verificar se os dados estão disponíveis
    if not dados.empty:
        preco_inicial = dados['Close'].iloc[0]
        preco_final = dados['Close'].iloc[-1]
        
        # Cálculo do retorno
        retorno = (preco_final / preco_inicial) * valor_investido
        lucro = retorno - valor_investido
        return retorno, lucro
    else:
        return None, None

# Função para simular o planejamento de aposentadoria
def simulacao_aposentadoria(valor_atual, contribuicao_mensal, anos, taxa_rendimento):
    meses = anos * 12
    saldo_final = valor_atual
    for i in range(meses):
        saldo_final += contribuicao_mensal
        saldo_final *= (1 + (taxa_rendimento / 100) / 12)  # rendimento mensal
    return saldo_final

# Função para simular a gestão de dívidas
def simulacao_divida(valor_divida, taxa_juros, pagamento_mensal):
    meses = 0
    while valor_divida > 0:
        juros = (taxa_juros / 100 / 12) * valor_divida
        valor_divida += juros
        valor_divida -= pagamento_mensal
        meses += 1
        if meses > 1000:  # Limitar a simulação para evitar loop infinito
            break
    return meses

# Função principal para simulações complexas
def simulacoes_complexas():
    st.header("Simulações Complexas de Investimento, Aposentadoria e Dívidas")

    # Simulação de Investimento em Ações
    st.subheader("Simulação de Investimento em Ações")
    ticker = st.text_input("Digite o código da ação (ex: AAPL, TSLA)", value="AAPL")
    valor_investido = st.number_input("Quanto você deseja investir? (em euros)", min_value=100.0, step=100.0)
    data_inicial = st.date_input("Data de início", value=dt.date(2023, 1, 1))
    data_final = st.date_input("Data final", value=dt.date(2023, 12, 31))

    if st.button("Simular Investimento"):
        retorno, lucro = simulacao_investimento_acao(ticker, valor_investido, data_inicial, data_final)
        if retorno:
            st.success(f"O valor final do seu investimento seria de {retorno:.2f} euros, com um lucro de {lucro:.2f} euros.")
        else:
            st.error("Dados da ação não disponíveis. Tente outro ticker ou intervalo de datas.")

    # Simulação de Planejamento de Aposentadoria
    st.subheader("Simulação de Planejamento de Aposentadoria")
    valor_atual = st.number_input("Quanto você já tem poupado? (em euros)", min_value=0.0, step=100.0)
    contribuicao_mensal = st.number_input("Quanto você pode contribuir por mês? (em euros)", min_value=0.0, step=50.0)
    anos = st.slider("Quantos anos até a aposentadoria?", min_value=1, max_value=50)
    taxa_rendimento = st.slider("Taxa de rendimento anual esperada (%)", min_value=0.0, max_value=15.0, step=0.1)

    if st.button("Simular Aposentadoria"):
        saldo_final = simulacao_aposentadoria(valor_atual, contribuicao_mensal, anos, taxa_rendimento)
        st.success(f"Após {anos} anos, você terá acumulado {saldo_final:.2f} euros.")

    # Simulação de Gestão de Dívidas
    st.subheader("Simulação de Gestão de Dívidas")
    valor_divida = st.number_input("Qual o valor total da dívida? (em euros)", min_value=100.0, step=100.0)
    taxa_juros = st.slider("Taxa de juros anual (%)", min_value=0.0, max_value=30.0, step=0.5)
    pagamento_mensal = st.number_input("Quanto você pode pagar por mês? (em euros)", min_value=0.0, step=50.0)

    if st.button("Simular Pagamento da Dívida"):
        meses = simulacao_divida(valor_divida, taxa_juros, pagamento_mensal)
        if meses < 1000:
            st.success(f"Você pagará sua dívida em {meses} meses.")
        else:
            st.error("Com este pagamento mensal, a dívida não será quitada. Tente aumentar o valor do pagamento.")

# Função principal da aplicação
def main():
    st.title("Plataforma Gamificada de Educação Financeira - Simulações Avançadas")

    # Menu de navegação
    menu = ["Simulações de Investimentos e Finanças Pessoais", "Quiz Financeiro", "Progresso e Recompensas"]
    escolha = st.sidebar.selectbox("Selecione uma Opção", menu)

    # Simulações complexas de finanças
    if escolha == "Simulações de Investimentos e Finanças Pessoais":
        simulacoes_complexas()
    elif escolha == "Quiz Financeiro":
        # Chamando a função do quiz (pode ser implementado conforme o código anterior)
        quiz_interativo()
    elif escolha == "Progresso e Recompensas":
        # Chamando a função de progresso e recompensas (do código anterior)
        progresso_e_recompensas(nivel_atual=1)

if __name__ == '__main__':
    main()

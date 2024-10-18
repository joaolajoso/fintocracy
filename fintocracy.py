#fintocracy
import streamlit as st
import yfinance as yf
import datetime as dt
from groq_qa_generator import groq_qa
from groq import Groq
import os


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

# Função para simular o planejamento de Reforma
def simulacao_Reforma(valor_atual, contribuicao_mensal, anos, taxa_rendimento):
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
    st.header("Simulações Complexas de Investimento, Reforma e Dívidas")

    # Simulação de Investimento em Ações
    st.subheader("Simulação de Investimento em Ações")
    lista = ["AAPL", "NVDA", "TSLA", "Digite o código da ação"]
    ticker = st.selectbox("Selecione uma Opção", lista)
    if ticker == "Digite o código da ação": ticker = st.textinput("Digite o código da ação (ex: AAPL, TSLA)", value="AAPL")
    valor_investido = st.number_input("Quanto você deseja investir? (em euros)", min_value=100.0, step=100.0)
    data_inicial = st.date_input("Data de início", value=dt.date(2023, 1, 1))
    data_final = st.date_input("Data final", value=dt.date(2023, 12, 31))

    if st.button("Simular Investimento"):
        retorno, lucro = simulacao_investimento_acao(ticker, valor_investido, data_inicial, data_final)
        if retorno:
            st.success(f"O valor final do seu investimento seria de {retorno:.2f} euros, com um lucro de {lucro:.2f} euros.")
        else:
            st.error("Dados da ação não disponíveis. Tente outro ticker ou intervalo de datas.")

    # Simulação de Planejamento de Reforma
    st.subheader("Simulação de Planejamento de Reforma")
    valor_atual = st.number_input("Quanto você já tem poupado? (em euros)", min_value=0.0, step=100.0)
    contribuicao_mensal = st.number_input("Quanto você pode contribuir por mês? (em euros)", min_value=0.0, step=50.0)
    anos = st.slider("Quantos anos até a Reforma?", min_value=1, max_value=50)
    taxa_rendimento = st.slider("Taxa de rendimento anual esperada (%)", min_value=0.0, max_value=15.0, step=0.1)

    if st.button("Simular Reforma"):
        saldo_final = simulacao_Reforma(valor_atual, contribuicao_mensal, anos, taxa_rendimento)
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

#Função para calcular feedback financeiro com base em uma simulação
def calcular_feedback(acao, valor):
    if acao == 'Investir':
        retorno = valor * 1.1  # Simulação simples de 10% de retorno
        feedback = f"Bom trabalho! Você investiu {valor} e agora tem {retorno}."
    elif acao == 'Poupar':
        retorno = valor * 1.05  # Simulação de 5% de retorno
        feedback = f"Ótima escolha! Você poupou {valor} e agora tem {retorno}."
    elif acao == 'Gastar':
        retorno = valor * 0.9  # Simulação de perda de 10%
        feedback = f"Cuidado! Você gastou {valor} e agora perdeu parte, ficando com {retorno}."
    else:
        retorno = valor
        feedback = f"Nenhuma ação foi tomada."
    return retorno, feedback

# Função para simulação de orçamento
def simulacao_orcamento():
    st.header("Simulação de Orçamento")
    st.write("Gerencie seu orçamento mensal e veja os impactos de suas decisões financeiras.")

    # Inputs do usuário
    valor = st.number_input("Quanto você deseja gerenciar? (em euros)", min_value=0, step=100)
    acao = st.selectbox("Escolha uma ação financeira:", ['Investir', 'Poupar', 'Gastar'])

    # Calcular feedback
    if st.button("Executar Ação"):
        saldo, feedback = calcular_feedback(acao, valor)
        st.success(feedback)
        st.write(f"Seu saldo atual: {saldo} euros")

# Função para atualizar o nível do usuário com base na pontuação
def atualizar_nivel(pontuacao):
    if pontuacao <= 1:
        return 1  # Nível 1 - Iniciante
    elif pontuacao == 2:
        return 2  # Nível 2 - Aprendiz
    elif pontuacao == 3:
        return 3  # Nível 3 - Intermediário
    elif pontuacao == 4:
        return 4  # Nível 4 - Avançado
    else:
        return 5  # Nível 5 - Expert

# Função para exibir o nível atual no topo de todas as páginas
def mostrar_nivel_topo(nivel_atual):
    st.markdown(f"### Seu nível atual: **Nível {nivel_atual}**")

# Função para simular o progresso e recompensas
def progresso_e_recompensas():
    st.header("Seu Progresso e Recompensas")
    nivel_atual = st.session_state['nivel']

    # Definir metas para cada nível
    niveis = {
        1: "Iniciante: Entendendo os conceitos básicos de finanças.",
        2: "Aprendiz: Ganhando conhecimento sobre poupança e orçamento.",
        3: "Intermediário: Compreendendo investimentos e gestão de dívidas.",
        4: "Avançado: Fazendo boas decisões financeiras com confiança.",
        5: "Expert: Mestre em finanças pessoais!"
    }

    st.write(f"Você está no **Nível {nivel_atual}**!")
    st.write(f"Descrição do seu nível: {niveis[nivel_atual]}")

    # Mostrar recompensas com base no nível
    if nivel_atual == 1:
        st.write("Objetivo: Completar o quiz para ganhar o Nível 2.")
    elif nivel_atual == 2:
        st.write("Objetivo: Continuar aprendendo para atingir o Nível 3.")
    elif nivel_atual == 3:
        st.write("Objetivo: Investimentos e gestão de dívidas são as suas próximas metas.")
    elif nivel_atual == 4:
        st.write("Objetivo: Alcance o nível máximo de especialista financeiro.")
    elif nivel_atual == 5:
        st.write("Parabéns! Você atingiu o nível máximo e se tornou um especialista em finanças pessoais!")

# Função de quiz interativo com níveis
def quiz_interativo(nivel_atual):
    st.header("Quiz de Educação Financeira")
    st.write("Responda as perguntas para testar seu conhecimento e subir de nível.")

    # Novas perguntas do quiz
    perguntas = {
        "O que é um orçamento?": ["Plano para gastar dinheiro", "Ferramenta de investimento", "Uma poupança"],
        "Qual é a melhor maneira de evitar dívidas?": ["Gastar mais do que ganha", "Poupar dinheiro", "Fazer empréstimos"],
        "Qual das seguintes opções é considerada um bom investimento?": ["Jogo de azar", "Ações", "Compras impulsivas"],
        "O que é um fundo de emergência?": ["Dinheiro para emergências", "Dinheiro para gastar em férias", "Investimento em ações"],
        "Qual é a principal função de um cartão de crédito?": ["Gastar sem limites", "Fazer compras e pagar depois", "Aumentar o saldo bancário"],
        "O que é diversificação de investimentos?": ["Investir em diferentes tipos de ativos", "Colocar todo o dinheiro em um único investimento", "Gastar em várias coisas"],
        "Qual é a fórmula básica para calcular juros compostos?": ["Principal * (1 + taxa)^tempo", "Principal / taxa", "Principal - tempo"],
        "O que é o prazo de carência em um empréstimo?": ["Período antes de começar a pagar", "Taxa de juros", "A data de vencimento final"],
        "O que significa planejar a aposentadoria?": ["Economizar ao longo da vida para o futuro", "Investir em ações de curto prazo", "Gastar todo o dinheiro na aposentadoria"],
        "Qual é a importância de um planejamento de dívida?": ["Evitar pagar juros excessivos", "Aumentar as dívidas", "Ignorar os pagamentos de juros"]
    }

    respostas_corretas = [
        "Plano para gastar dinheiro", 
        "Poupar dinheiro", 
        "Ações", 
        "Dinheiro para emergências", 
        "Fazer compras e pagar depois",
        "Investir em diferentes tipos de ativos",
        "Principal * (1 + taxa)^tempo",
        "Período antes de começar a pagar",
        "Economizar ao longo da vida para o futuro",
        "Evitar pagar juros excessivos"
    ]

    # Coletar respostas do usuário
    pontuacao = 0
    for i, (pergunta, opcoes) in enumerate(perguntas.items()):
        resposta = st.radio(pergunta, opcoes)
        if resposta == respostas_corretas[i]:
            pontuacao += 1

    # Exibir pontuação final e atualizar o nível
    if st.button("Submeter Respostas"):
        st.success(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
        novo_nivel = atualizar_nivel(pontuacao)
        st.session_state['nivel'] = novo_nivel
        st.balloons()
        st.success(f"Você subiu para o Nível {novo_nivel}!")


# Function to generate questions dynamically using Groq API
# Use Groq client
def generate_questions():
    # Configure your Groq model name
    GROQ_LLAMA_MODEL_FULLNAME = "llama-3.1-70b-versatile"
    markdown_content = """
    # Financial Literacy
    
    Financial literacy is the ability to understand and effectively use various financial skills, including personal financial management, budgeting, and investing.
    """
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        raise ValueError("API key não encontrada. Certifique-se de que a variável de ambiente GROQ_API_KEY está definida.")

    client = Groq(api_key=api_key)

    prompt_pagination = (
        "Gere perguntas de múltipla escolha sobre literacia financeira, "
        "usando o seguinte conteúdo como referência: \n\n"
        f"{markdown_content}\n"
        "Por favor, forneça 10 perguntas, cada uma acompanhada das suas opções e da resposta correta. "
        "As perguntas devem estar escritas em português de Portugal. "
        "Adicione um '>' antes da resposta correta, sem espaço após o símbolo, por exemplo, '>Opção3'. "
        "As perguntas e opções devem ser formatadas como no exemplo a seguir: "
        "'Qual é a melhor maneira de evitar dívidas? | Gastar mais do que ganha, >Poupar dinheiro, Fazer empréstimos, Jantar fora'. "
        "Certifique-se de que não haja outros caracteres especiais ou números na formatação."
    )


    try:
        response = client.chat.completions.create(
            model=GROQ_LLAMA_MODEL_FULLNAME,
            messages=[
                {"role": "system", "content": prompt_pagination},
                {"role": "user", "content": markdown_content},
            ],
        )

        response_content = response.choices[0].message.content.strip()
        #print(response_content)
        # Split the response into lines and validate
        questions = response_content.split("\n")
        formatted_questions = []

        for question in questions:
            if "|" in question:
                # Sanitize the output to avoid empty entries
                formatted_question = question.strip()
                if formatted_question:  # Only add non-empty lines
                    formatted_questions.append(formatted_question)

        return formatted_questions  # Return the formatted questions

    except Exception as e:
        print("Erro ao gerar perguntas:", str(e))
        return "Não foi possível gerar perguntas no momento. Tente novamente mais tarde. Priemeira linha"




def quiz_interativo_with_groq(nivel_atual):
    st.header("Quiz de Educação Financeira com Perguntas Geradas por Groq")
    pontuacao = 0
    # Verificar se as perguntas já foram geradas
    if 'perguntas' not in st.session_state:
        # Gerar perguntas dinamicamente usando a API Groq
        questions = generate_questions()
        
        if not questions or isinstance(questions, str):
            st.error("Não foi possível gerar perguntas no momento. Tente novamente mais tarde.")
            return
    
        # Dicionário para armazenar as perguntas e opções
        perguntas = {}
        respostas_corretas = []  # Lista para armazenar as respostas corretas
    
        for index, question_data in enumerate(questions):
            respostas_corretas = []
            for question_data in questions:
                parts = question_data.split("|")
                pergunta = parts[0].strip()
                opcoes = parts[1].split(",")
                # Adicionar pergunta e opções ao dicionário
                perguntas[pergunta] = [opcao.strip() for opcao in opcoes]
                
                resposta_correta = next((opcao.strip().lstrip('>') for opcao in opcoes if opcao.startswith(' >')), None)
                respostas_corretas.append(resposta_correta)
            
    
        #print(respostas_corretas)
        # Armazenar as perguntas e respostas corretas no session_state
        st.session_state['perguntas'] = perguntas
        st.session_state['respostas_corretas'] = respostas_corretas
        st.session_state['pontuacao'] = 0  # Reiniciar pontuação
    
        # Recuperar perguntas e respostas corretas do session_state
    perguntas = st.session_state['perguntas']
    respostas_corretas = st.session_state['respostas_corretas']
    respostas = []
    for i, (pergunta, opcoes) in enumerate(perguntas.items()):
        resposta = st.radio(pergunta, opcoes, key=f"radio_{i}")
        respostas.append(resposta.strip().lstrip('>'))
        #print(f"{respostas[i]} == {respostas_corretas[i]}")
        #if respostas[i] == respostas_corretas[i]:
        #    st.session_state['pontuacao'] += 1

    #print(respostas)
    # Exibir pontuação final e atualizar o nível
    if st.button("Submeter Respostas"):
        # Coletar respostas do usuário
        # Adicione aqui o restante do seu código para interagir com o usuário

        for i, (pergunta, opcoes) in enumerate(perguntas.items()):
            # Verificar se a resposta é correta e atualizar a pontuação
            st.markdown(f"{respostas[i]} == {respostas_corretas[i]}")
            if respostas[i] == respostas_corretas[i]:
                st.session_state['pontuacao'] += 1
        pontuacao = st.session_state['pontuacao']
        st.success(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
        novo_nivel = atualizar_nivel(pontuacao)
        st.session_state['nivel'] = novo_nivel
        st.balloons()
        st.success(f"Você subiu para o Nível {novo_nivel}!")







# Main function for app
def main():
    st.title("Plataforma Gamificada de Educação Financeira")

    # Iniciar o nível do usuário na sessão, se ainda não existir
    if 'nivel' not in st.session_state:
        st.session_state['nivel'] = 1

    # Exibir o nível atual no topo de todas as páginas
    nivel_atual = st.session_state['nivel']
    mostrar_nivel_topo(nivel_atual)

    # Menu de navegação
    menu = ["Quiz Financeiro", "Quiz Finceiro Intel", "Progresso e Recompensas", "Simulações de Finanças"]
    escolha = st.selectbox("Selecione uma Opção", menu)

    # Navegação entre os diferentes módulos
    if escolha == "Quiz Financeiro":
        quiz_interativo(nivel_atual)
    elif escolha == "Quiz Finceiro Intel":
        quiz_interativo_with_groq(nivel_atual)  # Dynamic Groq questions
    elif escolha == "Progresso e Recompensas":
        progresso_e_recompensas()
    elif escolha == "Simulações de Finanças":
        simulacoes_complexas()

if __name__ == '__main__':
    main()

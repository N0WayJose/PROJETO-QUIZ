import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random

# ==========================================
# CONFIGURAÇÃO INICIAL E ESTILO
# ==========================================
st.set_page_config(page_title="Plataforma de Aprendizagem Matemática", page_icon="🧮", layout="wide")

st.title("🧮 Plataforma de Aprendizagem Matemática")
st.markdown("""
Bem-vindo à sua plataforma de estudos! 
Selecione um módulo na barra lateral. Dentro de cada módulo, você encontrará a **Teoria** para estudar e a **Prática** com questões aleatórias e resolução passo a passo.
""")

# ==========================================
# FUNÇÕES AUXILIARES
# ==========================================
def plotar_funcao(expr_sympy, x_min=-10, x_max=10, titulo="Gráfico"):
    x = sp.Symbol('x')
    f_num = sp.lambdify(x, expr_sympy, 'numpy')
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = f_num(x_vals)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_vals, y_vals, label="f(x)", color='#1f77b4', linewidth=2)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title(titulo)
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

# ==========================================
# BARRA LATERAL (Navegação Principal)
# ==========================================
st.sidebar.header("Navegação")
modulo = st.sidebar.radio(
    "Escolha o conteúdo:",
    ("Aula 1: Funções", "Aula 2: Limites", "Aula 3: Derivadas", "Aula 4: Integrais")
)
st.sidebar.markdown("---")
st.sidebar.info("Projeto desenvolvido para a disciplina de Cálculo. Documentação e código no GitHub.")

# ==========================================
# CONTEÚDO DOS MÓDULOS (TEORIA + PRÁTICA)
# ==========================================

# ------------------------------------------
# MÓDULO 1: FUNÇÕES
# ------------------------------------------
if modulo == "Aula 1: Funções":
    st.header("Aula 1: Funções")
    
    # Criando as Abas
    tab_teoria, tab_pratica = st.tabs(["📖 Teoria (Obrigatório)", "✍️ Prática (Quiz)"])
    
    with tab_teoria:
        st.subheader("Resumo Teórico de Funções")
        st.markdown("""
        * **Função Constante:** f(x) = c. O gráfico é uma reta horizontal.
        * **Função Afim (Linear):** f(x) = ax + b. O gráfico é uma reta inclinada.
        * **Função Quadrática:** f(x) = ax² + bx + c. O gráfico é uma parábola.
        * **Domínio:** Conjunto de todos os valores possíveis de x.
        * **Imagem:** Conjunto de todos os valores possíveis de y (resultados).
        * **Gráfico:** Fundamental para visualizar o comportamento da função.
        """)
        
    with tab_pratica:
        st.subheader("Praticar: Funções")
        
        # Inicializa o estado do quiz na memória
        if 'func_q_index' not in st.session_state:
            st.session_state.func_q_index = 0
            st.session_state.func_q_atual = None

        # Banco de questões (pode adicionar mais aqui)
        questoes_func = [
            {"tipo": "afim", "a": random.randint(2, 5), "b": random.randint(-5, 5), "x_val": 3},
            {"tipo": "afim", "a": random.randint(1, 4), "b": random.randint(1, 5), "x_val": 2},
            {"tipo": "quadratica", "a": 1, "b": -2, "c": 1, "x_val": 4},
            {"tipo": "constante", "c": random.randint(5, 20)},
            {"tipo": "quadratica", "a": 2, "b": 1, "c": -3, "x_val": 1}
        ]

        # Lógica para sortear nova questão
        if st.button("🔄 Sortear Nova Questão"):
            st.session_state.func_q_atual = random.choice(questoes_func)
            st.rerun() # Recarrega a página para limpar a resposta anterior

        # Exibe a questão sorteada
        if st.session_state.func_q_atual:
            q = st.session_state.func_q_atual
            
            if q["tipo"] == "afim":
                sinal = "+" if q["b"] >= 0 else "-"
                texto_f = f"{q['a']}x {sinal} {abs(q['b'])}"
                st.write(f"Considere a função **f(x) = {texto_f}**.")
                st.write(f"Qual é o valor de f({q['x_val']})?")
                resp_certa = (q["a"] * q["x_val"]) + q["b"]
                explicacao = f"f({q['x_val']}) = {q['a']} * ({q['x_val']}) {sinal} {abs(q['b'])} = {resp_certa}."
            
            elif q["tipo"] == "quadratica":
                texto_f = f"{q['a']}x² + {q['b']}x + {q['c']}"
                st.write(f"Considere a função **f(x) = {texto_f}**.")
                st.write(f"Qual é o valor de f({q['x_val']})?")
                resp_certa = (q["a"] * (q["x_val"]**2)) + (q["b"] * q["x_val"]) + q["c"]
                explicacao = f"f({q['x_val']}) = {q['a']}({q['x_val']}²) + {q['b']}({q['x_val']}) + {q['c']} = {q['a']*q['x_val']**2} + {q['b']*q['x_val']} + {q['c']} = {resp_certa}."
                
            elif q["tipo"] == "constante":
                texto_f = f"{q['c']}"
                st.write(f"Considere a função constante **f(x) = {texto_f}**.")
                st.write(f"Qual é o valor de f(10)?")
                resp_certa = q["c"]
                explicacao = f"Em uma função constante, o valor não depende de x. Portanto, f(10) é sempre {q['c']}."

            # Opções de resposta
            opcoes = [str(resp_certa), str(resp_certa + 2), str(resp_certa - 3), str(resp_certa + 10)]
            opcoes = sorted(list(set(opcoes)))
            opcoes.insert(0, "Selecione...")
            
            resp_user = st.radio("Sua resposta:", opcoes, key=f"radio_{q['tipo']}_{resp_certa}")
            
            if st.button("Verificar Resposta"):
                if resp_user == "Selecione...":
                    st.warning("Escolha uma opção!")
                elif resp_user == str(resp_certa):
                    st.success(f"✅ **Você acertou!** A resposta é {resp_certa}.")
                    st.info(f"**Passo a passo:** {explicacao}")
                else:
                    st.error(f"❌ **Você errou.** A resposta correta é {resp_certa}.")
                    st.info(f"**Passo a passo:** {explicacao}")
                
                # Se for afim ou quadrática, plota o gráfico
                if q["tipo"] in ["afim", "quadratica"]:
                    st.write("### Visualização Gráfica")
                    x = sp.Symbol('x')
                    if q["tipo"] == "afim":
                        expr = q["a"] * x + q["b"]
                    else:
                        expr = q["a"] * x**2 + q["b"] * x + q["c"]
                    plotar_funcao(expr, titulo="Gráfico da Função")

# ------------------------------------------
# MÓDULO 2: LIMITES
# ------------------------------------------
elif modulo == "Aula 2: Limites":
    st.header("Aula 2: Limites")
    
    tab_teoria, tab_pratica = st.tabs(["📖 Teoria (Obrigatório)", "✍️ Prática (Quiz)"])
    
    with tab_teoria:
        st.subheader("Resumo Teórico de Limites")
        st.markdown("""
        * **Definição:** O limite de f(x) quando x tende a *a* é o valor L que a função se aproxima.
        * **Limites Laterais:** Limite pela esquerda (x → a⁻) e pela direita (x → a⁺). Se forem diferentes, o limite não existe.
        * **Indeterminação 0/0:** Quando substituímos o valor e dá 0/0, precisamos fatorar, simplificar ou usar racionalização.
        * **Continuidade:** Uma função é contínua se o limite existe, a função é definida naquele ponto e o limite é igual ao valor da função.
        """)
        
    with tab_pratica:
        st.subheader("Praticar: Limites")
        
        # Banco de limites (focados nas exigências)
        questoes_lim = [
            {"tipo": "fatoracao", "expr": "x² - 4", "den": "x - 2", "a": 2, "resp": 4, "expl": "Substituindo x=2, temos 0/0. Fatore o numerador: (x-2)(x+2). Cancele (x-2). Limite de (x+2) quando x→2 é 4."},
            {"tipo": "fatoracao", "expr": "x² - 9", "den": "x - 3", "a": 3, "resp": 6, "expl": "Substituindo x=3, temos 0/0. Fatore: (x-3)(x+3). Cancele (x-3). Limite de (x+3) com x→3 é 6."},
            {"tipo": "direto", "expr": "2x + 5", "den": "1", "a": 3, "resp": 11, "expl": "Basta substituir x=3: 2(3) + 5 = 11. Não há indeterminação."},
            {"tipo": "constante", "expr": "7", "den": "1", "a": 10, "resp": 7, "expl": "O limite de uma constante é a própria constante, independente do valor de x."},
            {"tipo": "fatoracao", "expr": "x² - 1", "den": "x - 1", "a": 1, "resp": 2, "expl": "Substituindo x=1, temos 0/0. Fatore: (x-1)(x+1). Cancele (x-1). Limite de (x+1) com x→1 é 2."}
        ]

        if 'lim_q_atual' not in st.session_state:
            st.session_state.lim_q_atual = random.choice(questoes_lim)

        if st.button("🔄 Sortear Nova Questão"):
            st.session_state.lim_q_atual = random.choice(questoes_lim)
            st.rerun()

        q = st.session_state.lim_q_atual
        st.write(f"Calcule o limite: **lim (x→{q['a']}) de ({q['expr']}) / ({q['den']})**")
        
        opcoes = [str(q['resp']), str(q['resp'] + 2), "0", "Inexistente"]
        opcoes = sorted(list(set(opcoes)))
        opcoes.insert(0, "Selecione...")
        
        resp_user = st.radio("Sua resposta:", opcoes, key=f"lim_{q['a']}_{q['resp']}")
        
        if st.button("Verificar Resposta", key="btn_ver_lim"):
            if resp_user == "Selecione...":
                st.warning("Escolha uma opção!")
            elif resp_user == str(q['resp']):
                st.success(f"✅ **Você acertou!** O limite é {q['resp']}.")
                st.info(f"**Passo a passo:** {q['expl']}")
            else:
                st.error(f"❌ **Você errou.** O limite correto é {q['resp']}.")
                st.info(f"**Passo a passo:** {q['expl']}")

# ------------------------------------------
# MÓDULO 3: DERIVADAS
# ------------------------------------------
elif modulo == "Aula 3: Derivadas":
    st.header("Aula 3: Derivadas")
    
    tab_teoria, tab_pratica = st.tabs(["📖 Teoria (Obrigatório)", "✍️ Prática (Quiz)"])
    
    with tab_teoria:
        st.subheader("Resumo Teórico de Derivadas")
        st.markdown("""
        * **Regra da Constante:** d/dx (c) = 0
        * **Regra da Potência:** d/dx (xⁿ) = n * xⁿ⁻¹
        * **Regra da Soma/Subtração:** Deriva cada termo separadamente.
        * **Regra do Produto:** (f*g)' = f'g + fg'
        * **Regra do Quociente:** (f/g)' = (f'g - fg') / g²
        * **Regra da Cadeia:** d/dx [f(g(x))] = f'(g(x)) * g'(x)
        """)
        
    with tab_pratica:
        st.subheader("Praticar: Derivadas")
        
        questoes_der = [
            {"f": "3x² + 2x", "resp": "6x + 2", "expl": "Derivada de 3x² = 6x. Derivada de 2x = 2. Resultado: 6x + 2."},
            {"f": "x³ - 4x + 7", "resp": "3x² - 4", "expl": "Derivada de x³ = 3x². Derivada de -4x = -4. Derivada de 7 = 0. Resultado: 3x² - 4."},
            {"f": "5x⁴", "resp": "20x³", "expl": "Regra do tombo: 5 * 4x³ = 20x³."},
            {"f": "2x³ + 3x² - x + 1", "resp": "6x² + 6x - 1", "expl": "2x³ -> 6x². 3x² -> 6x. -x -> -1. 1 -> 0. Resultado: 6x² + 6x - 1."},
            {"f": "x² * (x + 1)", "resp": "3x² + 2x", "expl": "Regra do produto ou distribua: x³ + x². Derivada: 3x² + 2x."}
        ]

        if 'der_q_atual' not in st.session_state:
            st.session_state.der_q_atual = random.choice(questoes_der)

        if st.button("🔄 Sortear Nova Questão"):
            st.session_state.der_q_atual = random.choice(questoes_der)
            st.rerun()

        q = st.session_state.der_q_atual
        st.write(f"Qual é a derivada da função **f(x) = {q['f']}**?")
        
        # Para simplificar, vou gerar opções baseadas em erros comuns
        opcoes = [q['resp'], "3x² + 2", "6x + 2x", "0"]
        opcoes = sorted(list(set(opcoes)))
        opcoes.insert(0, "Selecione...")
        
        resp_user = st.radio("Sua resposta:", opcoes, key=f"der_{q['f']}")
        
        if st.button("Verificar Resposta", key="btn_ver_der"):
            if resp_user == "Selecione...":
                st.warning("Escolha uma opção!")
            elif resp_user == q['resp']:
                st.success(f"✅ **Você acertou!** A derivada é {q['resp']}.")
                st.info(f"**Passo a passo:** {q['expl']}")
            else:
                st.error(f"❌ **Você errou.** A derivada correta é {q['resp']}.")
                st.info(f"**Passo a passo:** {q['expl']}")

# ------------------------------------------
# MÓDULO 4: INTEGRAIS
# ------------------------------------------
elif modulo == "Aula 4: Integrais":
    st.header("Aula 4: Integrais")
    
    tab_teoria, tab_pratica = st.tabs(["📖 Teoria (Obrigatório)", "✍️ Prática (Quiz)"])
    
    with tab_teoria:
        st.subheader("Resumo Teórico de Integrais")
        st.markdown("""
        * **Integral Indefinida:** ∫ f(x) dx = F(x) + C (onde F'(x) = f(x)). Sempre adicione a constante **C**.
        * **Regra da Potência:** ∫ xⁿ dx = (xⁿ⁺¹) / (n+1) + C (para n ≠ -1).
        * **Soma/Subtração:** Integre cada termo separadamente.
        * **Integral Definida:** Calculada de *a* até *b* usando o Teorema Fundamental do Cálculo: F(b) - F(a).
        * **Substituição (u-sub):** Usada quando a função é composta, ex: ∫ 2x(x²+1) dx. Faça u = x²+1.
        """)
        
    with tab_pratica:
        st.subheader("Praticar: Integrais")
        
        questoes_int = [
            {"f": "2x + 3", "resp": "x² + 3x + C", "expl": "Integral de 2x = x². Integral de 3 = 3x. Adicione C."},
            {"f": "3x²", "resp": "x³ + C", "expl": "Sobe o expoente (3) e divide por ele: 3x³/3 = x³. Adicione C."},
            {"f": "4x³ - 2x", "resp": "x⁴ - x² + C", "expl": "Integral de 4x³ = x⁴. Integral de -2x = -x². Adicione C."},
            {"f": "5", "resp": "5x + C", "expl": "A integral de uma constante é a constante multiplicada por x."},
            {"f": "x² + x", "resp": "(x³/3) + (x²/2) + C", "expl": "x² vira x³/3. x vira x²/2."}
        ]

        if 'int_q_atual' not in st.session_state:
            st.session_state.int_q_atual = random.choice(questoes_int)

        if st.button("🔄 Sortear Nova Questão"):
            st.session_state.int_q_atual = random.choice(questoes_int)
            st.rerun()

        q = st.session_state.int_q_atual
        st.write(f"Calcule a integral indefinida: **∫ ({q['f']}) dx**")
        
        opcoes = [q['resp'], "x² + 3x", "x³/3 + C", "0"]
        opcoes = sorted(list(set(opcoes)))
        opcoes.insert(0, "Selecione...")
        
        resp_user = st.radio("Sua resposta:", opcoes, key=f"int_{q['f']}")
        
        if st.button("Verificar Resposta", key="btn_ver_int"):
            if resp_user == "Selecione...":
                st.warning("Escolha uma opção!")
            elif resp_user == q['resp']:
                st.success(f"✅ **Você acertou!** A integral é {q['resp']}.")
                st.info(f"**Passo a passo:** {q['expl']}")
            else:
                st.error(f"❌ **Você errou.** A integral correta é {q['resp']}.")
                st.info(f"**Passo a passo:** {q['expl']}")

# ==========================================
# RODAPÉ
# ==========================================
st.markdown("---")
st.caption("Desenvolvido como projeto acadêmico. Documentação e código disponíveis no GitHub.")
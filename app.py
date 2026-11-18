import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random

# ==========================================
# 1. CONFIGURAÇÃO E CSS CUSTOMIZADO
# ==========================================
st.set_page_config(page_title="Plataforma de Matemática", layout="centered")

st.markdown("""
<style>
    /* Fundo escuro com degradê leve */
    .stApp {
        background: linear-gradient(180deg, #1a1a2e 0%, #0f0f16 100%);
        color: #e0e0e0;
    }
    
    /* Animação de Fade-Down */
    @keyframes fadeDown {
        from { opacity: 0; transform: translateY(-15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .block-container {
        animation: fadeDown 0.6s ease-out;
        padding-top: 3rem !important;
        max-width: 800px; /* Centraliza melhor o conteúdo */
    }

    /* Títulos e Textos */
    h1, h2, h3, h4, p, label {
        color: #e0e0e0 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1 { text-align: center; margin-bottom: 2rem; font-weight: 600; letter-spacing: 1px; }
    
    /* Estilo das Abas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #24243a;
        border-radius: 8px;
        padding: 10px 24px;
        color: #a0a0b0;
        border: 1px solid #3a3a5a;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        background-color: #6200ea !important;
        color: #ffffff !important;
        border-color: #7c43bd !important;
    }

    /* Botões Padrão (Sortear, Verificar) */
    .stButton > button {
        background-color: #2a2a40;
        color: #ffffff;
        border: 1px solid #6200ea;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: 500;
        transition: all 0.2s;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #6200ea;
        border-color: #7c43bd;
        color: white;
    }

    /* Limpando o visual dos Radio Buttons */
    div[role="radiogroup"] label {
        padding: 8px 12px;
        background-color: #1e1e2f;
        border-radius: 6px;
        margin-bottom: 5px;
        border: 1px solid transparent;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] label:hover {
        background-color: #2a2a40;
        border: 1px solid #3a3a5a;
    }
    
    /* Caixas de mensagem (Sucesso, Erro, Info) */
    .stAlert {
        background-color: #1e1e2f !important;
        border: 1px solid #3a3a5a !important;
        color: #e0e0e0 !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# FUNÇÕES AUXILIARES
# ==========================================
def plotar_funcao(expr_sympy, x_min=-10, x_max=10, titulo="Gráfico"):
    x = sp.Symbol('x')
    f_num = sp.lambdify(x, expr_sympy, 'numpy')
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = f_num(x_vals)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    
    ax.plot(x_vals, y_vals, color='#b388ff', linewidth=2) # Roxo mais claro para o gráfico
    ax.axhline(0, color='#555555', linewidth=1)
    ax.axvline(0, color='#555555', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.2, color='#777777')
    ax.set_title(titulo, color='#e0e0e0')
    ax.tick_params(colors='#a0a0b0')
    ax.legend(["f(x)"], facecolor='#24243a', labelcolor='#e0e0e0', framealpha=0.8)
    st.pyplot(fig)
    plt.close(fig)

# ==========================================
# ESTADO INICIAL DO MENU
# ==========================================
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = "menu"

# ==========================================
# TELA INICIAL (MENU CENTRALIZADO)
# ==========================================
if st.session_state.pagina_atual == "menu":
    st.title("Plataforma de Matemática")
    st.markdown("<p style='text-align: center; color: #a0a0b0; margin-bottom: 3rem;'>Selecione um módulo para estudar</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        if st.button("Aula 1: Funções", key="menu_func", use_container_width=True):
            st.session_state.pagina_atual = "func"
            st.rerun()
        if st.button("Aula 3: Derivadas", key="menu_der", use_container_width=True):
            st.session_state.pagina_atual = "der"
            st.rerun()
            
    with col2:
        if st.button("Aula 2: Limites", key="menu_lim", use_container_width=True):
            st.session_state.pagina_atual = "lim"
            st.rerun()
        if st.button("Aula 4: Integrais", key="menu_int", use_container_width=True):
            st.session_state.pagina_atual = "int"
            st.rerun()

    st.markdown("<br><br><hr style='border-color: #3a3a5a;'><p style='text-align: center; color: #666; font-size: 0.9rem;'>Projeto Acadêmico de Cálculo</p>", unsafe_allow_html=True)

# ==========================================
# MÓDULOS (CONTEÚDO)
# ==========================================
else:
    if st.button("Voltar ao Menu Principal"):
        st.session_state.pagina_atual = "menu"
        st.rerun()

    # ------------------------------------------
    # MÓDULO 1: FUNÇÕES
    # ------------------------------------------
    if st.session_state.pagina_atual == "func":
        st.header("Aula 1: Funções")
        tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
        
        with tab_teoria:
            st.subheader("Resumo Teórico")
            st.markdown("""
            * **Constante:** f(x) = c. Gráfico: reta horizontal.
            * **Afim (Linear):** f(x) = ax + b. Gráfico: reta inclinada.
            * **Quadrática:** f(x) = ax² + bx + c. Gráfico: parábola.
            * **Domínio:** Valores possíveis de x. **Imagem:** Valores possíveis de y.
            """)
            
        with tab_pratica:
            if 'func_q_atual' not in st.session_state:
                st.session_state.func_q_atual = None

            questoes_func = [
                {"tipo": "afim", "a": random.randint(2, 5), "b": random.randint(-5, 5), "x_val": 3},
                {"tipo": "afim", "a": random.randint(1, 4), "b": random.randint(1, 5), "x_val": 2},
                {"tipo": "quadratica", "a": 1, "b": -2, "c": 1, "x_val": 4},
                {"tipo": "constante", "c": random.randint(5, 20)},
                {"tipo": "quadratica", "a": 2, "b": 1, "c": -3, "x_val": 1},
                {"tipo": "grafico", "subtipo": "quadratica"}, 
                {"tipo": "grafico", "subtipo": "afim"},
                {"tipo": "grafico", "subtipo": "constante"}
            ]

            if st.button("Sortear Nova Questão"):
                st.session_state.func_q_atual = random.choice(questoes_func)
                st.rerun() 

            if st.session_state.func_q_atual:
                q = st.session_state.func_q_atual
                
                if q["tipo"] == "grafico":
                    st.write("Analise o gráfico abaixo e responda:")
                    st.write("**Qual é o tipo da função representada?**")
                    x_sym = sp.Symbol('x')
                    if q["subtipo"] == "quadratica":
                        expr = x_sym**2 - 4
                        resp_certa = "Quadrática (Parábola)"
                        explicacao = "O gráfico tem o formato de uma parábola. Isso indica uma função do 2º grau."
                    elif q["subtipo"] == "afim":
                        expr = 2*x_sym + 1
                        resp_certa = "Afim (Reta inclinada)"
                        explicacao = "O gráfico é uma linha reta inclinada. Função do 1º grau."
                    else:
                        expr = sp.Integer(5)
                        resp_certa = "Constante (Reta horizontal)"
                        explicacao = "O gráfico é uma linha reta horizontal. O valor de y não muda."
                    
                    plotar_funcao(expr, titulo="Gráfico Desconhecido")
                    opcoes = ["Afim (Reta inclinada)", "Quadrática (Parábola)", "Constante (Reta horizontal)", "Exponencial"]
                
                elif q["tipo"] == "afim":
                    sinal = "+" if q["b"] >= 0 else "-"
                    texto_f = f"{q['a']}x {sinal} {abs(q['b'])}"
                    st.write(f"Considere a função **f(x) = {texto_f}**.")
                    st.write(f"Qual é o valor de f({q['x_val']})?")
                    resp_certa = (q["a"] * q["x_val"]) + q["b"]
                    explicacao = f"f({q['x_val']}) = {q['a']} * ({q['x_val']}) {sinal} {abs(q['b'])} = {resp_certa}."
                    opcoes = [str(resp_certa), str(resp_certa + 2), str(resp_certa - 3), str(resp_certa + 10)]
                    
                elif q["tipo"] == "quadratica":
                    texto_f = f"{q['a']}x² + {q['b']}x + {q['c']}"
                    st.write(f"Considere a função **f(x) = {texto_f}**.")
                    st.write(f"Qual é o valor de f({q['x_val']})?")
                    resp_certa = (q["a"] * (q["x_val"]**2)) + (q["b"] * q["x_val"]) + q["c"]
                    explicacao = f"f({q['x_val']}) = {q['a']}({q['x_val']}²) + {q['b']}({q['x_val']}) + {q['c']} = {resp_certa}."
                    opcoes = [str(resp_certa), str(resp_certa + 2), str(resp_certa - 3), str(resp_certa + 10)]
                    
                elif q["tipo"] == "constante":
                    st.write(f"Considere a função constante **f(x) = {q['c']}**.")
                    st.write(f"Qual é o valor de f(10)?")
                    resp_certa = q["c"]
                    explicacao = f"Em uma função constante, o valor não depende de x. Portanto, f(10) é sempre {q['c']}."
                    opcoes = [str(resp_certa), str(resp_certa + 2), str(resp_certa - 3), str(resp_certa + 10)]

                if q["tipo"] != "grafico":
                    opcoes = sorted(list(set(opcoes)))
                else:
                    random.shuffle(opcoes)
                
                # AQUI ESTÁ A MÁGICA: index=None remove a opção "Selecione..."
                resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"radio_{q['tipo']}_{str(resp_certa)}")
                
                if st.button("Verificar Resposta", key="btn_ver_func"):
                    if resp_user is None:
                        st.warning("Por favor, selecione uma opção antes de verificar.")
                    elif resp_user == str(resp_certa):
                        st.success(f"Você acertou! A resposta é {resp_certa}.")
                        st.info(f"Passo a passo: {explicacao}")
                    else:
                        st.error(f"Você errou. A resposta correta é {resp_certa}.")
                        st.info(f"Passo a passo: {explicacao}")
                    
                    if q["tipo"] in ["afim", "quadratica"]:
                        st.write("### Visualização Gráfica")
                        x = sp.Symbol('x')
                        expr = (q["a"] * x + q["b"]) if q["tipo"] == "afim" else (q["a"] * x**2 + q["b"] * x + q["c"])
                        plotar_funcao(expr, titulo="Gráfico da Função")

    # ------------------------------------------
    # MÓDULO 2: LIMITES
    # ------------------------------------------
    elif st.session_state.pagina_atual == "lim":
        st.header("Aula 2: Limites")
        tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
        
        with tab_teoria:
            st.subheader("Resumo Teórico")
            st.markdown("""
            * **Definição:** O valor que a função se aproxima.
            * **Indeterminação 0/0:** Exige fatoração ou racionalização.
            * **Limites Laterais:** Esquerda e direita devem ser iguais para o limite existir.
            """)
            
        with tab_pratica:
            questoes_lim = [
                {"expr": "x² - 4", "den": "x - 2", "a": 2, "resp": 4, "expl": "Fatore: (x-2)(x+2)/(x-2). Cancela. Limite de x+2 = 4."},
                {"expr": "x² - 9", "den": "x - 3", "a": 3, "resp": 6, "expl": "Fatore: (x-3)(x+3)/(x-3). Cancela. Limite de x+3 = 6."},
                {"expr": "2x + 5", "den": "1", "a": 3, "resp": 11, "expl": "Substituição direta: 2(3) + 5 = 11."},
                {"expr": "7", "den": "1", "a": 10, "resp": 7, "expl": "Limite de constante é a própria constante."},
                {"expr": "x² - 1", "den": "x - 1", "a": 1, "resp": 2, "expl": "Fatore: (x-1)(x+1)/(x-1). Cancela. Limite de x+1 = 2."}
            ]

            if 'lim_q_atual' not in st.session_state:
                st.session_state.lim_q_atual = random.choice(questoes_lim)

            if st.button("Sortear Nova Questão"):
                st.session_state.lim_q_atual = random.choice(questoes_lim)
                st.rerun()

            q = st.session_state.lim_q_atual
            st.write(f"Calcule o limite: **lim (x→{q['a']}) de ({q['expr']}) / ({q['den']})**")
            
            opcoes = [str(q['resp']), str(q['resp'] + 2), "0", "Inexistente"]
            opcoes = sorted(list(set(opcoes)))
            
            resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"lim_{q['a']}_{q['resp']}")
            
            if st.button("Verificar Resposta", key="btn_ver_lim"):
                if resp_user is None:
                    st.warning("Por favor, selecione uma opção antes de verificar.")
                elif resp_user == str(q['resp']):
                    st.success(f"Você acertou! O limite é {q['resp']}.")
                    st.info(f"Passo a passo: {q['expl']}")
                else:
                    st.error(f"Você errou. O limite correto é {q['resp']}.")
                    st.info(f"Passo a passo: {q['expl']}")

    # ------------------------------------------
    # MÓDULO 3: DERIVADAS
    # ------------------------------------------
    elif st.session_state.pagina_atual == "der":
        st.header("Aula 3: Derivadas")
        tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
        
        with tab_teoria:
            st.subheader("Resumo Teórico")
            st.markdown("""
            * **Constante:** d/dx (c) = 0
            * **Potência:** d/dx (xⁿ) = n * xⁿ⁻¹
            * **Soma:** Deriva cada termo.
            """)
            
        with tab_pratica:
            questoes_der = [
                {"f": "3x² + 2x", "resp": "6x + 2", "expl": "3x² vira 6x. 2x vira 2."},
                {"f": "x³ - 4x + 7", "resp": "3x² - 4", "expl": "x³ vira 3x². -4x vira -4. 7 vira 0."},
                {"f": "5x⁴", "resp": "20x³", "expl": "Regra do tombo: 5 * 4x³ = 20x³."},
                {"f": "2x³ + 3x² - x + 1", "resp": "6x² + 6x - 1", "expl": "2x³ -> 6x². 3x² -> 6x. -x -> -1. 1 -> 0."},
                {"f": "x² * (x + 1)", "resp": "3x² + 2x", "expl": "Distribua: x³ + x². Derivada: 3x² + 2x."}
            ]

            if 'der_q_atual' not in st.session_state:
                st.session_state.der_q_atual = random.choice(questoes_der)

            if st.button("Sortear Nova Questão"):
                st.session_state.der_q_atual = random.choice(questoes_der)
                st.rerun()

            q = st.session_state.der_q_atual
            st.write(f"Qual é a derivada da função **f(x) = {q['f']}**?")
            
            opcoes = [q['resp'], "3x² + 2", "6x + 2x", "0"]
            opcoes = sorted(list(set(opcoes)))
            
            resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"der_{q['f']}")
            
            if st.button("Verificar Resposta", key="btn_ver_der"):
                if resp_user is None:
                    st.warning("Por favor, selecione uma opção antes de verificar.")
                elif resp_user == q['resp']:
                    st.success(f"Você acertou! A derivada é {q['resp']}.")
                    st.info(f"Passo a passo: {q['expl']}")
                else:
                    st.error(f"Você errou. A derivada correta é {q['resp']}.")
                    st.info(f"Passo a passo: {q['expl']}")

    # ------------------------------------------
    # MÓDULO 4: INTEGRAIS
    # ------------------------------------------
    elif st.session_state.pagina_atual == "int":
        st.header("Aula 4: Integrais")
        tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
        
        with tab_teoria:
            st.subheader("Resumo Teórico")
            st.markdown("""
            * **Indefinida:** ∫ f(x) dx = F(x) + C. Nunca esqueça o + C.
            * **Potência:** ∫ xⁿ dx = (xⁿ⁺¹) / (n+1) + C.
            * **Soma:** Integre cada termo.
            """)
            
        with tab_pratica:
            questoes_int = [
                {"f": "2x + 3", "resp": "x² + 3x + C", "expl": "2x vira x². 3 vira 3x. Adicione C."},
                {"f": "3x²", "resp": "x³ + C", "expl": "Sobe expoente e divide por ele: 3x³/3 = x³. Adicione C."},
                {"f": "4x³ - 2x", "resp": "x⁴ - x² + C", "expl": "4x³ vira x⁴. -2x vira -x². Adicione C."},
                {"f": "5", "resp": "5x + C", "expl": "Constante vira constante vezes x."},
                {"f": "x² + x", "resp": "(x³/3) + (x²/2) + C", "expl": "x² vira x³/3. x vira x²/2. Adicione C."}
            ]

            if 'int_q_atual' not in st.session_state:
                st.session_state.int_q_atual = random.choice(questoes_int)

            if st.button("Sortear Nova Questão"):
                st.session_state.int_q_atual = random.choice(questoes_int)
                st.rerun()

            q = st.session_state.int_q_atual
            st.write(f"Calcule a integral indefinida: **∫ ({q['f']}) dx**")
            
            opcoes = [q['resp'], "x² + 3x", "x³/3 + C", "0"]
            opcoes = sorted(list(set(opcoes)))
            
            resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"int_{q['f']}")
            
            if st.button("Verificar Resposta", key="btn_ver_int"):
                if resp_user is None:
                    st.warning("Por favor, selecione uma opção antes de verificar.")
                elif resp_user == q['resp']:
                    st.success(f"Você acertou! A integral é {q['resp']}.")
                    st.info(f"Passo a passo: {q['expl']}")
                else:
                    st.error(f"Você errou. A integral correta é {q['resp']}.")
                    st.info(f"Passo a passo: {q['expl']}")

st.markdown("<br><hr style='border-color: #3a3a5a;'><p style='text-align: center; color: #666; font-size: 0.9rem;'>Desenvolvido como projeto acadêmico.</p>", unsafe_allow_html=True)
import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random

# ==========================================
# 1. CONFIGURAÇÃO E CSS CUSTOMIZADO
# ==========================================
st.set_page_config(page_title="Plataforma de Matemática", layout="wide") # Mudei para "wide" para usar as laterais

st.markdown("""
<style>
    /* Fundo escuro */
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
        padding-top: 2rem !important;
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
        justify-content: flex-start;
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

    /* Botões */
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

    /* Radio Buttons */
    div[role="radiogroup"] label {
        padding: 10px 15px;
        background-color: #1e1e2f;
        border-radius: 6px;
        margin-bottom: 8px;
        border: 1px solid #3a3a5a;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] label:hover {
        background-color: #2a2a40;
        border: 1px solid #6200ea;
    }
    
    /* Caixas de mensagem */
    .stAlert {
        background-color: #1e1e2f !important;
        border: 1px solid #3a3a5a !important;
        color: #e0e0e0 !important;
    }

    /* Card de Dica (quando não há imagem) */
    .dica-card {
        background-color: #24243a;
        border-left: 5px solid #6200ea;
        padding: 20px;
        border-radius: 8px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# FUNÇÕES DE GERAÇÃO DE GRÁFICOS
# ==========================================
def plotar_funcao(expr_sympy, x_min=-10, x_max=10, titulo="Gráfico", preencher_area=False, esconder_legenda=False):
    x = sp.Symbol('x')
    f_num = sp.lambdify(x, expr_sympy, 'numpy')
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = f_num(x_vals)
    
    fig, ax = plt.subplots(figsize=(7, 5))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    
    # Se for esconder, o label é vazio, senão é f(x)
    label_linha = "" if esconder_legenda else "f(x)"
    ax.plot(x_vals, y_vals, color='#b388ff', linewidth=2, label=label_linha)
    
    ax.axhline(0, color='#555555', linewidth=1)
    ax.axvline(0, color='#555555', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.2, color='#777777')
    ax.set_title(titulo, color='#e0e0e0')
    ax.tick_params(colors='#a0a0b0')
    
    if preencher_area:
        ax.fill_between(x_vals, y_vals, 0, where=(x_vals >= x_min), color='#6200ea', alpha=0.3)
    
    # Só mostra a legenda se NÃO for para esconder
    if not esconder_legenda:
        ax.legend(facecolor='#24243a', labelcolor='#e0e0e0', framealpha=0.8)
    
    st.pyplot(fig)
    plt.close(fig)

# ==========================================
# ESTADO INICIAL E NAVEGAÇÃO
# ==========================================
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = "menu"

if st.session_state.pagina_atual == "menu":
    st.title("Plataforma de Matemática")
    st.markdown("<p style='text-align: center; color: #a0a0b0; margin-bottom: 3rem;'>Selecione um módulo para estudar</p>", unsafe_allow_html=True)
    
    # Centralizando os botões do menu
    col_vazia1, col_central, col_vazia2 = st.columns([1, 2, 1])
    with col_central:
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            if st.button("Aula 1: Funções", key="menu_func", use_container_width=True):
                st.session_state.pagina_atual = "func"; st.rerun()
            if st.button("Aula 3: Derivadas", key="menu_der", use_container_width=True):
                st.session_state.pagina_atual = "der"; st.rerun()
        with col2:
            if st.button("Aula 2: Limites", key="menu_lim", use_container_width=True):
                st.session_state.pagina_atual = "lim"; st.rerun()
            if st.button("Aula 4: Integrais", key="menu_int", use_container_width=True):
                st.session_state.pagina_atual = "int"; st.rerun()

else:
    if st.button("Voltar ao Menu Principal"):
        st.session_state.pagina_atual = "menu"; st.rerun()

    # ==========================================
    # LAYOUT DE DUAS COLUNAS PARA OS MÓDULOS
    # ==========================================
    col_quiz, col_imagem = st.columns([1.2, 1], gap="large")

    # ------------------------------------------
    # MÓDULO 1: FUNÇÕES
    # ------------------------------------------
    if st.session_state.pagina_atual == "func":
        with col_quiz:
            st.header("Aula 1: Funções")
            tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
            with tab_teoria:
                st.markdown("""
                * **Constante:** f(x) = c. Reta horizontal.
                * **Afim:** f(x) = ax + b. Reta inclinada.
                * **Quadrática:** f(x) = ax² + bx + c. Parábola.
                """)
            
            with tab_pratica:
                if 'func_q_atual' not in st.session_state:
                    st.session_state.func_q_atual = None

                # Adicionei a flag "esconder_nome" para a lógica do gráfico
                questoes_func = [
                    {"texto": "f(x) = 2x + 3. Qual o valor de f(4)?", "resp": "11", "expl": "2(4) + 3 = 11.", "img": {"tipo": "afim", "a": 2, "b": 3}, "esconder_nome": False},
                    {"texto": "f(x) = x² - 4. Qual o valor de f(3)?", "resp": "5", "expl": "3² - 4 = 9 - 4 = 5.", "img": {"tipo": "quadratica", "a": 1, "b": 0, "c": -4}, "esconder_nome": False},
                    {"texto": "Qual é o tipo de gráfico que representa f(x) = 3x² + 2x - 1?", "resp": "Parábola", "expl": "Funções quadráticas (ax²) geram parábolas.", "img": {"tipo": "quadratica", "a": 3, "b": 2, "c": -1}, "esconder_nome": True}, # <--- ESCONDE AQUI
                    {"texto": "A função f(x) = 7 é do tipo:", "resp": "Constante", "expl": "O valor não muda, f(x) é sempre 7.", "img": {"tipo": "constante", "c": 7}, "esconder_nome": True}, # <--- ESCONDE AQUI
                    {"texto": "A função f(x) = -2x + 5 é crescente ou decrescente?", "resp": "Decrescente", "expl": "O coeficiente 'a' é negativo (-2).", "img": {"tipo": "afim", "a": -2, "b": 5}, "esconder_nome": False}
                ]

                if st.button("Sortear Nova Questão", key="btn_sort_func"):
                    st.session_state.func_q_atual = random.choice(questoes_func)
                    st.rerun() 

                if st.session_state.func_q_atual:
                    q = st.session_state.func_q_atual
                    st.write(f"**{q['texto']}**")
                    
                    opcoes = [q['resp'], "10", "Parábola", "Constante", "5"]
                    opcoes = sorted(list(set(opcoes)))
                    
                    resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"radio_func_{q['texto']}")
                    
                    if st.button("Verificar Resposta", key="btn_ver_func"):
                        if resp_user is None: st.warning("Selecione uma opção.")
                        elif resp_user == q['resp']:
                            st.success("Você acertou!")
                            st.info(f"Passo a passo: {q['expl']}")
                        else:
                            st.error("Você errou.")
                            st.info(f"Resposta correta: {q['resp']}. Passo a passo: {q['expl']}")

        with col_imagem:
            st.write("<br><br>", unsafe_allow_html=True) 
            if st.session_state.func_q_atual and "img" in st.session_state.func_q_atual:
                img_data = st.session_state.func_q_atual["img"]
                esconder = st.session_state.func_q_atual.get("esconder_nome", False)
                
                x = sp.Symbol('x')
                
                # Lógica para definir o título do gráfico na tela
                if esconder:
                    titulo_grafico = "Gráfico de f(x)" # Título neutro
                else:
                    if img_data["tipo"] == "afim":
                        titulo_grafico = f"Visualização: f(x) = {img_data['a']}x + {img_data['b']}"
                    elif img_data["tipo"] == "quadratica":
                        titulo_grafico = "Visualização: Parábola"
                    else:
                        titulo_grafico = f"Visualização: f(x) = {img_data['c']}"
                
                # Desenhando a função
                if img_data["tipo"] == "afim":
                    expr = img_data["a"] * x + img_data["b"]
                elif img_data["tipo"] == "quadratica":
                    expr = img_data["a"] * x**2 + img_data["b"] * x + img_data["c"]
                elif img_data["tipo"] == "constante":
                    expr = sp.Integer(img_data["c"])
                
                # Passamos o título e se deve esconder a legenda
                plotar_funcao(expr, titulo=titulo_grafico, esconder_legenda=esconder)
                
            else:
                st.markdown("""
                <div class="dica-card">
                    <h4 style="color: #b388ff !important; margin-top:0;">Dica de Estudo</h4>
                    <p>O gráfico de uma função revela seu comportamento. Funções lineares formam retas, enquanto funções quadráticas formam curvas chamadas parábolas.</p>
                </div>
                """, unsafe_allow_html=True)

    # ------------------------------------------
    # MÓDULO 2: LIMITES
    # ------------------------------------------
    elif st.session_state.pagina_atual == "lim":
        with col_quiz:
            st.header("Aula 2: Limites")
            tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
            with tab_teoria:
                st.markdown("""
                * **Indeterminação 0/0:** Exige fatoração.
                * **Limites Laterais:** Esquerda e direita.
                """)
            with tab_pratica:
                if 'lim_q_atual' not in st.session_state:
                    st.session_state.lim_q_atual = None

                questoes_lim = [
                    {"texto": "lim (x→2) de (x² - 4) / (x - 2)", "resp": "4", "expl": "Fatore: (x-2)(x+2)/(x-2). Cancela, sobra x+2. 2+2=4.", "img": {"tipo": "limite", "a": 2}},
                    {"texto": "lim (x→3) de (x² - 9) / (x - 3)", "resp": "6", "expl": "Fatore: (x-3)(x+3)/(x-3). Cancela, sobra x+3. 3+3=6.", "img": {"tipo": "limite", "a": 3}},
                    {"texto": "lim (x→1) de (2x + 5)", "resp": "7", "expl": "Substituição direta: 2(1) + 5 = 7.", "img": {"tipo": "limite", "a": 1}},
                    {"texto": "O limite de uma constante é igual a:", "resp": "Ela mesma", "expl": "Não importa o valor de x, a constante não muda.", "img": {"tipo": "texto"}}
                ]

                if st.button("Sortear Nova Questão", key="btn_sort_lim"):
                    st.session_state.lim_q_atual = random.choice(questoes_lim)
                    st.rerun()

                if st.session_state.lim_q_atual:
                    q = st.session_state.lim_q_atual
                    st.write(f"**{q['texto']}**")
                    
                    opcoes = [q['resp'], "0", "Inexistente", "Ela mesma", "8"]
                    opcoes = sorted(list(set(opcoes)))
                    
                    resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"radio_lim_{q['texto']}")
                    
                    if st.button("Verificar Resposta", key="btn_ver_lim"):
                        if resp_user is None: st.warning("Selecione uma opção.")
                        elif resp_user == q['resp']:
                            st.success("Você acertou!")
                            st.info(f"Passo a passo: {q['expl']}")
                        else:
                            st.error("Você errou.")
                            st.info(f"Resposta correta: {q['resp']}. Passo a passo: {q['expl']}")

        with col_imagem:
            st.write("<br><br>", unsafe_allow_html=True)
            if st.session_state.lim_q_atual and "img" in st.session_state.lim_q_atual:
                img_data = st.session_state.lim_q_atual["img"]
                if img_data["tipo"] == "limite":
                    # Desenha uma função com um "buraco" para representar o limite
                    x_vals = np.linspace(img_data["a"] - 5, img_data["a"] + 5, 400)
                    y_vals = x_vals + img_data["a"] # Exemplo simples de função contínua
                    
                    fig, ax = plt.subplots(figsize=(7, 5))
                    fig.patch.set_facecolor('#1a1a2e'); ax.set_facecolor('#1a1a2e')
                    ax.plot(x_vals, y_vals, color='#b388ff', linewidth=2)
                    ax.scatter([img_data["a"]], [img_data["a"]*2], color='#1a1a2e', edgecolors='#b388ff', s=100, zorder=5, label="Ponto de Interesse")
                    ax.axhline(0, color='#555555'); ax.axvline(0, color='#555555')
                    ax.grid(True, linestyle='--', alpha=0.2)
                    ax.set_title(f"Análise Visual perto de x = {img_data['a']}", color='#e0e0e0')
                    ax.legend(facecolor='#24243a', labelcolor='#e0e0e0')
                    st.pyplot(fig); plt.close(fig)
            else:
                st.markdown("""
                <div class="dica-card">
                    <h4 style="color: #b388ff !important; margin-top:0;">Lembrete de Limites</h4>
                    <p>Sempre tente a substituição direta primeiro. Se der 0/0, use fatoração. Se der número/0, o limite tende ao infinito.</p>
                </div>
                """, unsafe_allow_html=True)

    # ------------------------------------------
    # MÓDULO 3: DERIVADAS
    # ------------------------------------------
    elif st.session_state.pagina_atual == "der":
        with col_quiz:
            st.header("Aula 3: Derivadas")
            tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
            with tab_teoria:
                st.markdown("* **Regra do Tombo:** d/dx (xⁿ) = n * xⁿ⁻¹")
            with tab_pratica:
                if 'der_q_atual' not in st.session_state:
                    st.session_state.der_q_atual = None

                questoes_der = [
                    {"texto": "Qual a derivada de f(x) = x³?", "resp": "3x²", "expl": "Tombo: 3 * x^(3-1) = 3x².", "img": {"tipo": "derivada", "func": "x**3"}},
                    {"texto": "Qual a derivada de f(x) = 5x² + 2x?", "resp": "10x + 2", "expl": "5x² -> 10x. 2x -> 2.", "img": {"tipo": "derivada", "func": "5*x**2 + 2*x"}},
                    {"texto": "Qual a derivada de uma constante (ex: f(x) = 8)?", "resp": "0", "expl": "Constantes não variam, então a derivada é zero.", "img": {"tipo": "texto"}},
                    {"texto": "Qual a derivada de f(x) = x⁴ - 3x?", "resp": "4x³ - 3", "expl": "x⁴ -> 4x³. -3x -> -3.", "img": {"tipo": "derivada", "func": "x**4 - 3*x"}}
                ]

                if st.button("Sortear Nova Questão", key="btn_sort_der"):
                    st.session_state.der_q_atual = random.choice(questoes_der)
                    st.rerun()

                if st.session_state.der_q_atual:
                    q = st.session_state.der_q_atual
                    st.write(f"**{q['texto']}**")
                    
                    opcoes = [q['resp'], "3x²", "10x", "0", "4x³"]
                    opcoes = sorted(list(set(opcoes)))
                    
                    resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"radio_der_{q['texto']}")
                    
                    if st.button("Verificar Resposta", key="btn_ver_der"):
                        if resp_user is None: st.warning("Selecione uma opção.")
                        elif resp_user == q['resp']:
                            st.success("Você acertou!")
                            st.info(f"Passo a passo: {q['expl']}")
                        else:
                            st.error("Você errou.")
                            st.info(f"Resposta correta: {q['resp']}. Passo a passo: {q['expl']}")

        with col_imagem:
            st.write("<br><br>", unsafe_allow_html=True)
            if st.session_state.der_q_atual and "img" in st.session_state.der_q_atual:
                img_data = st.session_state.der_q_atual["img"]
                if img_data["tipo"] == "derivada":
                    # Plota a função original e desenha a reta tangente em um ponto
                    x = sp.Symbol('x')
                    expr = sp.sympify(img_data["func"])
                    f_num = sp.lambdify(x, expr, 'numpy')
                    
                    # Ponto para a reta tangente
                    x0 = 1.5
                    y0 = f_num(x0)
                    deriv = sp.diff(expr, x)
                    deriv_num = sp.lambdify(x, deriv, 'numpy')
                    m = deriv_num(x0)
                    
                    x_vals = np.linspace(-5, 5, 400)
                    y_vals = f_num(x_vals)
                    y_tangente = m * (x_vals - x0) + y0
                    
                    fig, ax = plt.subplots(figsize=(7, 5))
                    fig.patch.set_facecolor('#1a1a2e'); ax.set_facecolor('#1a1a2e')
                    ax.plot(x_vals, y_vals, color='#b388ff', linewidth=2, label="f(x)")
                    ax.plot(x_vals, y_tangente, color='#00e5ff', linestyle='--', label=f"Reta Tangente (x={x0})")
                    ax.scatter([x0], [y0], color='#00e5ff', s=50, zorder=5)
                    ax.axhline(0, color='#555555'); ax.axvline(0, color='#555555')
                    ax.grid(True, linestyle='--', alpha=0.2)
                    ax.set_ylim(-10, 15)
                    ax.set_title("O que a derivada representa?", color='#e0e0e0')
                    ax.legend(facecolor='#24243a', labelcolor='#e0e0e0')
                    st.pyplot(fig); plt.close(fig)
            else:
                st.markdown("""
                <div class="dica-card">
                    <h4 style="color: #b388ff !important; margin-top:0;">Interpretação Geométrica</h4>
                    <p>A derivada de uma função em um ponto é a inclinação da reta tangente à curva naquele ponto.</p>
                </div>
                """, unsafe_allow_html=True)

    # ------------------------------------------
    # MÓDULO 4: INTEGRAIS
    # ------------------------------------------
    elif st.session_state.pagina_atual == "int":
        with col_quiz:
            st.header("Aula 4: Integrais")
            tab_teoria, tab_pratica = st.tabs(["Teoria", "Prática (Quiz)"])
            with tab_teoria:
                st.markdown("* **Integral de xⁿ:** (xⁿ⁺¹) / (n+1) + C")
            with tab_pratica:
                if 'int_q_atual' not in st.session_state:
                    st.session_state.int_q_atual = None

                questoes_int = [
                    {"texto": "Calcule a integral: ∫ 2x dx", "resp": "x² + C", "expl": "2x -> 2x²/2 = x². Adicione C.", "img": {"tipo": "integral", "func": "2*x"}},
                    {"texto": "Calcule a integral: ∫ x² dx", "resp": "x³/3 + C", "expl": "x² -> x³/3. Adicione C.", "img": {"tipo": "integral", "func": "x**2"}},
                    {"texto": "Calcule a integral: ∫ 5 dx", "resp": "5x + C", "expl": "Constante * x. Adicione C.", "img": {"tipo": "integral", "func": "5"}},
                    {"texto": "A integral definida de 0 a 2 de 2x dx vale:", "resp": "4", "expl": "A primitiva é x². Avaliando de 0 a 2: 2² - 0² = 4.", "img": {"tipo": "area", "func": "2*x"}}
                ]

                if st.button("Sortear Nova Questão", key="btn_sort_int"):
                    st.session_state.int_q_atual = random.choice(questoes_int)
                    st.rerun()

                if st.session_state.int_q_atual:
                    q = st.session_state.int_q_atual
                    st.write(f"**{q['texto']}**")
                    
                    opcoes = [q['resp'], "x² + C", "5x + C", "4", "x³/3"]
                    opcoes = sorted(list(set(opcoes)))
                    
                    resp_user = st.radio("Sua resposta:", opcoes, index=None, key=f"radio_int_{q['texto']}")
                    
                    if st.button("Verificar Resposta", key="btn_ver_int"):
                        if resp_user is None: st.warning("Selecione uma opção.")
                        elif resp_user == q['resp']:
                            st.success("Você acertou!")
                            st.info(f"Passo a passo: {q['expl']}")
                        else:
                            st.error("Você errou.")
                            st.info(f"Resposta correta: {q['resp']}. Passo a passo: {q['expl']}")

        with col_imagem:
            st.write("<br><br>", unsafe_allow_html=True)
            if st.session_state.int_q_atual and "img" in st.session_state.int_q_atual:
                img_data = st.session_state.int_q_atual["img"]
                if img_data["tipo"] == "integral" or img_data["tipo"] == "area":
                    x = sp.Symbol('x')
                    expr = sp.sympify(img_data["func"])
                    
                    if img_data["tipo"] == "area":
                        # Plota a área definida
                        plotar_funcao(expr, x_min=0, x_max=2, titulo="Área sob a Curva (de 0 a 2)", preencher_area=True)
                    else:
                        # Plota a função original
                        plotar_funcao(expr, titulo="Função a ser integrada")
            else:
                st.markdown("""
                <div class="dica-card">
                    <h4 style="color: #b388ff !important; margin-top:0;">Não esqueça o + C!</h4>
                    <p>Nas integrais indefinidas, a constante C representa todas as possíveis constantes que desapareceram ao derivar.</p>
                </div>
                """, unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: #3a3a5a;'><p style='text-align: center; color: #666; font-size: 0.9rem;'>Desenvolvido como projeto acadêmico.</p>", unsafe_allow_html=True)
import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random

# ==========================================
# CONFIGURAÇÃO INICIAL DA PÁGINA
# ==========================================
st.set_page_config(page_title="Quiz de Matemática", page_icon="🧮", layout="wide")

st.title("🧮 Quiz Interativo de Matemática")
st.markdown("""
Bem-vindo ao seu projeto de matemática! 
Este quiz foi criado para cobrir os 4 módulos obrigatórios: **Funções, Limites, Derivadas e Integrais**.
Responda à pergunta e veja a explicação passo a passo!
""")

# ==========================================
# FUNÇÃO AUXILIAR PARA GRÁFICOS (CORRIGIDA)
# ==========================================
def plotar_funcao(expr_sympy, x_min=-10, x_max=10, titulo="Gráfico"):
    # O sympy precisa ser convertido para uma função numérica do numpy
    x = sp.Symbol('x')
    f_num = sp.lambdify(x, expr_sympy, 'numpy')
    
    # Gera os pontos do eixo X e calcula o Y
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = f_num(x_vals)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_vals, y_vals, label=f"f(x)", color='#1f77b4', linewidth=2)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title(titulo)
    ax.legend()
    st.pyplot(fig)
    plt.close(fig) # Fecha a figura para não gastar memória

# ==========================================
# BARRA LATERAL
# ==========================================
st.sidebar.header("Escolha o Módulo")
modulo = st.sidebar.radio(
    "Selecione o conteúdo que deseja praticar:",
    ("Aula 1: Funções", "Aula 2: Limites", "Aula 3: Derivadas", "Aula 4: Integrais")
)

st.sidebar.markdown("---")
st.sidebar.info("Projeto desenvolvido para a disciplina de Cálculo. Use o VS Code e Streamlit.")

# ==========================================
# MÓDULO 1: FUNÇÕES
# ==========================================
if modulo == "Aula 1: Funções":
    st.header("Aula 1: Funções")
    st.write("**Requisito:** Identificar tipo, domínio, imagem e representação gráfica.")
    
    # Inicializa os coeficientes uma única vez na memória
    if 'a_func' not in st.session_state:
        st.session_state.a_func = random.randint(1, 5)
        st.session_state.b_func = random.randint(-5, 5)
        
    a = st.session_state.a_func
    b = st.session_state.b_func
    
    # Formatação bonita
    sinal = "+" if b >= 0 else "-"
    texto_funcao = f"{a}x {sinal} {abs(b)}"
    
    st.write(f"Considere a função afim: **f(x) = {texto_funcao}**")
    
    resposta_correta = (a * 3) + b
    
    # Gerando as opções
    opcoes = [str(resposta_correta), str(resposta_correta + 3), str(resposta_correta - 2), str(resposta_correta + 10)]
    opcoes = sorted(list(set(opcoes))) # Remove duplicatas e ordena
    opcoes.insert(0, "Selecione...")
    
    pergunta = st.radio("Qual é o valor de f(x) quando x = 3?", opcoes)
    
    if st.button("Verificar Resposta", key="btn_func"):
        if pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        elif pergunta == str(resposta_correta):
            st.success(f"✅ **Você acertou!** f(3) = {resposta_correta}.")
            st.info(f"**Explicação:** f(x) = {a}x {sinal} {abs(b)}. Substituindo x=3: f(3) = {a}(3) {sinal} {abs(b)} = {resposta_correta}.")
        else:
            st.error(f"❌ **Você errou.** A resposta correta é {resposta_correta}.")
            st.info(f"**Explicação:** f(x) = {a}x {sinal} {abs(b)}. Substituindo x=3: f(3) = {a}(3) {sinal} {abs(b)} = {resposta_correta}.")
        
        # Gráfico (só aparece após clicar)
        st.write("### Representação Gráfica da Função")
        x = sp.Symbol('x')
        expr = a * x + b
        plotar_funcao(expr, x_min=-10, x_max=10, titulo=f"Gráfico de f(x) = {texto_funcao}")
        
        st.write("**Domínio:** Todos os números reais (ℝ).")
        st.write("**Imagem:** Todos os números reais (ℝ).")

# ==========================================
# MÓDULO 2: LIMITES
# ==========================================
elif modulo == "Aula 2: Limites":
    st.header("Aula 2: Limites")
    st.write("**Requisito:** Aplicar propriedades dos limites e identificar casos de inexistência.")
    
    st.write("Considere a função: **f(x) = (x² - 9) / (x - 3)**")
    st.write("Qual é o limite de f(x) quando x tende a 3?")
    
    pergunta = st.radio("Escolha uma opção:", ["Selecione...", "0", "6", "Inexistente", "3"])
    
    if st.button("Verificar Resposta", key="btn_lim"):
        if pergunta == "6":
            st.success("✅ **Você acertou!** O limite é 6.")
            st.info("**Explicação:**\n1. Substituindo x=3, temos (9-9)/(3-3) = 0/0 (Indeterminação).\n2. Fatoramos o numerador: (x-3)(x+3) / (x-3).\n3. Simplificamos cortando (x-3): fica x+3.\n4. Substituindo x=3: 3+3 = 6.")
        elif pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        else:
            st.error("❌ **Você errou.**")
            st.info("**Explicação:** Ao substituir x=3, temos 0/0. Isso é uma indeterminação. Fatore o numerador: (x-3)(x+3). Cancele o (x-3). O limite é da função x+3 quando x→3, ou seja, 6.")

# ==========================================
# MÓDULO 3: DERIVADAS
# ==========================================
elif modulo == "Aula 3: Derivadas":
    st.header("Aula 3: Derivadas")
    st.write("**Requisito:** Implementar cálculo de derivadas (potência, soma/subtração, quociente).")
    
    st.write("Considere a função: **f(x) = 2x³ + 4x² - 3x + 7**")
    st.write("Qual é a derivada f'(x)?")
    
    pergunta = st.radio("Escolha uma opção:", 
                        ["Selecione...", 
                         "6x² + 8x - 3", 
                         "6x³ + 8x² - 3x", 
                         "2x² + 4x - 3", 
                         "6x² + 8x - 3 + 7"])
    
    if st.button("Verificar Resposta", key="btn_der"):
        if pergunta == "6x² + 8x - 3":
            st.success("✅ **Você acertou!**")
            st.info("**Explicação (Regra da Potência):**\n- Derivada de 2x³: 2 * 3x² = 6x².\n- Derivada de 4x²: 4 * 2x = 8x.\n- Derivada de -3x: -3.\n- Derivada de 7 (constante): 0.")
        elif pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        else:
            st.error("❌ **Você errou.**")
            st.info("**Explicação:** Use a regra do 'tombo' (multiplica pelo expoente e diminui 1 do expoente).\n2x³ -> 6x²\n4x² -> 8x\n-3x -> -3\n7 -> 0\nJuntando tudo: 6x² + 8x - 3.")

# ==========================================
# MÓDULO 4: INTEGRAIS
# ==========================================
elif modulo == "Aula 4: Integrais":
    st.header("Aula 4: Integrais")
    st.write("**Requisito:** Integrais definidas e indefinidas (potência, soma/subtração).")
    
    st.write("Calcule a integral indefinida: **∫ (4x + 5) dx**")
    
    pergunta = st.radio("Escolha uma opção:", 
                        ["Selecione...", 
                         "2x² + 5x + C", 
                         "4x² + 5x + C", 
                         "2x² + 5 + C", 
                         "4x² + 5 + C"])
    
    if st.button("Verificar Resposta", key="btn_int"):
        if pergunta == "2x² + 5x + C":
            st.success("✅ **Você acertou!**")
            st.info("**Explicação:**\n- Integral de 4x: sobe o expoente para 2 e divide por 2 -> 4x²/2 = 2x².\n- Integral de 5: vira 5x.\n- Sempre adicionamos a constante **C** no final.")
        elif pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        else:
            st.error("❌ **Você errou.**")
            st.info("**Explicação:** A integral de uma soma é a soma das integrais.\n∫ 4x dx = (4x²)/2 = 2x²\n∫ 5 dx = 5x\nNão esqueça da constante C. Resultado: 2x² + 5x + C.")

# ==========================================
# RODAPÉ
# ==========================================
st.markdown("---")
st.caption("Desenvolvido como projeto acadêmico. Documentação e código disponíveis no GitHub.")
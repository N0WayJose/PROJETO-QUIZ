import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random

# Configuração da página do site
st.set_page_config(page_title="Quiz de Matemática", page_icon="🧮", layout="wide")

st.title("🧮 Quiz Interativo de Matemática")
st.markdown("""
Bem-vindo ao seu projeto de matemática! 
Este quiz foi criado para cobrir os 4 módulos obrigatórios: **Funções, Limites, Derivadas e Integrais**.
Responda à pergunta e veja a explicação passo a passo!
""")

# --- BARRA LATERAL PARA ESCOLHER O MÓDULO ---
st.sidebar.header("Escolha o Módulo")
modulo = st.sidebar.radio(
    "Selecione o conteúdo que deseja praticar:",
    ("Aula 1: Funções", "Aula 2: Limites", "Aula 3: Derivadas", "Aula 4: Integrais")
)

st.sidebar.markdown("---")
st.sidebar.info("Projeto desenvolvido para a disciplina de Cálculo. Use o VS Code e Streamlit.")

# --- FUNÇÃO AUXILIAR PARA GERAR GRÁFICOS ---
def plotar_funcao(expr, x_min=-10, x_max=10, titulo="Gráfico"):
    x = np.linspace(x_min, x_max, 400)
    f = sp.lambdify(sp.Symbol('x'), expr, 'numpy')
    y = f(x)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, label=f"f(x) = {sp.pretty(expr)}", color='blue')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title(titulo)
    ax.legend()
    st.pyplot(fig)

# --- LÓGICA DOS MÓDULOS ---

# ==========================================
# MÓDULO 1: FUNÇÕES
# ==========================================
if modulo == "Aula 1: Funções":
    st.header("Aula 1: Funções")
    st.write("**Requisito:** Identificar tipo, domínio, imagem e representação gráfica.")
    
    # Gerando um coeficiente aleatório para a função afim (linear)
    a = random.randint(1, 5)
    b = random.randint(-5, 5)
    
    st.write(f"Considere a função afim (linear): **f(x) = {a}x + {b}**")
    
    pergunta = st.radio("Qual é o valor de f(x) quando x = 3?", 
                        ["Selecione...", str(a*3 + b), str(a*3 - b), str(a + b), str(a*3 + b + 5)])
    
    if st.button("Verificar Resposta"):
        resposta_correta = a*3 + b
        if pergunta == str(resposta_correta):
            st.success(f"✅ **Você acertou!** f(3) = {a}(3) + {b} = {resposta_correta}.")
        elif pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        else:
            st.error(f"❌ **Você errou.** A resposta correta é {resposta_correta}.")
            st.info(f"**Explicação:** Para calcular f(3), substituímos o 'x' por 3 na equação: f(3) = {a} * 3 + {b} = {resposta_correta}.")
        
        # Mostrando o gráfico exigido
        st.write("### Representação Gráfica da Função")
        x_sym = sp.Symbol('x')
        expr = a * x_sym + b
        plotar_funcao(expr, titulo=f"Gráfico de f(x) = {a}x + {b}")
        
        st.write(f"**Domínio:** Todos os números reais (ℝ).")
        st.write(f"**Imagem:** Todos os números reais (ℝ), pois é uma reta infinita.")

# ==========================================
# MÓDULO 2: LIMITES
# ==========================================
elif modulo == "Aula 2: Limites":
    st.header("Aula 2: Limites")
    st.write("**Requisito:** Aplicar propriedades dos limites e identificar casos de inexistência.")
    
    # Limite simples de substituição direta ou fatoração
    st.write("Considere a função: **f(x) = (x² - 4) / (x - 2)**")
    st.write("Qual é o limite de f(x) quando x tende a 2?")
    
    pergunta = st.radio("Escolha uma opção:", 
                        ["Selecione...", "0", "4", "Inexistente (Indeterminação 0/0)", "Infinito"])
    
    if st.button("Verificar Resposta"):
        if pergunta == "4":
            st.success("✅ **Você acertou!** O limite é 4.")
            st.info("**Explicação (Passo a passo):**\n1. Substituindo x=2, temos (4-4)/(2-2) = 0/0 (Indeterminação).\n2. Fatoramos o numerador: (x-2)(x+2) / (x-2).\n3. Simplificamos cortando o (x-2): fica x+2.\n4. Substituímos x=2: 2+2 = 4.")
        elif pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        else:
            st.error("❌ **Você errou.**")
            st.info("**Explicação:** Ao substituir x=2, obtemos 0/0. Isso não significa que o limite não existe, mas que precisamos fatorar! A expressão fatorada é (x-2)(x+2)/(x-2) = x+2. Logo, o limite quando x→2 é 4.")

# ==========================================
# MÓDULO 3: DERIVADAS
# ==========================================
elif modulo == "Aula 3: Derivadas":
    st.header("Aula 3: Derivadas")
    st.write("**Requisito:** Implementar cálculo de derivadas (potência, soma/subtração, quociente).")
    
    st.write("Considere a função: **f(x) = 3x³ + 2x² - 5x + 1**")
    st.write("Qual é a derivada f'(x)?")
    
    pergunta = st.radio("Escolha uma opção:", 
                        ["Selecione...", 
                         "9x² + 4x - 5", 
                         "9x³ + 4x² - 5x", 
                         "6x² + 4x - 5", 
                         "3x² + 2x - 5"])
    
    if st.button("Verificar Resposta"):
        if pergunta == "9x² + 4x - 5":
            st.success("✅ **Você acertou!**")
            st.info("**Explicação (Regras de derivação):**\n- **Regra da potência:** A derivada de x³ é 3x². Multiplicando pela constante 3, temos 9x².\n- A derivada de x² é 2x. Multiplicando por 2, temos 4x.\n- A derivada de -5x é -5.\n- A derivada de 1 (constante) é 0.")
        elif pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        else:
            st.error("❌ **Você errou.**")
            st.info("**Explicação:** Aplique a regra do tombo (potência):\n- 3x³ vira 3 * 3x² = 9x²\n- 2x² vira 2 * 2x = 4x\n- -5x vira -5\n- 1 vira 0\nResultado: 9x² + 4x - 5")

# ==========================================
# MÓDULO 4: INTEGRAIS
# ==========================================
elif modulo == "Aula 4: Integrais":
    st.header("Aula 4: Integrais")
    st.write("**Requisito:** Integrais definidas e indefinidas (potência, soma/subtração).")
    
    st.write("Calcule a integral indefinida: **∫ (2x + 3) dx**")
    
    pergunta = st.radio("Escolha uma opção:", 
                        ["Selecione...", 
                         "x² + 3x + C", 
                         "2x² + 3x + C", 
                         "x² + 3 + C", 
                         "2x² + 3 + C"])
    
    if st.button("Verificar Resposta"):
        if pergunta == "x² + 3x + C":
            st.success("✅ **Você acertou!**")
            st.info("**Explicação:**\n- Integral de 2x: sobe o expoente para 2 e divide pelo novo expoente: 2x²/2 = x².\n- Integral de 3: vira 3x.\n- Sempre adicionamos a constante de integração **C** no final para integrais indefinidas.")
        elif pergunta == "Selecione...":
            st.warning("Por favor, selecione uma opção.")
        else:
            st.error("❌ **Você errou.**")
            st.info("**Explicação:** A integral de uma soma é a soma das integrais.\n∫ 2x dx = 2 * (x²/2) = x²\n∫ 3 dx = 3x\nResultado final: x² + 3x + C (não esqueça do + C!).")

# --- RODAPÉ COM INFORMAÇÕES PARA O README ---
st.markdown("---")
st.caption("Desenvolvido como projeto acadêmico. Documentação e código disponíveis no GitHub.")
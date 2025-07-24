import streamlit as st

st.title("Comparador de Produtos de Cosméticos")

st.write("Insira abaixo as informações das opções que deseja comparar.")

num_opcoes = st.number_input("Quantas opções de produto você quer comparar?", min_value=2, max_value=10, value=2)

dados = []

for i in range(num_opcoes):
    st.subheader(f"Opção {i+1}")
    preco = st.number_input(f"Preço (R$) da opção {i+1}", min_value=0.0, format="%.2f")
    volume = st.number_input(f"Volume (ml) da opção {i+1}", min_value=1.0, format="%.2f")
    frete = st.number_input(f"Frete (R$) da opção {i+1}", min_value=0.0, format="%.2f")
    preco_total = preco + frete
    preco_por_ml = preco_total / volume
    dados.append({
        "Opção": f"Opção {i+1}",
        "Preço Total (R$)": round(preco_total, 2),
        "Preço por ml (R$)": round(preco_por_ml, 4)
    })

# Exibe resultado
st.subheader("Resultado da Comparação")
dados_ordenados = sorted(dados, key=lambda x: x["Preço por ml (R$)"])
for d in dados_ordenados:
    st.write(f"{d['Opção']}: R${d['Preço por ml (R$)']} por ml (Total: R${d['Preço Total (R$)']})")

st.success(f"A opção mais econômica é: **{dados_ordenados[0]['Opção']}**")

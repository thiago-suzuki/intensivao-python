import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
print(tabela)

print(tabela.info())
tabela = tabela.dropna()
print(tabela.info())

print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

print(tabela["duracao_contrato"].value_counts(normalize=True))
print(tabela["duracao_contrato"].value_counts())

print(tabela.groupby("duracao_contrato").mean(numeric_only=True))

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
print(tabela)
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

print(tabela["assinatura"].value_counts(normalize=True))
print(tabela.groupby("assinatura").mean(numeric_only=True))

import plotly.express as px
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

tabela = tabela[tabela["ligacoes_callcenter"]<5]
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela)
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
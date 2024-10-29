import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("ecommerce_preparados_analisados.csv")

#Gráfico de Histograma - Nota
plt.figure(figsize=(10, 6))
sns.histplot(df['nota'], bins=20, kde=True)
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.show()
#Gráfico de Histograma - Número de Qtd de Avaliações
plt.figure(figsize=(10, 6))
sns.histplot(df['N_avaliações'], bins=20, kde=True)
plt.title('Número de Qtd de Avaliações')
plt.xlabel('Número de Avaliações')
plt.ylabel('Frequência')
plt.show()

#Gráfico de Dispersão - Preço vs Qtd Vendida / Gênero
print("Nomes das colunas no DataFrame:")
print(df.columns)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Preço', y='Qtd_Vendidos', hue='Genero', alpha=0.7)
plt.title('Gráfico de Dispersão: Preço vs Qtd Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.legend(title='Gênero')
plt.grid(True)
plt.show()

#Gráfico Mapa de Calor
heatmap_data = df[['Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax']]
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data.corr(), annot=True, cmap="YlGnBu", cbar_kws={'label': 'Correlação'})
plt.title("Mapa de Calor das Correlações das Métricas Normalizadas")
plt.show()

#Gráfico de Barra
marca_avaliacoes = df.groupby('Marca')['N_avaliações'].mean().nlargest(10).sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(x=marca_avaliacoes, y=marca_avaliacoes.index, hue=marca_avaliacoes.index, dodge=False, legend=False, palette="viridis")
plt.title("Top 10 Marcas com Maior Média de Avaliações")
plt.xlabel("Média de Avaliações")
plt.ylabel("Marca")
plt.show()

#Gráfico de Pizza
material_counts = df['Material'].value_counts().nlargest(5)
plt.figure(figsize=(8, 8))
plt.pie(material_counts, labels=material_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Proporção dos 5 Principais Materiais dos Produtos")
plt.show()

#Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço_MinMax'], fill=True, color="blue")
plt.title("Distribuição de Densidade dos Preços Normalizados")
plt.xlabel("Preço (Normalizado)")
plt.ylabel("Densidade")
plt.show()

#Gráfico de Regressão - Relação entre Desconto e Preço
plt.figure(figsize=(18, 15))
plt.subplot(3, 1, 2)
sns.regplot(x='Desconto', y='Preço_MinMax', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'blue'})
plt.title("Relação entre Percentual de Desconto e Preço (Normalizado)")
plt.xlabel("Percentual de Desconto")
plt.ylabel("Preço (Normalizado)")
plt.tight_layout()
plt.show()
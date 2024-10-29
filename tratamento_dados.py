import pandas as pd

df = pd.read_csv("ecommerce_preparados.csv")

pd.set_option("display.width", None)
print(df.head())
print(df.tail())

print("Análise de dados nulos:") #Análise de dados nulos
print(df.isnull().sum())

df = df.dropna() #Exclusão dos dados nulos
print("Dados nulos removidos.")

print("\nAnálise de dados duplicados:") #Análise de dados duplicados
print(f"Total de linhas duplicadas: {df.duplicated().sum()}")

df = df.drop_duplicates() #Exclusão de dados duplicados
print("Dados duplicados removidos.")

print("\nAnálise de dados únicos:") #Análise de dados únicos
print("Número de valores únicos por coluna:")
print(df.nunique())

print("\nEstatísticas dos dados:") #Estatísticas dos dados
print(df.describe())

#Renomear colunas específicas
colunas_renomeadas = {
    "Título": "Titulo",
    "Nota": "nota",
    "N_Avaliações": "N_avaliações",
    "Desconto": "Desconto",
    "Marca": "Marca",
    "Gênero": "Genero",
    "Temporada": "Temporada",
    "Qtd_Vendidos": "Qtd_Vendidos",
    "Preço": "Preço"
}

df = df.rename(columns=colunas_renomeadas) #Renomear apenas as colunas que estão no dicionário

#Selecionar e exibir as colunas específicas
colunas_para_visualizar = [
    "Titulo", "nota", "N_avaliações", "Desconto", "Marca",
    "Genero", "Temporada", "Qtd_Vendidos", "Preço"
]
print("\nVisualização das colunas específicas:")
print(df[colunas_para_visualizar].head())
print(df[colunas_para_visualizar].tail())

df.to_csv("ecommerce_preparados_analisados.csv", index=False)

print("\nArquivo salvo como 'ecommerce_preparados_analisados.csv'.")
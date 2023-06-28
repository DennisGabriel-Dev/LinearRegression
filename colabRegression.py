import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados de exemplo
idade = np.array([18, 23, 25, 33, 34, 43, 48, 51, 58, 63, 67]).reshape(-1, 1)
custo = np.array([871, 1100, 1393, 1654, 1915, 2100, 2356,2698, 2959, 3000, 3100])

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo com os dados
modelo.fit(idade, custo)


# Plotando o gráfico de dispersão e a linha de regressão
plt.scatter(idade, custo, color='blue', label='Cordenadas dos dados')
plt.plot(idade, modelo.predict(idade), color='red', linewidth=2, label='Regressão Linear')
plt.xlabel('Idade')
plt.ylabel('Custo')
plt.title('Regressão Linear - Previsão de Preço de Plano de Saúde')
plt.legend()
plt.show()

# Fazendo uma previsão para o custo com nova(s) idade(s)
import csv
from google.colab import files

op = 's'
idade_analisada = []

# Salvando as idades analisadas em um arquivo CSV
nome_arquivo = 'idades_analisadas.csv'
def baixarDados():
  with open(nome_arquivo, mode='w', newline='') as arquivo:
      escritor = csv.writer(arquivo)
      escritor.writerow(['Idade', 'Custo'])
      escritor.writerows(idade_analisada)

  # Baixando o arquivo CSV
  files.download(nome_arquivo)

while op == 's':
    nova_idade = np.array([[int(input("Digite a Idade a ter o custo previsto: "))]])  # Nova idade para prever o custo
    custo_previsto = modelo.predict(nova_idade)

    # Adicionando idade e custo a uma lista
    idade_analisada.append([nova_idade[0][0], np.round(custo_previsto, 2)[0]])

    # Imprimindo o preço previsto
    print(f"O custo previsto para {nova_idade[0][0]} anos é: R${np.round(custo_previsto,2)[0]}")
    print('--------------------------')

    op = input('Deseja analisar outra idade? (s/n) ').lower()
    if op == 'n':
        acao = input("Você quer fazer o download dos dados analisados em .csv? (s/n)").lower()
        if(acao == 's'):
          baixarDados()
        print('Programa encerrado!')
        break
    else:
        continue


###########################################
############ FIM DO 1º CÓDIGO #############
###########################################
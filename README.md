 # Projeto Regressão Linear 

 Nesse projeto importei o módulo "LinearRegression" da biblioteca externa chamada sklearn(https://scikit-learn.org/), e a biblioteca matplotlib(https://matplotlib.org/).

 Nessa resolução o gráfico é apresentado, e em seguida é pedido uma idade para ser analisada na regressão, em seguida,
é retornado um valor(custo) adequado para o plano de saúde da idade informada. <br> Observação: é preciso rodar no colab("https://colab.research.google.com/") ou jupyter-lab("https://jupyter.org/install")<br> para uma análise adequada.<br> Caso queira usar o jupyter(mais rápido) você deve instalar algumas bibliotecas: numpy, matplotlib e sklearn, além do próprio jupyter.

 Obs: SE, SOMENTE SE, VOCÊ ESTIVER USANDO O JUPYTER rode os seguintes comandos no seu terminal(você precisa do python instalado):
```bash
 python -m pip install -U pip
 pip install numpy python
 pip install -U matplotlib
 pip install -U scikit-learn
```
 ou para baixar tudo de uma vez: 
```bash
pip install numpy matplotlib scikit-learn
```
 Caso você use o Colab, não é preciso baixar nenhuma ferramenta.

O CÓDIGO A SEGUIR é ideal para o COLAB, pois ele tem recursos de download de um arquivo .csv no final da análise, usando libs do Google Colab.

## Código 1(Colab):
```python
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
```

## O 2º código agora é ideal para o Jupyter.
Pensando na rapidez, e não excluindo a QA(Qualidade de Software)<br>
do código anterior, esse tem a mesma capacidade de salvar um arquivo .csv na sua máquina, mas ao invés de perguntar a<br>
pasta que você deseja baixar, ele salva automaticamente na mesma pasta do seu arquivo do jupyter.<br>
```python
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
#from google.colab import files

op = 's'
idade_analisada = []

# Salvando as idades analisadas em um arquivo CSV
nome_arquivo = 'idades_analisadas.csv'
def baixarDados():
  with open(nome_arquivo, mode='a', newline='') as arquivo:
      escritor = csv.writer(arquivo)
      escritor.writerow(['Idade', 'Custo'])
      escritor.writerows(idade_analisada)


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
            print(f'Arquivo {nome_arquivo} foi salvo na pasta do seu ipynb notebook!')
        print('Programa encerrado!')
        break
    else:
        continue

###########################################
############ FIM DO 2º CÓDIGO #############
###########################################
```

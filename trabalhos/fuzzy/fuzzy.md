Soft Computing

https://towardsdatascience.com/fuzzy-logic-and-how-it-is-curing-cancer-dc6bcc961ded

<img src="img/001.png" align="center" height=auto width=80%/>

# Lógica Fuzzy
O termo difuso se refere a coisas que não são claras ou coisas vagas. No mundo real, muitas vezes encontramos uma situação em que não podemos determinar se o estado é True ou False; 

No valor True do sistema booleano, 1.0 representa o valor verdadeiro absoluto e 0.0 representa o valor False absoluto. Mas no sistema difuso, não há lógica para True absoluta e valor False absoluto. Mas na lógica fuzzy, há um valor intermediário muito presente que é parcialmente verdadeiro e parcialmente falso.

<img src="img/03.png" align="center" height=auto width=80%/>

https://colab.research.google.com/drive/13nqdB-kHLIMUxemuQJfnV1bqrLzM3hPS
https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html
https://share.cocalc.com/share/25212860c43c41742e304949bb53b63290e6d71a/Fuzzy%20logic/Exemplo%20-%20Criminalistica%20-%20skfuzzy.ipynb?viewer=share
http://monografias.poli.ufrj.br/monografias/monopoli10017168.pdf

<br/>
<br/>
<br/>

## Diferença entre um conjunto clássico e um conjunto fuzzy
A lógica fuzzy está intimamente relacionada aos conjuntos, assim como a lógica bivariada tradicional. Na verdade, os conjuntos clássicos são subconjuntos de conjuntos difusos. Isso significa que a lógica bivariada são casos especiais de lógica difusa.


<img src="img/11_fuzzy_and_crisp.png" align="center" height=auto width=80%/>

os conjuntos fuzzy permitem que os elementos pertençam a um determinado conjunto com um certo grau - pertinência parcial.

### Vantagens do Sistema de Lógica Fuzzy
- A lógica difusa faz com que as decisões tomadas pela máquina se aproximem cada vez mais das decisões humanas.
- A estrutura dos Sistemas de Lógica Fuzzy é fácil e compreensível
- A lógica difusa é amplamente utilizada para fins comerciais e práticos
- Pode não oferecer um raciocínio preciso, mas o único raciocínio aceitável
- Fornece uma solução mais eficaz para problemas complexos

### Desvantagens dos Sistemas de Lógica Fuzzy
- A lógica difusa nem sempre é precisa, portanto, os resultados são percebidos com base em suposições, portanto, podem não ser amplamente aceitos.
- Definir regras exatas e difusas e funções de associação é uma tarefa difícil
- Alguma lógica de tempo difuso é confundida com a teoria da probabilidade e os termos

### Área Financeira
- Controle de transferência de notas
- Gestão de fundos
- Previsões do mercado de ações
- Sistemas de decisão para negociação de títulos

## Conceitos
### Conjutos Fuzzy
Um conjuto difuso não tem bem definido o que são os limites.

<img src="img/01.png" align="center" height=auto width=80%/>

Conjuntos Clássicos X Conjuntos Fuzzy 

<br/>
<br/>
<br/>

Um Conjunto Fuzzy é um conjunto cuja função de pertinência não é determinística e sim probabilística. Por exemplo:

<img src="img/02.png" align="center" height=auto width=100%/>

Conjuntos Clássicos X Conjuntos Fuzzy 

Para um trabalhador o final de semana começa no sábado e vai até domingo mas para um estudante universitário o final de semana pode começar a partir de quinta, por exemplo, ao invés  de ter 5 aulas, na quinta ele tem 3 depois na sexta ele tem 2 aulas e no domingo ele faz um trabalho.

Exemplo de conjuto clássico X conjunto fuzzy

– No Conjunto CLÁSSICO uma pessoa com 1.70 não pertence ao conjunto de
pessoas altas (pertence com grau de pertinência 0).
– No Conjunto FUZZY abaixo uma pessoa com 1.70 pertence ao conjunto de
pessoas altas com pertinência 0.8.

<img src="img/06.png" align="center" height=auto width=100%/>

<img src="img/07.png" align="center" height=auto width=100%/>
<img src="img/09.png" align="center" height=auto width=100%/>


### Variável linguistica
**A lógica fuzzy baseia-se em palavras** e não em números, ou seja, os valores verdades são expressos lingüisticamente.
Exemplo: baixo, médio, alto, quente, frio, ...., e outros usados
para definir estados de uma variável.

<img src="img/04.png" align="center" height=auto width=100%/>

<img src="img/05.png" align="center" height=auto width=100%/>


## Terminologia

<img src="img/10.png" align="center" height=auto width=100%/>

### Grau de Pertinência
Como descrito anteriormente, o valor de pertinência determina o quanto um objeto pertence a um Conjunto Fuzzy. Assim sendo, um “Conjunto Fuzzy é caracterizado por uma função de pertinência que mapeia os elementos de um
domínio, espaço ou universo de discurso X para o um dado intervalo” (ZADEH, 1965), normalmente assumido entre 0 e 1 [0,1]. 

#### Funções de pertinência
```python

# plot the gaussian pdf
from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm
# define the distribution parameters
sample_space = arange(-5, 5, 0.001)
mean = 0.0
stdev = 1.0
# calculate the pdf
pdf = norm.pdf(sample_space, mean, stdev)
# plot
pyplot.plot(sample_space, pdf)
pyplot.show()
```

<img src="img/gaussian.png" align="center" height=auto width=100%/>

```python
# plot the gaussian cdf
from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm
# define the distribution parameters
sample_space = arange(-5, 5, 0.001)
# calculate the cdf
cdf = norm.cdf(sample_space)
# plot
pyplot.plot(sample_space, cdf)
pyplot.show()
```

<img src="img/sigmoid.png" align="center" height=auto width=100%/>

<img src="img/trapeziodal.png" align="center" height=auto width=100%/>



#### 7 etapas para calcular os nomes FIS (Fuzzy Inference System) para chegar a uma saída
1. Um conjunto de regras difusas deve ser inferido - Base de regras.
2. Funções de associação de entrada fuzzyifying- Banco de dados.
3. Estabelecendo força de regra difusa - Unidade de Tomada de Decisão.
4. Combinando força de regra e unidade de tomada de decisão de função de associação de saída.
5. Obtendo distribuição de saída da unidade de interface de conseqüências Fuzzification.
6. Ativação de kernel por meio de regras de produção fuzzy - Programação baseada em regras.
7. Distribuição de saída de defuzzyfying com centro de massa - Unidade de interface de defuzzyfying.


FuzzyNet é o modelo matemático mais proeminente para estabelecer Modelos Fuzzy e protótipos no sistema de negociação. O sistema de negociação funciona na Implicação (valor mínimo), Agregação (valor máximo) e na defuzzyfication que opera no centro de gravidade.

A lógica difusa, juntamente com a tecnologia de rede neural, é amplamente utilizada em negociações e finanças para quantificar o risco operacional envolvido nas transações de mercado. A lógica difusa foi implementada na área de aprendizado de máquina e inteligência de investimento especificamente para sistemas de negociação.





- neuro-fuzzy

#### References
- [1] https://www.geeksforgeeks.org/fuzzy-logic-introduction/
- [2] https://www.ime.usp.br/~adao/LOGICAFUZZY2017F.pdf
































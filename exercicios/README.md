
# EXERCÍCIOS

### 1. Responda Verdadeiro ou Falso<br/>
a. ( ) A busca em profundidade sempre acha a solução para um problema em menos tempo que a busca em largura.<br/>
b. ( ) A busca em gulosa é uma busca heurística em que a função de custo do caminho é igual a zero.<br/>
c. ( ) Na busca bidirecional uma das buscas necessita ser em largura.<br/>
d. ( ) Os mecanismos de busca heurística sempre acham a solução ótima.<br/>
e. ( ) Uma heurística admissível garante que o A* ache a solução ótima.<br/>
f. ( ) Dadas duas heurísticas admissíveis h1 e h2 tal que h1 > h2. Usando h1 expandiremos mais nós na árvore de busca.


a) FALSO. Dependendo do nivel de profundidade a busca em profundidade pode nem encontrar a solucao.<br/>
b) FALSO. A busca gulosa se dá pelo maior valor heurístico entre os passos alcançaveis, logo seus passos tem valor heuristico.<br/>
c) FALSO. É possível utilizar estratégias de busca diferentes ou iguais em cada direção de busca.<br/>
Ex) largura x largura, profundidade x profundidade, ...<br/>
d) FALSO. A busca gulosa é um mecanismo de busca heuristica que não garante a solução ótima.<br/>
e) VERDADEIRO. A otimalidade de A* depende de h(n). A busca será ótima se h(n) for admissível e consistente.<br/>
f) FALSO. A árvore de busca será expandida com h(n) <= h*(n) onde h*(n) é o custo real do caminho. Logo tende-se a ter menos nós quando o valor de h(n) sobe.<br/>

---
## RESUMO
### Algoritmos de busca:

#### Uninformed Search
* Tipos de Busca Cega
    * Busca em largura
    * Busca pelo custo uniforme
    * Busca em profundidade
    * Busca em profundidade limitada
    * Busca por aprofundamento iterativo
    * Busca bidirecional (larg x larg, profun x profund, larg x profund, profund x larg)

#### Informed Search
* A*
* Greedy Search

#### Informed Search

* Hill climbing
* Simulated Annealing

---
### 2. Defina com suas próprias palavras inteligência, inteligência artificial, conhecimento e raciocínio.

**Inteligência:** é a capacidade de planejar, raciocinar e aprender utilizando o conhecimento.<br/>
**Inteligência Artificial:** é a utilização da inteligência em modelos computacionais.<br/>
**Conhecimento:** é uma informação com um propósito.<br/>
**Raciocínio:** é uma capacidade de resolver problemas. Um raciocínio pode ser:
- Dedutivo: determinar conclusão
- Indutivo: determinar regras
- Abdutivo: determinar premissas

---
### 3. Como a linguagem RDF pode ser classificada e descrita em termos de uma representação de conhecimento?

RDF é uma linguagem para manipulação de documentos XML e que serve para chegar em níveis da web semântica. Pode ser descrita como um modelo de dados para representar meta-dados e descrever informações acessíveis por máquinas.

---
### 4. Por que é difícil modelar o conhecimento de senso comum? Qual estratégia (representação de conhecimento, formas de aciocínio) você utilizaria?
A ontologia pode ser definida como um conjunto de conceitos para descrever áreas de conhecimento.......

A melhor estratégia seria modelar com uma ontologia genérica para construir teorias básicas do mundo que sejam aplicáveis a qualquer domínio.

---
### 7. Represente de forma adequada a solução do problema abaixo :
Um fazendeiro quer atravessar um rio junto com seu lobo de estimação, uma ovelha e um
repolho bem grande. Tem a seu dispor um barco que por restrições de peso e tamanho só
suporta a travessia com o fazendeiro e mais um dos outros 3 seres vivos. Considerando que o
barco necessita do homem para fazer a travessia, como o fazendeiro deve proceder de modo a
que o lobo não fique sozinho (sem o fazendeiro) com a ovelha e a ovelha não fique sozinha
(sem o fazendeiro) com o repolho ?

- barco = [fazendeiro]
- Fila_margem_origem = [lobo, ovelha, repolho]
- Fila_margem_chegada = []<br/>

**1º passo)** Tirar a ovelha da Fila_margem_origem.<br/>
**2º passo)** atravesar a **ovelha**.<br/>
**3º passo)** Inserir a ovelha na Fila_margem_chegada.<br/>
**4º passo)** voltar vazio.<br/>
Fila_margem_origem = [lobo, repolho]<br/>
Fila_margem_chegada = [ovelha]<br/>
barco = [fazendeiro]

**5º passo)** Tirar o lobo da Fila_margem_origem.<br/>
**6º passo)** atravesar o lobo.<br/>
**7º passo)** Inserir o lobo na Fila_margem_chegada.<br/>
**8º passo)** voltar com a ovelha.<br/>
Fila_margem_origem = [repolho]<br/>
Fila_margem_chegada = [lobo]<br/>
barco = [fazendeiro, ovelha]


**9º passo)** Inserir a ovelha NOVAMENTE na Fila_margem_origem.<br/>
**10º passo)** Tirar o repolho da Fila_margem_origem.<br/>
**11º passo)** atravesar o repolho.<br/>
**12º passo)** voltar vazio.<br/>
Fila_margem_origem = [ovelha]<br/>
Fila_margem_chegada = [lobo, repolho]<br/>
barco = [fazendeiro]

**13º passo)** Tirar a ovelha da Fila_margem_origem.<br/>
**14º passo)** atravesar a ovelha.<br/>
**15º passo)** Inserir a ovelha na Fila_margem_chegada.<br/>
Fila_margem_origem = []<br/>
Fila_margem_chegada = [lobo, repolho, ovelha]<br/>
barco = [fazendeiro]

---
### 8. Realize o procedimento MINIMAX sobre a árvore que representa os ganhos de um jogo para MAX. Indique por quais nós o jogo vai passar se nenhum dos jogadores cometer nenhum erro e quanto MAX vai ganhar ao final do jogo.

<img src="minimax.png" />
H=7, G=0, F=7, E=7, D=5, C=5, B=3, A=5<br/>
Caminho percorrido: A-> C-> D-> (5)

---
## Resumo minimax
- É um algoritmo que tem 2 jogadores:
 - MAX: busca vitória
 - MIN: não quer que o MAX ganhe
- **Funcionamento:** O minimax escolhe os nodos baseados numa pontuação através da função de utilidade que determina se o nível é min ou máx.<br/>
- O root node é sempre máx.
- Faz uma busca em profundidade (busca cega)
- Começa pelo nodo esquerdo
- vídeo que explica o funcionamento do algoritmo de minimax: https://youtu.be/ceU9sNFaSM8

---
### 9. Quais são os módulos que compõem um típico Sistema Especialista e qual a função de cada um deles?
Um agente é composto por:
- sensores para perceber o ambiente 
- atuadores para realizar ações no ambiente

---
### 10. O que são Sistemas Especialistas ou Sistemas Baseados em Conhecimento? Quais são os módulos que compõem um típico Sistema Baseado em Conhecimento? e qual a diferença entre um sistema de raciocínio baseado em Regras, um sistema baseado em Modelos e um sistema baseado em Casos?
São sistemas que empregam o conhecimento humano para resolver problemas que requerem um especialista.
Vide questao 9
SE baseado em regras trabalha com um conjunto de regras, dividindo o problema em subproblemas e testando as soluções para cada regra estabelecida.
SE baseados em modelos tenta representar dispositivos e configurações de dispositivos em um nível casual ou funcional
SE baseado em casos soluciona problemas por meio da utilização de casos anteriormente conhecidos.

---
### 12. Em um sistema multiagente, qual a diferença entre um modelo de cooperação emergente e um modelo comunicativo-cooperativo?
Cooperacao emergente: agentes independentes seguem suas proprias metas e um observador externo tem a aparencia de uma cooperacao.
Comunicativo-cooperativo: os agentes são construídos de modo a cooperar com outros agentes

---
### 13. Um dos propósitos de um SMA é que ele seja capaz de resolver problemas além da capacidade individual de cada agente. Como isso pode ser alcançado? Explique utilizando conceitos de agentes e SMA.
Através da junção de solucionadores de problemas (agentes), podemos ter um sistema que trabalha em conjunto, sendo no caso um sistema multiagente que nada mais é do que uma rede fracamente acoplada de agente autônomos.

---
### 14. Quais as principais caractarísticas de um sistema multiagente que demandam a modelagem de um sistema de cooperação entre os agentes?
Um sistema multiagente é uma rede fracamente acoplada. As principais caracteristicas que demandam a modelagem para este tipo de sistema são:
- Cooperação;
- Resolução de conflitos;
- Negociação;
- Comprometimentos;
- Comunicação;
- Interação.

---
### 15. Qual a importância de padrões para sistemas multiagente? Quais as estratégias da FIPA para promover a interoperabilidade em sistemas multiagente abertos?
É importante para garantir a interoperabilidade entre sistemas. A FIPA estabelece padrões de softwares.



## Resumo sobre agentes
* Um agente é alguma coisa que percebe e age no ambiente. A função de agente para um
agente especifica a ação tomada por um agente em resposta a qualquer sequência de
percepções.
* A medida de performance avalia o comportamento do agente no ambiente. Um agente
racional age para maximizar o valor esperado da medida de performance, dada a sequência
de percepções que ele vê.
* Uma especificação de ambiente inclui uma medida de performance, o ambiente externo, os
atuadores e os sensores. Projetando um agente, o primeiro passo deve sempre ser especificar
o ambiente tão completamente quanto possível.
* Ambientes variam ao longo de várias dimensões significantes. Eles podem ser
completamente ou parcialmente observáveis, determinísticos ou estocásticos, episódicos ou
sequenciais, estáticos ou dinâmicos, discretos ou contínuos e de único agente ou multi
agente.
* O programa do agente implementa a função do agente.
* Agentes reflexivos simples respondem diretamente a percepções, enquanto um agente
reflexivo baseado em modelo mantem um estado interno para rastrear aspectos do mundo
que não são evidentes na percepção atual. Agentes baseados em objetivo agem para
alcançar seus objetivos, e agentes baseados em utilidade tentam maximizar suas próprias
expectativas de “felicidade”.
* Todos os agentes podem melhorar suas performance através de aprendizado.

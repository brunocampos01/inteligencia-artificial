
# EXERCÍCIOS

### 1. Responda Verdadeiro ou Falso<br/>
a. ( ) A busca em profundidade sempre acha a solução para um problema em menos tempo que a busca em largura.<br/>
b. ( ) A busca em gulosa é uma busca heurística em que a função de custo do caminho é igual a zero.<br/>
c. ( ) Na busca bidirecional uma das buscas necessita ser em largura.<br/>
d. ( ) Os mecanismos de busca heurística sempre acham a solução ótima.<br/>
e. ( ) Uma heurística admissível garante que o A* ache a solução ótima.<br/>
f. ( ) Dadas duas heurísticas admissíveis h1 e h2 tal que h1 > h2. Usando h1 expandiremos mais nós na árvore de busca.

---

a) FALSO. Dependendo do nivel de profundidade a busca em profundidade pode nem encontrar a solucao.
b) FALSO. A busca gulosa se dá pelo maior valor heurístico entre os passos alcançaveis, logo seus passos tem valor heuristico.
c) FALSO. É possível utilizar estratégias de busca diferentes em cada direção de busca.
d) FALSO. A busca gulosa é um mecanismo de busca heuristica que não garante a solução ótima.
e) VERDADEIRO. A otimalidade de A* depende de h(n). A busca será ótima se h(n) for admissível e consistente.
f) FALSO. A árvore de busca será expandida com h(n) <= h*(n) onde h*(n) é o custo real do caminho. Logo tende-se a ter menos nós quando o valor de h(n) sobe.

---

### Algoritmos de busca:

#### Uninformed Search
* Tipos de Busca Cega
    * Busca em largura
    * Busca pelo custo uniforme
    * Busca em profundidade
    * Busca em profundidade limitada
    * Busca por aprofundamento iterativo
    * Busca bidirecional

#### Informed Search
* A*
* Greedy Search

#### Informed Search

* Hill climbing
* Simulated Annealing

### 2. Defina com suas próprias palavras inteligência, inteligência artificial, conhecimento e raciocínio.

**Inteligência:** é a capacidade de planejar, raciocinar e aprender utilizando o conhecimento.<br/>
**Inteligência Artificial:** é a utilização da inteligência em modelos computacionais.<br/>
**Conhecimento:** é uma informação com um propósito.<br/>
**Raciocínio:** é uma capacidade de resolver problemas. Um raciocínio pode ser:
- Dedutivo: determinar conclusão
- Indutivo: determinar regras
- Abdutivo: determinar premissas


### 3. Como a linguagem RDF pode ser classificada e descrita em termos de uma representação de conhecimento?

RDF é uma linguagem para manipulação de documentos XML e que serve para chegar em níveis da web semântica. Pode ser descrita como um modelo de dados para representar meta-dados e descrever informações acessíveis por máquinas.

### 4. Por que é difícil modelar o conhecimento de senso comum? Qual estratégia (representação de conhecimento, formas de aciocínio) você utilizaria?
...

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

### 8. Realize o procedimento MINIMAX sobre a árvore que representa os ganhos de um jogo para MAX. Indique por quais nós o jogo vai passar se nenhum dos jogadores cometer nenhum erro e quanto MAX vai ganhar ao final do jogo.

<img src="minimax.png" />
H=7, G=0, F=7, E=7, D=5, C=5, B=3, A=5<br/>
Caminho percorrido: A-> C-> D-> (5)
### Resumo minimax
- É um algoritmo que tem 2 jogadores:
 - MAX: busca vitória
 - MIN: não quer que o MAX ganhe
- **Funcionamento:** O minimax escolhe os nodos baseados numa pontuação através da função de utilidade que determina se o nível é min ou máx.<br/>
- O root node é sempre máx.
- Faz uma busca em profundidade (busca cega)
- Começa pelo nodo esquerdo
- vídeo que explica o funcionamento do algoritmo de minimax: https://youtu.be/ceU9sNFaSM8

Resumo
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

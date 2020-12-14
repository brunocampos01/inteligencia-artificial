# Relatório do trabalho Teórico: Lógica Fuzzy
- **Nome:** Bruno Aurélio Rôzza de Moura Campos
- **Matéria:** INE5633-07238 (20201) - Sistemas Inteligentes

1. **Modele um pequeno sistema difuso para um domínio à sua escolha:**

O domínio utilizado é a tomada de decisão em uma operação de trading. O Sistema fuzzy vai retornar qual a porcentagem de capital que devo inserir em um trade podendo variar entre 0% a 20% do total de capital. Para isso vou utilizar as seguintes características:
- liquidez da ação
- indicador RSI
- trades errados

## a. Mínimo de 4 variáveis contando com a saída, quantidade de conjuntos difusos compatível com o domínio, no mínimo uma variável com 3 conjuntos.

```
nome: x_liquedez_acao 
valores linguisticos: 'baixa', 'regular', 'alta'
conjunto fuzzy: 0 a 2000 compradores e vendedores

nome: x_indicador_rsi
valores linguisticos: 'sobrecompra', 'regiao_briga', 'sobrevenda'
conjunto fuzzy: 0% a 100%

nome: x_trades_errados 
valores linguisticos: 'verde', 'continue', 'limite'
conjunto fuzzy: 0 a 10 operações

nome: y_tamanho_entrada 
valores linguisticos: 'pequeno', 'medio', 'grande'
conjunto fuzzy:0% a 20% do capital total
```

---

## b. Explicar as funções de pertinência utilizadas (utilidade geral da função e o motivo do seu uso no domínio).

### funções de pertinência
- Liquidez de uma ação: essa variável indica se é fácil de entrar e sair da ação, ou seja, se há bastantes compradores e vendedores.
  - x_liquedez_acao_baixa = trapézio
  - x_liquedez_acao_regular = trapézio
  - x_liquedez_acao_alta = trapézio
  - Valores:
    - baixa: 0 a 500 compradores e vendedores é uma liquidez baixa
    - regular: 500 a 700 compradores e vendedores é uma liquidez regular
    - alta: 700 a 2000 compradores e vendedores é uma liquidez alta

- Indicador RSI: é um indicador gráfico que mostra o índice de força relativa. Se estiver numa região de sobrevenda indica compra, se estiver numa região de briga indica para não operar e se estiver numa região de sobrecompra indica venda.
  - x_indicador_rsi_sobrevenda = trapézio
  - x_indicador_rsi_regiao_briga = trapézio
  - x_indicador_rsi_sobrecompra = trapézio
  - Valores:
    - sobrevenda: 0% a 30% começando a queda entre 30% até 40%
    - região de briga: 31% a 69%, começando a alta entre 20% e estabilizando em 30% e começando a queda entre 70% até 80%
    - sobrecompra: 70% a 100%, começando a alta entre 60% e estabilizando em 70%

- Trades errados: essa variável serve para gerenciar o capital. o Trader tem 10 operações de compra ou venda para fazer em um dia. O trader quebra a banca se tiver 10 operações erradas.
  - x_trades_errados_continue = triangular
  - x_trades_errados_atencao = triangular
  - x_trades_errados_limite = triangular
  - Valores:
    - continue: 0 a 2 trades errados é sinal 'continue' para a gestão de capital.
    - atencao: 2 a 8 trades errados é sinal 'atencao' para a gestão de capital.
    - limite: 9 a 10 trades errados é sinal limite para a gestão de capital.

- Tamanho da Entrada: porcentagem aplicada no trade a partir do total de capital disponível. Por exemplo, se há R$ 1000,00 para investir e o resultado deu 20%, então será investido R$ 200,00.
  - y_tamanho_entrada_pequeno = triangular
  - y_tamanho_entrada_medio = triangular
  - y_tamanho_entrada_grande = triangular

---

## c. Explicar a escolha de todos os parâmetros do sistema (ativação, implicação, agregação, defuzzyficação, etc.)


### Entradas (CRISP)
- É a 1ª etapa do sistema fuzzy. Aqui são inseridos os parâmetros para cada variável.
- x_liquedez_acao: 0 a 1000 pessoas
- x_indicador_rsi: 0 a 100%
- x_trades_errados: 0 a 10 erros

### Implicações
- 1ª parte: para liquedez da ação e o indicar RSI é utilizado o operador `OU (|)`. Neste caso é escolhido o maior - valor (MAX).
- 2ª parte: a 1ª parte da regra ainda calcula os trade errados utilizando o operador `E (&)`. Neste caso é escolhido sempre o antecedente de menor valor (MIN).

### Regras
```
rule1 = (x_liquedez_acao['alta'] | x_indicador_rsi['sobrecompra']) & x_trades_errados['continue'] 
    -> y_tamanho_entrada['grande']

rule2 = (x_liquedez_acao['medio'] | x_indicador_rsi['regiao_briga']) & x_trades_errados['atencao']
    -> y_tamanho_entrada['medio']

rule3 = (x_liquedez_acao['baixa'] | x_indicador_rsi['sobrevenda']) & x_trades_errados['limite']
    -> y_tamanho_entrada['pequeno']
```

- A execução das regras é o processamento, a fuzzificação

### Saída (CRISP)
- É feito a soma dos conjuntos de resposta de cada regra

### Exemplo
#### Entradas
- tamanho_entrada_simulador.input['x_liquedez_acao'] = 300
- tamanho_entrada_simulador.input['x_indicador_rsi'] = 50
- tamanho_entrada_simulador.input['x_trades_errados'] = 0

#### Saídas
- tamanho_entrada_simulador.output["y_tamanho_entrada"] = 7.9 %
<br/>
Isso significa que será aplicado 7,9% do total de 20% do capital, ou seja:
<br/>

```
capital_inicial = R$ 1000,00
tamanho_entrada no trade = [0, 20%] do capital inicial
resultado = 7,9%

resultado * (capital_inicial * tamanho_entrada) = R$ 15,81
```

Então neste trade vou colocar R$ 15,81.

---

## c. Implementar o modelo proposto 1 com alguma API para sistemas fuzzy.

- Implementei em Python usando a biblioteca scikitfuzzy.
- [Notebook](gerenciamento_capital_trade_fuzzy.ipynb) com o código (anexo)

---

## d. Testar diferentes parâmetros e analisar as diferenças (quanto mais testes e mais análises, melhor);

Tem no arquivo de [notebook](gerenciamento_capital_trade_fuzzy.ipynb) (anexo)

---

#### Referências
- RSI: https://admiralmarkets.com/pt/educacao/aprender-trading/indicadores-trading/rsi-indicador
- [Documentção scikitfuzzy](https://pythonhosted.org/scikit-fuzzy/_modules/skfuzzy/control/controlsystem.html#ControlSystemSimulation.compute)

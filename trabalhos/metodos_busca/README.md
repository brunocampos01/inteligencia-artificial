# Trabalho sobre Métodos de busca (2020-1)
O propósito do trabalho é implementar o algoritmo de busca A*. A implementação será testada através do jogo 8-puzzle, o qual também fornece o contexto para a heurística.

A entrada do programa é um tabuleiro desordenado (com o quadrado sem número em qualquer lugar do tabuleiro). A saída principal do programa é o menor caminho (a sequência de movimentos do quadrado sem número) para chegar-se ao tabuleiro ordenado. Além do caminho, ao final, deve ser exibido:
- O total de nodos visitados
- O total de nodos expandidos/criados
- O maior tamanho da fronteira durante a busca
- O tamanho do caminho

Para a implementação do algoritmo, a equipe deve implementar 3 variações do algoritmo:
1. Custo Uniforme (sem heurística)
2. A* com uma heurística simples
3. A* com a heurística mais precisa que conseguirem

Juntamente com a implementação (.ZIP) deverá ser entregue um mini-relatório explicando brevemente: 
1. Qual a representação (estrutura de dados) do estado;
2. Qual a estrutura de dados para a fronteira e nodos fechados;
3. Descrição da implementação (ideia geral e métodos relacionados) das heurísticas
4. Como foi gerenciada a fronteira, verificações, quais etapas foram feitas ao adicionar um estado na fronteira (explicação das estratégias, respectivos métodos e possibilidades além do que foi implementado);
5. Quais os métodos principais e breve descrição do fluxo do algoritmo;
6. Caso algum dos objetivos não tenha sido alcançado explique o que você faria VS o que foi feito e exatamente qual o(s) problema(s) encontrado(s), bem como  limitações da implementação. 


Caso tenha sido utilizado algum referencial teórico ou prático, o mesmo deverá ser informado. A avaliação da implementação considera especialmente a forma de implementar a busca e os cálculos das heurísticas. Para receber nota máxima na implementação é necessário utilizar uma estrutura de dados e de busca adequada além de implementar a heurística matematicamente (sem uso de regras codificadas). Importante: a avaliação considera todo o trabalho realizado, não apenas uma saída correta. No livro do Russel & Norvig e no do Luger são apresentadas boas discussões sobre heurísticas para esse problema e também uma boa apresentação do A*.
 
Se for detectado plágio de qualquer forma (inclusive de trabalhos de semestres anteriores), todos os envolvidos receberão nota 0 e não será possível entregar o trabalho novamente em nenhum momento.

O trabalho foi planejado para ser desenvolvido por equipes de até 3 alunos.

---

%% Considere um programa em Prolog com as cláusulas a seguir:

progenitor(maria,jose). % Maria e progenitor de José.
progenitor(joao, jose). 
progenitor(joao, ana). 
progenitor(jose, julia).
progenitor(jose, iris).
progenitor(iris, jorge).

masculino(joao). % Joao e do sexo masculino.
masculino(jose). 
masculino(jorge). 
masculino(rocky).

feminino(maria). % Maria e do sexo feminino.
feminino(ana). 
feminino(julia). 
feminino(iris).

mae(Mae,Y) :- progenitor(Mae,Y), feminino(Mae).
pai(Pai,Y) :- progenitor(Pai,Y), masculino(Pai).

avo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).

antepassado(X,Z) :- progenitor(X,Z).
antepassado(X,Z) :- progenitor(X,Y), antepassado(Y,Z).

nasceu_em(joao,porto_alegre). 
nasceu_em(jean,paris).

fica_em(porto_alegre,brasil). 
fica_em(paris,franca).

patria_de(X,Y):-nasceu_em(X,Z),fica_em(Z,Y).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 1) Executar as consultas estudas em aula para testar o funcionamento

% 2) Escrever as cláusulas necessárias para consultar sobre o parentesco de irmãos, cunhados e sogros
irmao(X,Y):-pai(Z,X),pai(Z,Y).
irmao(X,Y):-mae(Z,X),mae(Z,Y).

% Só pode haver cunhados e sogros se existir uma relação entre pessoas
% add rocky
namora(iris,rocky).

cunhado(X,Z):-irmao(X,Y),namora(Y,Z).
cunhado(Z,X):-irmao(X,Y),namora(Y,Z).
% cunhado(rocky,Z). --perguntar professor
% cunhado(julia,Z).

eh_sogro(A,C):-namora(B,C), progenitor(A,B).
% eh_sogro(jose,X).

% 3) Com base nas cláusulas sobre a relação de descendentes, faça as cláusulas para determinar a relação de ascendentes.
pais(P,Y):-pai(P,Y).
pais(M,Y):-mae(M,Y).
% pais(X,jose).

% 4) Complemente o programa para permitir consultas 
% sobre a pátria onde nasceram todos os descendentes de alguém.

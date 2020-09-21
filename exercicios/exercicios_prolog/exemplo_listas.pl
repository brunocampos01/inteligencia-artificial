INE5633-07238 (20182) - Sistemas Inteligentes
Exemplos de programas PROLOG: Listas
/* 01 =====================

* Predicado: first(L,P)
* Definição: L é uma lista e P é o first dado de L. */
first(P,[P|_]).


/* 02 ====================
* Predicado: segundo(L,S)
* Definição: L é uma lista e S é o segundo dado de L.*/
segundo(S,[_|Y]):- first(S,Y).


/* 03 ===================
* Predicado: last(L,U)
* Definição: L é uma lista e U é o último dado de L.*/
last(U,[U|[]]).
last(U,[_|Y]):- last(U,Y).


/* 04 ======================
* Predicado: penlast(L,P)
* Definição: L é uma lista e P é o penúltimo de L.*/
penlast([P,_], P).
penlast([_,S,T|R],P) :- penlast([S,T|R],P).


/* 05 ====================
* Predicado: size(L,T)
* Definição: L é uma lista e T é o número de dados de L.*/
size([], 0).
size([_|Y], N) :- size(Y, N1), N is N1+1.


/* 06 =====================
* Predicado: pertence(D,L)
* Definição: L é uma lista e D é um dos dados de L*/
pertence(D, [D|_]).
pertence(D, [_|Y]) :- pertence(D, Y).


/* 07 ========================
* Predicado: posicao(D,L,Pos)
* Definição: L é uma lista e Pos é a posição (iniciando com 1) 
* do dado D na lista L. Pos = 0 caso dado não esteja em L.*/
posicao(D,[],0).
posicao(D,[P|_],1) :- D = P.
posicao(D,[P|T],Pos) :- D \= P, posicao(D,T,PosAuxiliar),
Pos is PosAuxiliar + 1.


/* 08 ==============================
* Predicado: removidofirst(L,LR)
* Definição: L é uma lista e LR é uma lista com os mesmos dados de L, menos o first.*/
removidofirst([X|Y],Y).


/* 09 ============================
* Predicado: removidolast(L,LR)
* Definição: L é uma lista e LR é uma lista com os mesmos dados de L, menos o último.Primeira parte:*/
removidolast([X],[]).
removidolast([Y|T], [Y|T2]) :- removidolast(T,T2).


/* 10 =================================
* Predicado: substituidolast(D,L,LM)
* Definição: L é uma lista e LM é uma lista com os mesmos dados de L, com exceção do último que é D.*/
substituidolast(D,[U],[D]).
substituidolast(D,[A|T], [A|T2]) :- substituidolast(D,T,T2).


/* 11 ==================================
* Predicado: inseridoNoInicio(D, L, LM)
* Definição: D é um dado, L é uma lista e LM é a lista L mais o dado D no início. */
inseridoNoInicio(D, L, [D|L]):- !.


/* 12 =================================
* Predicado: inseridoNoFinal(D, L, LM)
* Definição: D é um dado, L é uma lista e LM é a lista L mais o dado D no final.*/
inseridoNoFinal(D,[],[D]).
inseridoNoFinal(D,[A|T],[A|T2]) :- inseridoNoFinal(D,T,T2).


/* 13 ====================================
* Predicado: inseridoNaPos(D, Pos, L, LM)
* Definição: D é um dado, Pos é a posição onde D deve ser inserido na lista L e LM é a lista L mais o dado D na posição Pos.*/
inseridoNaPos(D,1, L,[D|L]).
inseridoNaPos(D,Pos,[A|T],[A|T2]) :- inseridoNaPos(D,PosAuxiliar,T,T2),
Pos is PosAuxiliar + 1.


/ * 14 =====================================
* Predicado: removidoDaPos(L, Pos, D, LM)
* Definição: L é uma lista, Pos é a posição do dado a ser removido, D é o dado removido e LM é a lista L sem o dado removido.*/
removidoDaPos(P,1,[P|Y],Y).
removidoDaPos(D,Pos,[P|T],[P|T2]) :- Pos > 1, removidoDaPos(D,PosAuxiliar,T,T2),
Pos is PosAuxiliar + 1.


/* 15 =====================================
* Predicado: substituidoDoInicio(D, L, LM)
* Definição: D é um dado, L é uma lista e LM é a lista L com D no lugar do first dado de L. */
substituidoDoInicio(D,[P|T],[D|T]).


/* 16 ====================================
* Predicado: substituidoDoFinal(D, L, LM)
* Definição: D é um dado, L é uma lista e LM é a lista L com D no lugar do último dado de L. */
substituidoDoFinal(D,[U],[D]).
substituidoDoFinal(D,[A|T], [A|T2]) :- substituidoDoFinal(D,T,T2).


/* 17=======================================
* Predicado: substituidoDaPos(D, Pos, L, LM)
* Definição: D é um dado, Pos é a posição do dado a ser substituído, L é uma lista e LM é a lista L com D no lugar do dado de L que está na posição Pos.*/
substituidoDaPos(D,1,[P|T],[D|T]).
substituidoDaPos(D,Pos,[P|T],[P|T2]) :- D \= P, substituidoDaPos(D,PosAuxiliar,T,T2), Pos is PosAuxiliar + 1.

 

/* 19 ========================
* Predicado: invertida(L, LM)
* Definição: L é uma lista e LM é a lista L com os dados 
* invertidos (o primeriro de L será o último de LM, 
* o segundo de L será o penúltimo de LM e assim por diante).*/
invertida(L, LM) :- aux([], L, LM).
aux(L1, [], L1).
aux(L1, [L|LM], Z) :- aux([L | L1], LM, Z).


/* 20 ========================
* Predicado: primos(L, N)
* Definição: L é uma variável que retorna uma lista e N é um inteiro. A lista L retorna os números primos menores que N */
/* e_primo(2).
/* e_primo(3).
/* e_primo(P) :- integer(P), P > 3, P mod 2 =\= 0, \+fator(P,3).
/* fator(N,L) :- N mod L =:= 0.
/* fator(N,L) :- L * L < N, L2 is L + 2, fator(N,L2).

e_primo(2).
e_primo(3).
e_primo(P) :- integer(P), P > 3, P mod 2 =\= 0, \+tem_factor(P,3).
tem_factor(N,L) :- N mod L =:= 0.
tem_factor(N,L) :- L * L < N, L2 is L + 2, tem_factor(N,L2).

inseridoNoInicio(D,[],[D]).
inseridoNoInicio(D,L,[D|L]).

primos(N,L):- primos2(N,0,L).
primos2(N,X,_):- X > N, !.
primos2(N,X,L):- X =< N, e_primo(X), Y is X+1, primos2(N,Y,R), inseridoNoInicio(X,R,L).
primos2(N,X,L):- X =< N, Y is X+1, primos2(N,Y,L).

Last modified: quarta, 12 setembro 2018, 9:13

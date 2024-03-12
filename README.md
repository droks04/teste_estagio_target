# teste_estagio_target
1) Observe o trecho de código abaixo:
```
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);
```
Ao final do processamento, qual será o valor da variável SOMA?

**Reposta questão 1: 91** --- [teste]([url](https://github.com/droks04/teste_estagio_target/blob/master/soma/soma.py))


2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

**Resposta questão 2:** [Codigo](https://github.com/droks04/teste_estagio_target/blob/master/pesquisa_fibonacci/fibonacci.py)


3) Descubra a lógica e complete o próximo elemento:


a) 1, 3, 5, 7, **9**

b) 2, 4, 8, 16, 32, 64, **128**

c) 0, 1, 4, 9, 16, 25, 36, **49**

d) 4, 16, 36, 64, **100**

e) 1, 1, 2, 3, 5, 8, **13**

f) 2,10, 12, 16, 17, 18, 19, **200**


4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

**Resposta**

Sabendo que há 3 salas cada um com uma lâmapda:

Na primeira ida:
Ligo o interruptor  1 por 5 minutos e o desligo, ligo o interruptor 2 e o deixo ligado e vou até a primeira sala.
Se a lampada estiver acessa, pertence ao interruptor 2, se estiver desligada e quente pertence ao interruptor 1, se estiver desligada e fria pertence ao interruptor 3.

Na segunda ida:
Ciente das informações deduzidas na primeira ida, para a segunda ida espero ao menos 5 minutos para que as lampadas esfriem e ligo somente o interruptor 3.
Vou ate a segunda sala, agora só tenho duas opções após as informações da primeira ida e posso deduzir a qual interruptor pertence a lampada.


5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

Resposta questão 5: [Codigo]([url](https://github.com/droks04/teste_estagio_target/blob/master/soma/soma.py)https://github.com/droks04/teste_estagio_target/blob/master/reverter_string/reserve.py)



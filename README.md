# Python_TetraMasterVicLogicEngine
Es un Motor de la lógica del Videojuego TetraMaster de Final Fantasy IX
## Las cartas
Una carta de tetramaster tiene las siguientes características
![Cartas de TetraMaster](./img/Cartas_Numeros.png)

### Interpretación de los cuatro digitos
Los 4 dígitos al pie de la carta son:

AP - Valor del Ataque 
AT - Tipo de Ataque
PD - Valor de la Defensa Física
MD - Valor de la Defensa Mágica

Los tipos de ataque son:

P - Ataque físico
M - Ataque Mágico
X - Ataque Flexible
A - Ataque Asalto

La mecánica de cada tipo de ataque es:

P - AP vs PD
M - AP vs MD
X - AP vs min(PD, MD)
A - max( AP, PD, MD) vs min (AP, PD, MD)

### Cálculo de los valores
Los puntos que le corresponden son:

| Valor | Mínimo | Máximo |
|-------|--------|--------|
| 0     | 000    | 015    |
| 1     | 016    | 031    |
| 2     | 032    | 047    |
| 3     | 048    | 063    |
| 4     | 064    | 079    |
| 5     | 080    | 095    |
| 6     | 096    | 111    |
| 7     | 112    | 127    |
| 8     | 128    | 143    |
| 9     | 144    | 159    |
| A     | 160    | 175    |
| B     | 176    | 191    |
| C     | 192    | 207    |
| D     | 208    | 223    |
| E     | 224    | 239    |
| F     | 240    | 255    |

La fórmula para generar la tabla se basa en multiplicar por 16 el valor, y así los rangos mínimo y máximo se dan por:

$$
\begin{array}{lcl}
v & = & 0,1,2, ... , 14, 15, 16 \\
min & = & 16 \cdot v  \\
max & = & 16 \cdot (v+1)  -1    
\end{array}
$$

### Cálculos de los valores en la batalla de cartas
Sean dos cartas, A y B, representadas por los siguientes parámetros:

```
A : A-AP, A-AT, A-PD, A-MD
B : B-AP, B-AT, B-PD, B-MD
```

Cuando empieza la batalla de las dos cartas se sigue el siguiente proceso:

Fase 1: Cálculo del valor de ataque de la carta A:
```
if AT == A -> v = max( AP, PD, MD)
else v = AP

vmin = 16 * v
vmax = 16 * (v+1) - 1
potencia = random(vmin, vmax)
```

Fase 2: Se calcula el ataque real de la carta A:
```
ataque = potencia - random (0, potencia)

Fase 3: Cálculo del valor de la carta B:

if AT == P -> v = PD
if AT == M -> v = MD
if AT == X -> v = min (PD, MD)
if AT == A -> v = min (AP, PD, MD)

vmin = 16 * v
vmax = 16 * (v+1) - 1
potencia = random(vmin, vmax)
```
Fase 4: Cálculo de la defensa real de la carta B: 
```
defensa = defensa - random(0, potencia)
```
Fase 5: Calcular quien gana entre carta A y B:
```
if ataque >= defensa ->  gana carta A
else gana carta B
```

## Pantalla Selector de cartas
Al inicio el jugador debe elegir cinco cartas de  su mazo, en la siguiente pantalla
![Selector de cartas](img/SelectorDeCartas.png)

## Mesa de batalla
El aspecto de la mesa de juego o de batalla es:
![Mesa de Batalla](./img/MesaDeBatalla.png)



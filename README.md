# 🧾 README – Parcial 2 Lenguajes de Programación 2025-2

## 👩‍💻 Autora
**Nombre:** Paula Alejandra  
**Sistema:** Kali Linux  
**Materia:** Lenguajes de Programación – Parcial 2  

---

## Descripción general
Este proyecto implementa diferentes técnicas de **análisis sintáctico** sobre gramáticas libres de contexto, aplicadas a la simulación de operaciones CRUD sobre una base de datos y expresiones aritméticas.  

Se desarrollan y prueban **cinco enfoques distintos**:

| Punto | Tema | Tecnología | Tipo de análisis |
|-------|------|-------------|------------------|
| 1 | Diseño de gramática para operaciones CRUD | ANTLR / BNF | Diseño formal |
| 2 | Implementación en ANTLR | Python + ANTLR4 | Parser descendente |
| 3 | Analizador sintáctico ascendente (por pila) | Python | Shift-reduce simplificado |
| 4 | Parser CYK y Predictivo (comparación de rendimiento) | Python | Ascendente vs descendente |
| 5 | Diseño del algoritmo de emparejamiento para parser descendente recursivo | Python | Recursión y backtracking |

---

## 🧩 Estructura del proyecto

```

Parcial2/
│
├── Punto1/
│   └── DataLang.g4                  # Gramática ANTLR para operaciones CRUD
│
├── Punto2/
│   ├── src/
│   │   └── run_datalang.py          # Script ejecutor del parser
│   ├── tests/
│   │   └── test1.txt                # Archivo con ejemplos CRUD
│   └── antlr/
│       └── DataLang/                # Archivos generados por ANTLR
│
├── Punto3/
│   ├── ascendente.py                # Analizador sintáctico ascendente por pila
│   └── conjuntos.txt                # Cálculos de PRIMEROS, SIGUIENTES y PREDICCIÓN
│
├── Punto4/
│   ├── benchmark_cyk.py             # Implementación y comparación CYK vs Predictivo
│   └── benchmark_cyk_predictive.csv # Resultados de rendimiento
│
├── Punto5/
│   └── parser_emparejamiento.py     # Implementación del parser recursivo con backtracking
│
└── README.md                        # Este archivo

````

---

## Punto 1 – Diseño de la gramática CRUD

**Objetivo:** Definir una gramática libre de contexto que modele un lenguaje capaz de realizar operaciones **CRUD** en una base de datos.

**Lenguaje definido (`DataLang`):**
```antlr
createStmt : BUILD TABLE ID WITH LPAREN colList RPAREN ;
readStmt   : GET FROM ID (WHERE condition)? ;
updateStmt : UPDATE ID SET assignList (WHERE condition)? ;
deleteStmt : ERASE FROM ID (WHERE condition)? ;
````

**Ejemplo válido:**

```
build table empleados with (id:number, nombre:text, activo:bool);
get from empleados where activo = true;
update empleados set nombre = "Paula" where id = 1;
erase from empleados where activo = false;
```

**Tokens principales:**
`BUILD, TABLE, WITH, GET, FROM, WHERE, UPDATE, SET, ERASE, TRUE, FALSE`

---

## Punto 2 – Implementación de la gramática en ANTLR

**Objetivo:** Implementar la gramática anterior usando **ANTLR4** y ejecutar un analizador en **Python**.
Para este punto es requerido usar un entrono virtual para ejecutar el ANTLR.

### Instalación en Kali

```bash
sudo apt install default-jdk
mkdir -p ~/tools && cd ~/tools
wget https://www.antlr.org/download/antlr-4.13.0-complete.jar
export CLASSPATH=".:$HOME/tools/antlr-4.13.0-complete.jar:$CLASSPATH"
alias antlr4='java -jar $HOME/tools/antlr-4.13.0-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
pip install antlr4-python3-runtime
```

### Generación de archivos ANTLR

```bash
antlr4 -Dlanguage=Python3 DataLang.g4 -o ../antlr/DataLang
```

### Ejecución del parser

```bash
cd src
python3 run_datalang.py ../tests/test1.txt
```

**Salida esperada:**

```
✅ Análisis completado correctamente.
Árbol sintáctico generado: (program (statement (createStmt build table empleados with ... )))
```

---

## Punto 3 – Analizador sintáctico ascendente (por pila)

**Gramática base:**

```
E → E + T | T
T → T * F | F
F → ( E ) | id
```

### Transformación a LL(1)

```
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ( E ) | id
```

### Archivos

* `ascendente.py` → implementación del parser por pila
* `conjuntos.txt` → PRIMEROS, SIGUIENTES y PREDICCIÓN

### Ejemplo de ejecución

```bash
python3 ascendente.py
```

**Salida esperada:**

```
Analizando: id + id * id
SHIFT -> id
REDUCE -> F, T, E
✅ Cadena aceptada.
```

---

## Punto 4 – Parser CYK y Predictivo

**Objetivo:** Implementar un parser con el algoritmo **CYK** y comparar su rendimiento con un **parser predictivo LL(1)**.

**Archivo:** `benchmark_cyk.py`

### Ejecución

```bash
python3 benchmark_cyk.py
```

**Salida esperada:**

```
size=5  CYK avg: 0.00004s   Predictive avg: 0.000003s
size=80 CYK avg: 0.09587s   Predictive avg: 0.000020s
```

**Resultados:**

* CYK: O(n³) — crece rápidamente con la longitud de la cadena.
* Predictivo: O(n) — mucho más eficiente.
* Archivo con resultados: `benchmark_cyk_predictive.csv`

---

## Punto 5 – Diseño del Algoritmo de Emparejamiento (Parser Descendente Recursivo)

Diseñar un **algoritmo de emparejamiento** que reconozca cadenas válidas basadas en una gramática libre de contexto, utilizando **recursión y backtracking** para el análisis sintáctico descendente.

---

### **Representación de la Gramática**

* Se usa un **diccionario de Python** donde cada no terminal es una clave y su valor es una lista de producciones.
* Las producciones vacías (epsilon) se representan como listas vacías `[]`.

Ejemplo:

```python
gramatica = {
    "S": [["a", "A", "b"]],
    "A": [["a", "A"], []]  # [] representa epsilon
}
```

---

### **Emparejamiento de Terminales**

* Para los terminales (símbolos en minúscula), el algoritmo compara el símbolo actual de la cadena con el esperado.
* Si coincide, avanza la posición; si no, lanza un **error con posición y símbolo esperado**.

---

### **Manejo de No Terminales (Recursión)**

Cada no terminal se procesa probando todas sus producciones posibles:

1. Se guarda la posición actual (para retroceder si falla).
2. Se intenta emparejar cada símbolo recursivamente.
3. Si una producción completa tiene éxito, se retorna éxito.
4. Si todas fallan, se vuelve atrás (backtracking) y se marca error.

---

### **Backtracking**

* Se usa para probar **múltiples alternativas** en las producciones de un no terminal.
* Si una falla, se retrocede a la posición original y se intenta con la siguiente.

---

### **Evaluación de la Cadena**

Una cadena es **válida** si:

* Se emparejan todos los símbolos según la gramática.
* Se consumen todos los caracteres de la cadena.

Si no, se reporta un error indicando la posición del fallo.

---

### ** Lectura desde Archivo**

El algoritmo puede leer un archivo `.txt` donde **cada línea es una cadena** a evaluar automáticamente.

---

### **Resumen del Diseño**

1. Representar la gramática como diccionario.
2. Crear función recursiva para cada símbolo.
3. Implementar backtracking para manejar alternativas.
4. Validar el emparejamiento completo.
5. Leer y procesar múltiples cadenas desde archivo.

---

## 📊 Conclusiones Generales

1. **ANTLR (P1–P2)** simplifica el análisis sintáctico generando analizadores eficientes.
2. **El parser ascendente (P3)** permite observar el proceso *shift/reduce* paso a paso.
3. **El algoritmo CYK (P4)** es más general pero mucho más lento.
4. **El algoritmo de emparejamiento (P5)** demuestra la lógica interna del parser recursivo con backtracking.
5. En lenguajes estructurados como *DataLang*, **LL(1)** y **ANTLR** son las mejores opciones por simplicidad y rendimiento.

---

```

---


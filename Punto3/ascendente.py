# ascendente.py

def es_reducible(pila):
    """Devuelve la producción si el tope de la pila puede reducirse."""
    # Producciones de la gramática LL(1) transformada:
    # E  → T E'
    # E' → + T E' | ε
    # T  → F T'
    # T' → * F T' | ε
    # F  → ( E ) | id

    reglas = {
        ('id',): 'F',
        ('(', 'E', ')'): 'F',
        ('F', 'T\''): 'T',
        ('T', 'E\''): 'E',
        ('+', 'T', 'E\''): 'E\'',
        ('*', 'F', 'T\''): 'T\''
    }

    # Buscar la reducción más larga posible
    for longitud in range(3, 0, -1):
        if tuple(pila[-longitud:]) in reglas:
            return longitud, reglas[tuple(pila[-longitud:])]
    return None, None


def analizar(tokens):
    pila = ['$']
    print(f"Tokens: {tokens}")

    while True:
        if tokens:
            actual = tokens[0]
        else:
            actual = '$'

        # Intentar reducir antes de hacer shift
        reducida = False
        while True:
            longitud, no_terminal = es_reducible(pila[1:])
            if no_terminal:
                pila = pila[:-longitud] + [no_terminal]
                print(f"REDUCE -> {no_terminal:<4} Pila: {pila}")
                reducida = True
            else:
                break

        # Aceptación
        if pila == ['$', 'E'] and actual == '$':
            print("Cadena aceptada.\n")
            break

        # Si no se puede reducir, hacer shift
        if tokens:
            simbolo = tokens.pop(0)
            pila.append(simbolo)
            print(f"SHIFT  -> {simbolo:<4} Pila: {pila}")
        else:
            print("Fin del análisis (no hay más reducciones posibles).\n")
            break


# ------------------ PRUEBAS ------------------
def main():
    pruebas = [
        "id + id * id",
        "( id + id ) * id",
        "id + ( id * id )",
        "id * id + id",
        "id"
    ]

    for expr in pruebas:
        print(f"\nAnalizando: {expr}")
        tokens = expr.split() + ['$']
        analizar(tokens)



main()

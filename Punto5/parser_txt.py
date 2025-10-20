# Gramática como diccionario
gramatica = {
    "S": [["a", "A", "b"]],
    "A": [["a", "A"], []]  # [] representa epsilon
}

def match_terminal(t, cadena, pos):
    if pos < len(cadena) and cadena[pos] == t:
        return True, pos + 1
    return False, pos

def parse_symbol(simbolo, cadena, pos):
    start = pos
    if simbolo.islower():  # terminal
        exito, pos_new = match_terminal(simbolo, cadena, pos)
        if not exito:
            return False, pos
        return True, pos_new

    # No terminal
    for produccion in gramatica.get(simbolo, []):
        pos = start
        exito = True
        for s in produccion:
            exito, pos = parse_symbol(s, cadena, pos)
            if not exito:
                break
        if exito:
            return True, pos
    return False, start

# Leer archivo de cadenas
with open("cadenas.txt", "r") as file:
    lineas = file.read().splitlines()

for cadena in lineas:
    exito, pos_final = parse_symbol("S", cadena, 0)
    if exito and pos_final == len(cadena):
        print(f"'{cadena}': Cadena válida")
    else:
        print(f"'{cadena}': Cadena inválida")

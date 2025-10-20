"""
Parser usando el Algoritmo CYK (Cocke-Younger-Kasami)
Complejidad: O(n³)
"""

def cyk_parse(tokens, grammar):
    """
    Algoritmo CYK para parsing
    
    Args:
        tokens: Lista de tokens a analizar
        grammar: Diccionario con la gramática en CNF
        
    Returns:
        bool: True si la cadena es válida
    """
    n = len(tokens)
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Fase 1: Llenar diagonal (subcadenas de longitud 1)
    for i, token in enumerate(tokens):
        for lhs, rhs_list in grammar.items():
            for rhs in rhs_list:
                if len(rhs) == 1 and rhs[0] == token:
                    table[i][i].add(lhs)
    
    # Fase 2: Llenar tabla para subcadenas de longitud 2 a n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for lhs, rhs_list in grammar.items():
                    for rhs in rhs_list:
                        if len(rhs) == 2:
                            B, C = rhs
                            if B in table[i][k] and C in table[k + 1][j]:
                                table[i][j].add(lhs)
    
    return "S" in table[0][n - 1]


# Gramática en CNF
grammar_cnf = {
    "S": [["E"]],
    "E": [["E", "+T"], ["T"]],
    "+T": [["+", "T"]],
    "T": [["T", "*F"], ["F"]],
    "*F": [["*", "F"]],
    "F": [["(E)"], ["id"]],
    "(E)": [["(", "E"]],
    "E)": [["E", ")"]],
}


if __name__ == "__main__":
    # Casos de prueba
    casos = [
        ["id", "+", "id"],
        ["id", "*", "id", "+", "id"],
        ["(", "id", "+", "id", ")", "*", "id"],
        ["id"],
    ]
    
    print("=" * 60)
    print("PARSER CYK - PRUEBAS")
    print("=" * 60)
    
    for tokens in casos:
        expr = ' '.join(tokens)
        resultado = cyk_parse(tokens, grammar_cnf)
        print(f"{'✓' if resultado else '✗'} {expr}")

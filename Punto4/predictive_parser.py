"""
Parser Predictivo (Descendente Recursivo)
Complejidad: O(n)
"""

def parse_expression(tokens):
    """
    Parser predictivo recursivo
    
    Gramática LL(1):
    E → T E'
    E' → + T E' | ε
    T → F T'
    T' → * F T' | ε
    F → ( E ) | id
    
    Args:
        tokens: Lista de tokens
        
    Returns:
        bool: True si es válida
    """
    pos = 0
    
    def E():
        nonlocal pos
        T()
        while pos < len(tokens) and tokens[pos] == "+":
            pos += 1
            T()
    
    def T():
        nonlocal pos
        F()
        while pos < len(tokens) and tokens[pos] == "*":
            pos += 1
            F()
    
    def F():
        nonlocal pos
        if pos < len(tokens) and tokens[pos] == "id":
            pos += 1
        elif pos < len(tokens) and tokens[pos] == "(":
            pos += 1
            E()
            if pos < len(tokens) and tokens[pos] == ")":
                pos += 1
    
    try:
        E()
        return pos == len(tokens)
    except:
        return False


if __name__ == "__main__":
    # Casos de prueba
    casos = [
        ["id", "+", "id"],
        ["id", "*", "id", "+", "id"],
        ["(", "id", "+", "id", ")", "*", "id"],
        ["id"],
    ]
    
    print("=" * 60)
    print("PARSER PREDICTIVO - PRUEBAS")
    print("=" * 60)
    
    for tokens in casos:
        expr = ' '.join(tokens)
        resultado = parse_expression(tokens)
        print(f"{'✓' if resultado else '✗'} {expr}")

import sys
import os
from antlr4 import *

# --- Ajuste de ruta para encontrar el paquete antlr ---
# Calcula la ruta base del proyecto (sube 1 nivel desde src/)
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
antlr_path = os.path.join(base_path, 'antlr')
sys.path.insert(0, antlr_path)
# ------------------------------------------------------

from DataLang.DataLangLexer import DataLangLexer
from DataLang.DataLangParser import DataLangParser


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 run_datalang.py <archivo.txt>")
        return

    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = DataLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DataLangParser(stream)

    tree = parser.program()
    print("✅ Análisis completado correctamente.\n")
    print("Árbol sintáctico generado:")
    print(tree.toStringTree(recog=parser))



main()


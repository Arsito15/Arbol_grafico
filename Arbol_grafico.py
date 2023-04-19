import re

# Definir la clase Nodo que representa un nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para crear un árbol de expresiones a partir de una expresión dada
def crear_arbol_expresiones(expresion):
    # Eliminar espacios en blanco de la expresión
    expresion = expresion.replace(" ", "")
    expresion = expresion.replace("(", "")
    expresion = expresion.replace(")", "")

    # Separar la expresión en una lista de símbolos
    simbolos = re.findall(r"[\d\.]+|\(|\)|\+|\-|\*|\/", expresion)

    # Función auxiliar para convertir una lista de símbolos en un árbol de expresiones
    def crear_subarbol(simbolos, inicio, fin):
        # Encontrar el índice del operador con la menor precedencia
        nivel_operador = 0
        indice_operador = None
        for i in range(inicio, fin + 1):
            if simbolos[i] == "(":
                nivel_operador += 1
            elif simbolos[i] == ")":
                nivel_operador -= 1
            elif nivel_operador == 0:
                if simbolos[i] in ["+", "-"]:
                    if indice_operador is None or simbolos[i] in ["*", "/"]:
                        indice_operador = i
                elif simbolos[i] in ["*", "/"]:
                    if indice_operador is None:
                        indice_operador = i

        # Si no se encontró ningún operador, entonces la expresión es simplemente un número
        if indice_operador is None:
            return Nodo(float(simbolos[inicio]))

        # Crear el nodo actual y recursivamente crear los subárboles de la izquierda y la derecha
        nodo = Nodo(simbolos[indice_operador])
        nodo.izquierda = crear_subarbol(simbolos, inicio, indice_operador - 1)
        nodo.derecha = crear_subarbol(simbolos, indice_operador + 1, fin)
        return nodo

    # Crear el árbol de expresiones a partir de la lista de símbolos
    raiz = crear_subarbol(simbolos, 0, len(simbolos) - 1)

    return raiz

# Función para imprimir el árbol de expresiones en la terminal
def imprimir_arbol_expresiones(nodo, prefijo="", es_izquierdo=None):
    if nodo is None:
        return
    print(prefijo, end="")
    print("├───" if es_izquierdo else "└───", end="")
    print(nodo.valor)
    imprimir_arbol_expresiones(nodo.izquierda, prefijo + ("|  " if es_izquierdo else "   "), True)
    imprimir_arbol_expresiones(nodo.derecha, prefijo + ("   " if es_izquierdo else "|  "), False)

# Ejemplo de uso del programa
expresion = input("expresion: ")
#expresion = "3 * (9 - 3 * 4)"
#print(f"expresion: {expression}")
arbol = crear_arbol_expresiones(expresion)
imprimir_arbol_expresiones(arbol)
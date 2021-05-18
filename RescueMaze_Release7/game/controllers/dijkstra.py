class Vertice:
    """Clase que define los vertices de las graficas"""
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = []
        self.padre = None #predecesor del vertice
        self.distancia = float('inf')

    def agregarVecino(self, v, p): #el vertice y el peso de la arista
        if v not in self.vecinos:
            self.vecinos.append([v, p]) #vecino y peso

class Grafica:
    """Clase que define los vertices de las graficas"""
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p): 
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b,p)
            self.vertices[b].agregarVecino(a,p)

    #Lista de pasos
    #1) Poner vertice inicial en distancia de 0 y al resto valor infinito, asignar tambien predecesor nulo para todos.
    #2) Establecer nodo inicial como actual y crear un conunto de nodos no visitados con todos los nodos
    #3) Mientras el conjunto de nodos no visitados no está vacio: 
    #4) Para el nodo actual u, considerando sus vecinos no visitados (v) con peso w en sus aristas:
        #a. Si la distancia del nodo u sumada con el peso w es menor a la distancia del nodo v, actualiza la distancia de v
        #y guardar a u como predecesor de v



    def dijkstra(self, a):
        if a in self.vertices: #a se encuentra en vertices?
            self.vertices[a].distancia = 0 #Establecer distancia del nodo inicial en 0
            actual = a #nodo actual
            noVisitados = [] #Lista de nodos no visitados

            for v in self.vertices:
                if v != a: #Mientras no encontremos al vertice a. estableceremos la distancia de ese vertice como inf
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None #Todos los predecesores de los nodos en None
                noVisitados.append(v)
                
            while len(noVisitados) > 0: #mientras noVisitados tenga elementos en el
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:

        else:
            return False


#Clase con columnas y filas 
    #Ya recorrido
    #Si era lugar de origen
    #Si era checkpoint
    #Si es swamp
    #Si tile negro
    #Si te puedes mover al norte,este, sur, oeste
    #Si era accesible
    #Si hay victima
    #width, height
#Sistema de orientación del robot

#mapelites
import random

# ME_POP_COUNT (ME_SIZEX * ME_SIZEY)
# son los tamaños del mapita que queres modificar
# 
# // calling code defines me_dna, me_mutate, me_pos, me_eval

# Genoma (vector)
class me_dna(object):
   def __init__(self,gnome, size):
        self.gnome = gnome
        self.size = size

    def me_dna_create(self,size):
        self.gnome = [0.0 for i in range(size)]
        self.size = size

    # Some dark logic for mutation
    def me_mutate(self,init):
        if init != 0 :
            pr = random.random()
            # genera valores aleatorios
            self.gnome = map(lambda g: random.random() ,self.gnome)
            for i in range(5,DIM*6,6):
                if random.random() < pr:
                    self.gnome[i] = random.random() * 0.5 + 0.5
                else:
                    self.gnome[i] = random.random() * 0.5 + 0.5
        else:
            pr = 6.0 / self.size
            for i in range (self.size):
                if random.random() < pr:
                    v = self.gnome[i] + (random.random() - 0.5)
                    if 0.0 <= v <= 1.0:
                        self.gnome[i] = 0
    
    # Toma la solución actual y obtiene a partir de 
    # eso las posiciones en el mapa para ir a guardar el fitness si 
    # es que es mejor que el que ya existe en el mapa
    def me_pos(self)
            y = self.user1 * (SIZEY-1)
            x = self.user2 * (SIZEX-1)
            return x, y

    # Calcular el porcentaje del fitness en este caso sería
    # hacer correr el clasificador y guardar el resultado de 
    # la corrida del subconjunto (porcentaje de aciertos)
    # f(x) 
    def me_eval(self)

 # Cantidad de celdas 
SIZEX = 100
SIZEY = 100
SIZE = SIZEX * SIZEY          
                
# Clase específica del juego
class me_info(object):
    def __init__(self,fitness,user1,user2,parent):
        self.fitness = fitness
        self.user1 = user1
        self.user2 = user2
        self.parent = parent

# Celdas del map elite
class me_cell(object):
    def __init__(self,best,state):
        self.best = best # me_dna
        self.state = state

#Clase principal
class me_project(object):
        
        #Constructor que incializa todos los parametros
        def __init__(self,tmp,tmpi,mapp,cell,generation,best_score):
            self.tmp = tmp # genoma
            self.tmpi = tmpi # me_info
            # incializa el mapa
            self.mapp = [0.0 for i in range(SIZE)] 
            # create an empty N-dimensional map of elites
            self.cell = [me_cell() for i in range(SIZE)]
            self.generation = 0
            self.best_score = -1

        #En cada celda 
        def me_create(self,size):
            for c in self.cell:
                c.best = me_dna(size)
                c.best.me_dna_create(size)
            self.tmp = me_dna(size)
            self.tmp.me_dna_create(size)
        
        def me_restart(self):
            self.mapp = [0.0 for i in range(SIZE)]
            map(lambda c: c.state = 0, self.cell)
            self.generation = 0
            self.best_score = -1
        
        def update(self):
            # SELECTION
            cell_id = random(0,SIZE-1)
            cell = self.cell[cell_id]

            if cell.state > 0:
                self.tmp = cell.best
            
            # MUTATION
            if cell.state == 0:
                me_mutate(sel.tmp,1)
                self.tmpi.parent = -1 # Esta estructura es especifica al juego
            else:
                # TODO: me_mutate
                me_mutate(self.tmp,0)
                self.tmpi.parent = cell_id
            
            # EVALUATE
            # método que obtiene el fitness
            me_eval(self,self.tmp, self.tmpi)
            
            fit = self.tmpi.fitness
            if self.best_score < 0:
                self.best_score = fit
            else:
                if fit > self.best_score:
                    self.best_score = fit
            
            if self.tmpi.fitness != 0:
                x,y = me_pos(self.tmpi)
                if SIZEX > x >= 0 and SIZEY  > y >= 0:
                    mid = y * SIZEX + x
                    cell = self.cell[mid]
                    if self.tmpi.fitness >= self.mapp[mid]:
                        if cell.state == 0:
                            cell.state = 1
                        self.mapp[mid] = self.tmpi.fitness
                        cell.best = self.tmp
            self.generation += 1
import threading
from queue import Queue
from tkinter import *
from tkinter import ttk
from time import sleep
import random
import copy

def view_graph(g, weighted = False, q = Queue()):
    update_thread = GraphUpdater(g, q)
    draw_thread = Drawer(q, weighted)
    draw_thread.start()
    update_thread.start()
    return True

class Drawer(threading.Thread):
    def __init__(self, q, weighted):
        threading.Thread.__init__(self)
        #self.tree = tree
        self.weighted = weighted
        self.daemon = True
        self.q = q
        self.h = dict()
    
    def run(self):
        try:
            root = Tk()
            root.columnconfigure(0, weight=1)
            root.rowconfigure(0, weight=1)
            root.geometry('650x650')
            canvas = Canvas(root)
            # hbar=Scrollbar(canvas,orient=HORIZONTAL)
            # hbar.pack(side=BOTTOM,fill=X)
            # hbar.config(command=canvas.xview)
            # vbar=Scrollbar(canvas,orient=VERTICAL)
            # vbar.pack(side=RIGHT,fill=Y)
            # vbar.config(command=canvas.yview)
            # canvas.config(yscrollcommand=vbar.set)
            # canvas.config(xscrollcommand=hbar.set)
            canvas.grid(column=0, row=0, sticky=(N, W, E, S))
            def update():
                canvas.delete('all')
                self.graph = self.q.get(True)
                # canvas.config(width= w, height= h, scrollregion=(0,0,w,h))
                self.drawEdges(canvas)
                self.drawVertices(canvas)
                root.after(3000, update)
            root.after(3000, update)
            root.mainloop()
        except:
            print("Unexpected error:", sys.exc_info()[0])
        
    def drawVertices(self, canvas):
        vertices = self.graph.vertices
        for v in vertices:
            arr = []
            self.h[v.value] = arr
            (x, y) = v.getCoords()
            arr.append(canvas.create_oval(x + 35, y + 35, x + 65, y + 65, fill='gray'))
            arr.append(canvas.create_text(x + 50, y + 50, anchor='center', text=v.value))
            arr.append((x, y))
            
    def drawEdges(self, canvas):
        # print('drawing edges!')
        vertices = self.graph.vertices
        for v in vertices:
            #(x, y) = v.getCoords()
            for a in v.adjList:
                self.drawEdge(canvas, v, a[0], a[1])
                    
    def drawEdge(self, canvas, v, a, weight = None):
        (x, y) = v.getCoords()
        (ax, ay) = a.getCoords()
        canvas.create_line(x + 50, y + 50, ax + 50, ay + 50)
        arrowLengthx = (ax-x)
        arrowLengthx = abs(arrowLengthx)
        arrowLengthx = (arrowLengthx - 9.0)*0.03
        arrowLengthy = (ay-y)
        arrowLengthy = abs(arrowLengthy) 
        arrowLengthy = (arrowLengthy - 9.0)*0.03		
        #to mark the directed graph from the source to the adj node e.g. node 5 had adj node 4, mark will be *4
        x5= 0.0
        y5= 0.0
        distance = 9.0
        dist = 7.0
        if(arrowLengthx < arrowLengthy and (arrowLengthx/0.03) >= 60):
            distance = 8.8
            dist = 7.0
        elif(arrowLengthx < arrowLengthy):
            distance = 2.8
            dist = 2.5
        elif(arrowLengthx > arrowLengthy and (arrowLengthy/0.03) >= 60):
            distance =8.8
            dist = 7.0
        elif(arrowLengthx > arrowLengthy):
            distance = 2.8
            dist = 2.2
        if(ax<x and y>ay):
            x5 = ((x-ax)/distance)+ax
            y5 = ((y-ay)/distance)+ay
        elif(ax<x and y<ay):
            x5 = ((x-ax)/distance)+ax
            y5 = ay-((ay-y)/distance)
        elif(ax>x and y<ay):
            x5 = ax-((ax-x)/distance)
            y5 = ay-((ay-y)/distance)
        elif(ax>x and y>ay):
            x5 = ax-((ax-x)/distance)
            y5 = ((y-ay)/distance)+ay
        x0= 0.0
        y0= 0.0
        
        # if line is not horizontal or vertical
        if ax != x and ay != y:
            gradient =(((ay*-1.0)-(y*-1.0))/(ax-x))
            c= (ay*-1.0)-(gradient*ax)
            if(ax<x and y>ay):
                x0 = ((x-ax)/dist)+ax
                y0 = ((y-ay)/dist)+ay
            elif(ax<x and y<ay):
                x0 = ((x-ax)/dist)+ax
                y0 = ay-((ay-y)/dist)
            elif(ax>x and y<ay):
                x0 = ax-((ax-x)/dist)
                y0 = ay-((ay-y)/dist)
            elif(ax>x and y>ay):
                x0 = ax-((ax-x)/dist)
                y0 = ((y-ay)/dist)+ay
            gradientPerpendicular = (1.0/gradient)*-1.0
            cPerpendicular = (y0*-1.0) - (gradientPerpendicular*x0)
            
            x3,y3,x4,y4 = (0,0,0,0)
            
            if(arrowLengthx < arrowLengthy and arrowLengthx >= 60):
                arrl = arrowLengthx
                x3 = x0 - arrl
                y3 = (x3*gradientPerpendicular + cPerpendicular)*-1.0
                x4 = x0 + arrl
                y4 = (x4*gradientPerpendicular + cPerpendicular)*-1.0
                
            elif(arrowLengthx < arrowLengthy):
                arrl = 9.0
                x3 = x0 - arrl
                y3 = (x3*gradientPerpendicular + cPerpendicular)*-1.0
                x4 = x0 + arrl
                y4 = (x4*gradientPerpendicular + cPerpendicular)*-1.0
                
            elif(arrowLengthx > arrowLengthy and arrowLengthy >=60):
                arrl = arrowLengthy
                y3 = (-y0 - arrl)*-1.0
                x3 = (-y3-cPerpendicular)/gradientPerpendicular
                y4 = (-y0 + arrl)*-1.0
                x4 = (-y4-cPerpendicular)/gradientPerpendicular
                
            else:
                arrl = 9.0
                y3 = (-y0 - arrl)*-1.0
                x3 = (-y3-cPerpendicular)/gradientPerpendicular
                y4 = (-y0 + arrl)*-1.0
                x4 = (-y4-cPerpendicular)/gradientPerpendicular
                
            # create arrows
            canvas.create_line(x3 + 50,y3 + 50,x5 + 50,y5 + 50)
            canvas.create_line(x4 + 50,y4 + 50,x5 + 50,y5 + 50)
                
        if self.weighted and weight != None:
            value = round(weight,3)
            canvas.create_text((x + ax) / 2 + 50, (y + ay) / 2 + 65, anchor='center', text=value)
            
class GraphUpdater(threading.Thread):
    def __init__(self, graph, q):
        threading.Thread.__init__(self)
        self.daemon = True
        self.graph = graph
        self.q = q
    
    def run(self):
        while True:
            if self.q.empty():
                sleep(1)
                self.q.put(self.graph)
                #print('updated!')
                
class TraversalDrawer(Drawer):
    def __init__(self, traversalQueue, graph, step, title, weighted = False):
        super().__init__(traversalQueue, weighted)
        self.graph = graph
        self.updateArr = []
        self.step = step
        self.title = title
        self.daemon = True

    def run(self):
        root = Tk()
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.title(self.title)
        root.geometry('650x650')
        canvas = Canvas(root)
        canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.drawEdges(canvas)
        self.drawVertices(canvas)
        def update():
            #canvas.delete('all')
            if self.q.empty():
                return
            self.updateArr.append(self.q.get(True))
            self.drawVertices(canvas)
            for i in range(1, len(self.updateArr) + 1):
                value = self.updateArr[i - 1]
                # print('value: ' + str(value))
                canvas.itemconfig(self.h[value][0], outline='red')
                canvas.itemconfig(self.h[value][1], fill='red')
                canvas.create_text(self.h[value][2][0] + 50, self.h[value][2][1] + 75, anchor='center', text=str(i), fill='red')
            root.after(self.step, update)
        root.after(self.step, update)
        root.mainloop()
        
class SetDrawer(TraversalDrawer):
    def __init__(self, traversalQueue, graph, step, title, weighted = False):
        super().__init__(traversalQueue, graph, step, title, weighted)

    def run(self):
        root = Tk()
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.title(self.title)
        root.geometry('650x650')
        canvas = Canvas(root)
        canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.drawVertices(canvas)
        self.drawEdges(canvas)
        def update():
            # canvas.delete('all')
            if self.q.empty():
                return
            for i in self.updateArr:
                canvas.delete(self.h[i.value][-1])
            self.updateArr = self.q.get(True)
            # print(self.updateArr)
            # print(self.h)
            for i in range(1, len(self.updateArr) + 1):
                value = self.updateArr[i - 1].value
                # print('value: ' + str(value))
                canvas.itemconfig(self.h[value][0], outline='red')
                canvas.itemconfig(self.h[value][1], fill='red')
                self.h[value].append(canvas.create_text(self.h[value][2][0] + 50, self.h[value][2][1] + 75, anchor='center', text=str(i), fill='red'))
            root.after(self.step, update)
        root.after(self.step, update)
        root.mainloop()

class TSPDrawer(TraversalDrawer):
    def __init__(self, q, graph, step, title, showEnd):
        super().__init__(q, graph, step, title, False)
        self.showEnd = showEnd
        
    def run(self):
        root = Tk()
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.title(self.title)
        root.geometry('650x650')
        canvas = Canvas(root)
        canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.drawVertices(canvas)
        def update():
            
            if self.q.empty():
                self.drawEdge(canvas, self.updateArr[-1], self.updateArr[0])
                return
            canvas.delete('all')
            self.updateArr = self.q.get(True)
            
            self.drawEdges(canvas)
            self.drawVertices(canvas)
            root.after(self.step, update)
        root.after(self.step, update)
        root.mainloop()
            
    def drawEdges(self, canvas):
        for i in range(1, len(self.updateArr)):
            self.drawEdge(canvas, self.updateArr[i - 1], self.updateArr[i])
        if self.showEnd:
            self.drawEdge(canvas, self.updateArr[-1], self.updateArr[0])
        
        
class Graph:
    # class constructor
    def __init__(self):
        self.vertices = []
    
    # checks whether the graph is empty
    def isEmpty(self):
        return len(self.vertices) == 0		
    
    def addVertex(self, vertex, x = None, y = None):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        if vertex in self.vertices:
            print("Vertex already added in the graph!")
            return False
        if x == None or y == None:
            x = random.randrange(551)
            y = random.randrange(551)
        while self.isCoordsOccupied(x, y):
            x = random.randrange(551)
            y = random.randrange(551)
        self.vertices.append(vertex)
        if vertex.x == None:
            vertex.setCoords(x, y)
        return self.vertices
        
    def isCoordsOccupied(self, x, y):
        for v in self.vertices:
            coords = v.getCoords()
            if coords[0] >= x - 40 and coords[0] <= x + 40 and coords[1] >= y - 40 and coords[1] <= y + 40:
                return True
        return False
   
    
    def addEdge(self, v1, v2, weight = 1):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if v2 in v1.adjList:
            raise Exception('Edge already created!')
        v1._addEdge(v2, weight)
        
    def isAdj(self, v1, v2):
        for a in v1.adjList:
            if a[0] == v2:
                return True
        return False
    
    def deleteEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if not self.isAdj(v1, v2):
            raise Exception('Vertex ' + str(v1.value) + ' does not have ' + str(v2.value) + ' edge')
        v1._deleteEdge(v2)
    
            
    #to count number of vertices in the graph
    def count_v(self):
        return len(self.vertices)
    
    #to delete the vertex from the graph        
    def deleteVertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError('value must be a Vertex!')
        if not vertex in self.vertices:
            raise ValueError('Vertex does not exist in graph')
        for e in self.vertices:
            e._deleteEdge(vertex)
        self.vertices.remove(vertex)
        return self.vertices
    
    # returns a string representation of the array
    def __repr__(self):	
        return str(self.vertices)
      
            
    def getVertexWithValue(self, value):
        for v in self.vertices:
            if v.value == value:
                return v
            

        
class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()
        
    def addEdge(self, v1, v2, weight = 1):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if v2 in v1.adjList:
            raise Exception('Edge already created!')
        v1._addEdge(v2, weight)
        v2._addEdge(v1, weight)
        
    def deleteEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if not self.isAdj(v1, v2):
            raise Exception('Vertex ' + str(v1.value) + ' does not have ' + str(v2.value) + ' edge')
        v1._deleteEdge(v2)
        v2._deleteEdge(v1)
        
class TSPGraph(UndirectedGraph):
    def __init__(self):
        super().__init__()
        
    def addVertex(self, v, x, y):
        v.setCoords(x, y)
        if len(self.vertices) > 0:
            for u in self.vertices:
                self.addEdge(u, v)
        self.vertices.append(v)
    
    def addEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if v2 in v1.adjList:
            raise Exception('Edge already created!')
        v1Coords = v1.getCoords()
        v2Coords = v2.getCoords()
        weight = ((v1Coords[0] - v2Coords[0]) ** 2 + (v1Coords[1] - v2Coords[1]) ** 2) ** 0.5
        v1._addEdge(v2, weight)
        v2._addEdge(v1, weight)
        
    def generateRandomNodes(self, num):
        for i in range(num):
            self.addVertex(i)
        for i in range(len(self.vertices) - 1):
            v1 = self.vertices[i]
            for j in range(i + 1, len(self.vertices)):
                v2 = self.vertices[j]
                self.addEdge(v1, v2)
            
        
class Vertex:
    
    def __init__(self, value, x = None, y = None):
        self.value = value 
        self.adjList = []
        self.setCoords(x, y)
		
    def getAdjList(self):
        return self.adjList

    #to add edge to this vertex
    def _addEdge(self, vertex, weight):
        if not isinstance(vertex, Vertex):
            raise TypeError("Value must be a Vertex!")
        if vertex == self:
            raise Exception("cannot add edge to itself")
        if vertex in self.adjList:
            raise Exception('Edge already exists')
        self.adjList.append([vertex, weight])
    
    def _deleteEdge(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError("Value must be a Vertex!")
        for i in range(len(self.adjList) - 1, -1, -1):
            if self.adjList[i][0] == vertex:
                self.adjList.pop(i)
    
    # return a string representation of the vertex
    def __repr__(self):
        return str(self.value)		
        
    def setCoords(self, x, y):
        self.x = x
        self.y = y
        
    def getCoords(self):
        return (self.x, self.y)
        
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.value == other.value
        
    def __hash__(self):
        return hash(str(self.value))

        
def shortest_path(graph, initial, target):
    visited = {initial: 0}
    paths = {}
    nodes = set(graph.vertices)
    while len(nodes) > 0:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node == None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for node in min_node.adjList:
            weight = current_weight + node[1]
            if node[0] not in visited or weight < visited[node[0]]:
                visited[node[0]] = weight
                paths[node[0]] = min_node
    path = [target]
    next = target
    while next != initial:
        next = paths[next]
        path.append(next)
    return visited[target], path[::-1]
        
def dfs_traversal(v, step=1000, visualize=False):
    q = Queue()
    g = Graph()
    visited = []
    _dfs(v, visited, g, q)
    if visualize:
        traversalThread = TraversalDrawer(q, g, step, 'DFS')
        traversalThread.start()
    
def _dfs(v, visited, g, q):
    setVisitedDfs(v, visited, g, q)
    for u in v.adjList:
        setVisitedDfs(u[0], visited, g, q)
    
def setVisitedDfs(v, visited, g, q):
    if v not in visited:
        visited.append(v)
        g.addVertex(v)
        print(v)
        q.put(v.value)
        _dfs(v, visited, g, q)
        
def bfs_traversal(v, step = 1000, visualize=False):
    q = Queue()
    g = Graph()
    visited = []
    queue = []
    setVisitedBfs(v, visited, queue, g, q)
    while len(queue) > 0:
        v = queue.pop(0)
        for u in v.adjList:
            setVisitedBfs(u[0], visited, queue, g, q)
    if visualize:
        traversalThread = TraversalDrawer(q, g, step, 'BFS')
        traversalThread.start()

def setVisitedBfs(v, visited, queue, g, q):
    if v not in visited:
        g.addVertex(v)
        print(v)
        visited.append(v)
        q.put(v.value)
        queue.append(v)
        
def topsort(graph):
    s = []
    visited = []
    for v in graph.vertices:
        if v not in visited:
            topsort_dfs(v, s, visited)
    return s[::-1]
    
def topsort_dfs(v, s, visited):
    visited.append(v)
    for u in v.adjList:
        if u[0] not in visited:
            topsort_dfs(u[0], s, visited)
    s.append(v)
    
def getMinDistNode(arr):      
    lowest = arr[0]
    for e in arr:
        if e[1] < lowest[1]:
            lowest = e
    return lowest
    
def retrieveVertex(g, vertex):
    for e in g.vertices:
        if e == vertex:
            return e 
    return None
    
def greedy1(g, initial, step = 1000, visualize=False):
    q = Queue()
    graph = copy.deepcopy(g)
    initial = retrieveVertex(graph, initial)
    path = [initial]
    q.put([initial])
    if visualize:
        thread = TSPDrawer(q, g, step, 'greedy 1 - ' + str(initial.value), False)
        thread.start()
    dist = 0
    graph.deleteVertex(initial)
    min = (initial, 0)
    while len(path) != len(g.vertices):
        min = getMinDistNode(min[0].adjList)
        graph.deleteVertex(min[0])
        path.append(min[0])
        dist += min[1]
        q.put(path + [])
    min = retrieveVertex(g, min[0])
    for e in min.adjList:
        if e[0] == initial:
            dist += e[1]
            break
    path.append(initial)
    return dist, path
    
def greedy2(g, step = 1000, visualize=False):
    q = Queue()
    if visualize:
        thread = TSPDrawer(q, g, step, 'greedy 2', True)
        thread.start()
    graph = copy.deepcopy(g)
    
    # dictionary to store distances between any two points
    distance_dict = {}
    
    # stores the initial two nodes that are nearest to each other
    first = None
    second = None
    min_dist = 100000
    
    # handshake between all possible two points in the tour
    for node in g.vertices:
        for (neighbor, weight) in node.adjList:
            distance_dict[str(node)+str(neighbor)] = weight
            
            if weight < min_dist:
                min_dist = weight                
                first = node
                second = neighbor

    path = [first, second]
    dist = 0
    
    graph.deleteVertex(first)
    graph.deleteVertex(second)
    q.put(path[:])
    
    # while the path is not complete
    while len(path) != len(g.vertices):
        # variable to represent node with nearest distance from all nodes in the path
        nearest_in_path = None
        nearest_to_add = None
        
        # represents nearest distance
        nearest_dist = 1000000
        
        # for each vertice alr in the tour
        for vertice in path:
        
            # for each vertice that is not in the tour
            for neighbor in graph.vertices:
                
                # get distance between two points using the dictionary
                dist = distance_dict[str(vertice)+str(neighbor)] 
                    
                if dist < nearest_dist:
                    nearest_dist = dist
                    nearest_in_path = vertice
                    nearest_to_add = neighbor
        
        # get position of vertice in path that contains shortest distance
        curr_pos = path.index(nearest_in_path)    
        
        # choose where to insert the neighbor to the tour
        # e.g. path is A-B, A-C is the next shortest distance to add into the tour
        # compare between C-A-B and A-C-B
        if curr_pos == 0:
            next_in_path = path[curr_pos+1]
            
            # calculating distance of C-A-B
            d1 = nearest_dist + distance_dict[str(nearest_in_path) + str(next_in_path)]
           
            # calculating distance of A-C-B
            d2 = nearest_dist + distance_dict[str(nearest_to_add) + str(next_in_path)]
            
            # append C to the front of the tour
            if d1 < d2:
                path.insert(0,nearest_to_add)
            
            # append C after the first in the tour
            else:
                path.insert(1,nearest_to_add)
                
        # e.g. path is ...-X-Y, Y-Z is the next shortest distance to add into the tour
        # compare between X-Y-Z and X-Z-Y
        elif curr_pos == len(path) - 1:
            prev_in_path = path[curr_pos-1]
            
            # calculating distance of X-Y-Z
            d1 = distance_dict[str(prev_in_path) + str(nearest_in_path)] + nearest_dist
           
            # calculating distance of X-Z-Y
            d2 = distance_dict[str(prev_in_path) + str(nearest_to_add)] + nearest_dist
            
            # append Z to the back of the tour
            if d1 < d2:
                path.append(nearest_to_add)
            
            # append Z before the last in the tour
            else:
                path.insert(len(path)-1,nearest_to_add)
            
        # e.g. path is A-B-C, B-D is the next shortest distance to add into the tour
        # compare between A-D-B-C and A-B-D-C
        else:
            prev_in_path = path[curr_pos-1]
            next_in_path = path[curr_pos+1]
            
            # calculating distance of A-D-B-C
            d1 = distance_dict[str(prev_in_path) + str(nearest_to_add)] + nearest_dist + distance_dict[str(nearest_in_path) + str(next_in_path)]
           
            # calculating distance of A-B-D-C
            d2 = distance_dict[str(prev_in_path) + str(nearest_in_path)] + nearest_dist + distance_dict[str(nearest_to_add) + str(next_in_path)]
            
            # append D before B
            if d1 < d2:
                path.insert(curr_pos, nearest_to_add)
            
            # append D after B
            else:
                path.insert(curr_pos + 1,nearest_to_add) 
        
        # remove vertex from remaining vertexes to add
        graph.deleteVertex(nearest_to_add)
        q.put(path[:])
    # to make the path go back to its start
    path.append(path[0])
    
    total_dist = 0
    for i in range(len(path)-1):
        curr_v = path[i]
        next_v = path[i+1]
        
        # calculate total distance
        total_dist += distance_dict[str(curr_v) + str(next_v)]
        
        # put vertice in queue for visualization
                
    return total_dist, path
    
def two_opt(arr, g, step = 1000, visualize=False):
    q = Queue()
    if visualize:
        thread = TSPDrawer(q, g, step, '2-opt', True)
        thread.start()
    q.put(arr)
    line_arr = generate_line_arr(arr)
    next_arr = resolve_lines(arr, line_arr)
    while next_arr != arr:
        arr = next_arr
        q.put(arr)
        line_arr = generate_line_arr(arr)
        next_arr = resolve_lines(arr, line_arr)
        line_arr = generate_line_arr(arr)
    q.put(arr)
    return next_arr
    
def resolve_lines(result, lineArr):
    for i in range(len(lineArr) - 2):
        for j in range(i + 2, len(lineArr)):
            if do_lines_intersect(lineArr[i], lineArr[j]):
                temp = result[:i + 1]
                temp += result[j:i : -1]
                temp += result[j + 1:]
                return temp 
    return result
      
      
def has_intersect_lines(lineArr):
    for i in range(0, len(lineArr) - 2):
        for j in range(i + 2, len(lineArr)):
            if do_lines_intersect(lineArr[i], lineArr[j]):
                return True
    return False

def generate_line_arr(result):
    lineArr = []
    for i in range(0, len(result) - 1):
        lineArr.append(Line(Point(v=result[i]), Point(v=result[i + 1])))
    return lineArr
  
class Point:
    def __init__(self, x = 0, y = 0, v = None):
        if v != None:
            self.x = v.x 
            self.y = v.y
        else:
            self.x = x
            self.y = y 
  
    def get_x(self):
        return self.x
  
    def get_y(self):
        return self.y 
  
    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
  
class Line:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2 
  
    def get_first(self):
        return self.point1
  
    def get_second(self):
        return self.point2
  
    def __repr__(self):
        return 'p1: ' + str(self.point1) + ', p2: ' + str(self.point2)

def cross_product(a, b):
    return a.x * b.y - b.x * a.y

def is_point_on_line(line, point):
    tempLine = Line(Point(0, 0), Point(line.get_second().x - line.get_first().x, line.get_second().y - line.get_first().y))
    tempPoint = Point(point.x - line.get_first().x, point.y - line.get_first().y)
    r = cross_product(tempLine.get_second(), tempPoint)
    return abs(r) < 0.000001

def is_point_right_of_line(line, point): 
    tempLine = Line(Point(0, 0), Point(line.get_second().x - line.get_first().x, line.get_second().y - line.get_first().y));
    tempPoint = Point(point.x - line.get_first().x, point.y - line.get_first().y);
    return cross_product(tempLine.get_second(), tempPoint) < 0

def line_segment_touches_or_crosses_line(line1, line2):
    return (is_point_right_of_line(line1, line2.get_first()) ^ is_point_right_of_line(line1, line2.get_second()))

def do_lines_intersect(line1, line2):
    return line_segment_touches_or_crosses_line(line1, line2) and line_segment_touches_or_crosses_line(line2, line1)
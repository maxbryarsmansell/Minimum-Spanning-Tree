import tkinter, os, random, math, time

# Properties
w = 800
h = 600
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
maxVertices = 10
animationDelay = 300 # ms
    
def createGraph(maxVertices):
    vertices = random.randint(5, maxVertices)
    graphWeights = [math.inf] * vertices ** 2
    graphPositions = []
    for vertex in range(0, vertices):
        x = random.randint(0, w)
        y = random.randint(0, h)
        position = [x, y]
        graphPositions.append(position)

    for col in range(0, vertices):
        for row in range(col + 1, vertices):
            currentRow = []
            connections = 0
            for e in range(0, vertices):
                currentRow.append(graphWeights[row + e * vertices])
            if (currentRow.count(math.inf) > vertices - 2 and connections < 3):
                weight = round((((graphPositions[col][0] - graphPositions[row][0]) ** 2) + ((graphPositions[col][1] - graphPositions[row][1]) ** 2) ) ** 0.5)
                graphWeights[row + col * vertices] = weight
                graphWeights[col + row * vertices] = weight
                connections += 1
    return [graphWeights, graphPositions, vertices]


def Prims(graph):
    spanningTreePositions = graph[1]
    verts = graph[2]
    spanningTreeWeights = [math.inf] * verts ** 2
    openNodes = [0]
    while (len(openNodes) < verts):
        smallest = math.inf
        smallestYIndex = -1
        smallestXIndex = -1
        for i in range(0, len(openNodes)):
            column = graph[0][ (openNodes[i] * verts) : ((openNodes[i] + 1) * verts)]
            for j in range(0, len(column)):
                value = column[j]
                if (value < smallest and j not in openNodes):
                    smallest = value
                    smallestYIndex = j
                    smallestXIndex = openNodes[i]
        openNodes.append(smallestYIndex)
        spanningTreeWeights[smallestYIndex + smallestXIndex * verts] = smallest
        spanningTreeWeights[smallestXIndex + smallestYIndex * verts] = smallest
        window.update()
        window.update_idletasks()
        canvas.delete("all")
        drawGraph(graph, "blue")
        drawGraph([spanningTreeWeights, spanningTreePositions, verts], "red")
        time.sleep(animationDelay / 1000)
    return [spanningTreeWeights, spanningTreePositions , verts]
                           
def drawGraph(graph, colour):
    for col in range(0, graph[2]):
        for row in range(col + 1, graph[2]):
            if (graph[0][row + col * graph[2]] != math.inf):
                canvas.create_line(graph[1][col][0], graph[1][col][1], graph[1][row][0], graph[1][row][1], fill=colour, width=8)
                canvas.create_text((graph[1][col][0] + graph[1][row][0]) / 2,(graph[1][col][1] + graph[1][row][1]) / 2,fill="white",font="Helvetica 15 bold", text=graph[0][row + col * graph[2]])
        
        canvas.create_oval(graph[1][col][0]-10, graph[1][col][1]-10, graph[1][col][0]+10, graph[1][col][1]+10, fill=colour)
        canvas.create_text(graph[1][col][0],graph[1][col][1],fill="white",font="Helvetica 20 bold", text=alphabet[col])


window = tkinter.Tk()
window.title("Spanning Tree")
canvas = tkinter.Canvas(window, bg="black", height=h, width=w)
canvas.pack()

graph = createGraph(maxVertices)

Prims(graph)

window.mainloop()

    





    



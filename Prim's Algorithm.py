import tkinter, os, random, math

# Properties
w = 800
h = 600
vertices = 5
    

graphWeights = [math.inf] * vertices ** 2
graphPositions = []
for vertex in range(0, vertices):
    x = random.randint(0, w)
    y = random.randint(0, h)
    position = [x, y]
    graphPositions.append(position)

for col in range(0, vertices):
    columnA = graphWeights[col * vertices:(col + 1) * vertices]
    connections = 0 #len(columnA) - columnA.count(math.inf)
    for row in range(col + 1, vertices):
        rowA = []
        for e in range(0, vertices):
            rowA.append(graphWeights[row + e * vertices])
        if (connections < 2 and math.inf in rowA):
                weight = round((((graphPositions[col][0] - graphPositions[row][0]) ** 2) + ((graphPositions[col][1] - graphPositions[row][1]) ** 2) ) ** 0.5)
                graphWeights[row + col * vertices] = weight
                graphWeights[col + row * vertices] = weight
                connections += 1

print(graphPositions)
print("\n")

for x in range(0, vertices):
    result = ""
    for y in range(0, vertices):
        result += str(graphWeights[x + y * vertices]) + ", "
    print(result)

print("\n")


def Prims(graph):
    verts = int(len(graph) ** 0.5)
    spanningTree = [math.inf] * verts ** 2
    openNodes = [0]
    while (len(openNodes) < verts):
        smallest = math.inf
        smallestYIndex = -1
        smallestXIndex = -1
        for i in range(0, len(openNodes)):
            
            column = graph[ (openNodes[i] * verts) : ((openNodes[i] + 1) * verts)]
            #print("OpenNodes value: ",openNodes[i])
            #print("Colunm: ", column)
            for j in range(0, len(column)):
                value = column[j]
                if (value < smallest and j not in openNodes):
                    smallest = value
                    #print("Value: ",value,"I: ",openNodes[i],"J: ",j)
                    smallestYIndex = j
                    smallestXIndex = openNodes[i]
        #print(smallestXIndex, ", ", smallestYIndex)
        openNodes.append(smallestYIndex)
        #print(openNodes)
        spanningTree[smallestYIndex + smallestXIndex * verts] = smallest
        spanningTree[smallestXIndex + smallestYIndex * verts] = smallest
    return spanningTree
                      
tree = Prims(graphWeights)      
                

window = tkinter.Tk()
window.title("Spanning Tree")
canvas = tkinter.Canvas(window, bg="black", height=h, width=w)
canvas.pack()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for col in range(0, vertices):
    canvas.create_oval(graphPositions[col][0]-10, graphPositions[col][1]-10, graphPositions[col][0]+10, graphPositions[col][1]+10, fill='blue')
    for row in range(col + 1, vertices):
        if (graphWeights[row + col * vertices] != math.inf):
            canvas.create_line(graphPositions[col][0], graphPositions[col][1], graphPositions[row][0], graphPositions[row][1], fill='blue', width=8)
            canvas.create_text((graphPositions[col][0] + graphPositions[row][0]) / 2,(graphPositions[col][1] + graphPositions[row][1]) / 2,fill="white",font="Helvetica 15 bold", text=graphWeights[row + col * vertices])

for col in range(0, vertices):
    for row in range(col + 1, vertices):
        if (tree[row + col * vertices] != math.inf):
            canvas.create_line(graphPositions[col][0], graphPositions[col][1], graphPositions[row][0], graphPositions[row][1], fill='red', width=5)
            canvas.create_text((graphPositions[col][0] + graphPositions[row][0]) / 2,(graphPositions[col][1] + graphPositions[row][1]) / 2,fill="yellow",font="Helvetica 15 bold", text=graphWeights[row + col * vertices])
    canvas.create_oval(graphPositions[col][0]-5, graphPositions[col][1]-5, graphPositions[col][0]+5, graphPositions[col][1]+5, fill='red')
    canvas.create_text(graphPositions[col][0],graphPositions[col][1],fill="white",font="Helvetica 20 bold", text=alphabet[col])


window.mainloop()



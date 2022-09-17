import random
shapes = [[[1,1],
        [0,1],
        [0,1]],

       [[1,1],
        [1,0],
        [1,0]],
       
       [[1,0],
        [1,0],
        [1,1]],

       [[0,1],
        [0,1],
        [1,1]],
       
       [[1,0,0],
        [1,1,1]],  

       [[0,0,1],
        [1,1,1]],

       [[1,1,1],
        [1,0,0]],
       
       [[1,1,1],
        [0,0,1]]]
shapesList = [0,1,2,3,4,5,6,7]
#Grundfeld, entweder 4,6 oder 8,8
rows = 4
cols = 6
globalField = [[0]*cols]*rows
#Startposition List for Randomization
posX = [0]
posY = [0]
x = 1
y = 1
while y <= (rows-len(shapes[0])+1):
    posY.append(y)
    y = y + 1
    
while x <= (cols-len(shapes[7][0])+1):
    posX.append(x)
    x = x + 1
#Zähler um zu messen wann das Feld voll ist.
counter = 0
upperLimit = (rows*cols)/4

def fit(checkShape, checkField, checkPosX, checkPosY):
    
    if (checkPosY + len(checkShape) >= len(checkField[0])):
        return 0
    if (checkPosX + len(checkShape[0]) >= len(checkField)):
        return 0
    i = 0
    j = 0
    while i < len(checkShape):
        while j < len(checkShape[i]):
            if checkShape[i][j] != 0:
                if checkField[i + checkPosX][j + checkPosY] != 0:
                    return 0
            j = j + 1
        i = i + 1
    return 1        

def fill(field, objectsPlaced):
    print (posX)
    copyField = [[0]*cols]*rows
    i = 0
    j = 0
    while i < len(field):
        while j < len(field[i]):
            copyField[i][j] = field[i][j]
            j = j + 1
        i = i + 1
    random.shuffle(shapes)
    random.shuffle(posX)
    random.shuffle(posY)
    for shape in shapes:
        for positionRow in posY:
            for positionCol in posX:
                if fit(shape, copyField, positionRow, positionCol):
                    objectsPlaced = objectsPlaced + 1
                    i = 0
                    j = 0
                    c = 0
                    print (shape)
                    while i < len(shape):
                        while j < len(shape[i]):
                            print(i + positionCol)
                            if shape[i][j] != 0:
                                c = c + 1
                                copyField[i + positionRow][j + positionCol] = objectsPlaced
                            j = j + 1
                        i = i + 1
                    print(c)
                    if objectsPlaced >= upperLimit:
                        return copyField
                    else: 
                        return fill(copyField, objectsPlaced)
                        
                    
                        
    return field


objectsPlaced = 0
initialField = [[0]*cols]*rows
result = fill(initialField, objectsPlaced)
for column in result:
    print (column)
print("finished")
                    



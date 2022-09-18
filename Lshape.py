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
#Grundfeld, entweder 4,6 oder 8,8
#Leider fürt die Multiplikation der Felder zu Fehlern
rows = 16
cols = 8
#Startposition List for Randomization
posX = [0]
posY = [0]
x = 1
y = 1
while y <= (rows-len(shapes[7][0])+1):
    posY.append(y)
    y = y + 1
    
while x <= (cols-len(shapes[0])+1):
    posX.append(x)
    x = x + 1
print(posX)
print(posY)
#Zähler um zu messen wann das Feld voll ist.
counter = 0
upperLimit = (rows*cols)/4

def createField(row,col):
    outer = []
    i = 0
    while i < row:
        inner = [0]
        j = 0
        while j < col-1:
            inner.append(0)
            j += 1
        outer.append(inner)
        i += 1
    return outer

def fit(checkShape, checkField, checkPosX, checkPosY):
    print(str(checkPosX)+str(checkPosY))
    print(checkField)
    if (checkPosY + len(checkShape[0]) >= len(checkField)):
        return 0
    if (checkPosX + len(checkShape) >= len(checkField[0])):
        return 0
    i = 0
    while i < len(checkShape):
        j = 0
        while j < len(checkShape[i]):
            if checkShape[i][j] != 0:
                if checkField[i + checkPosY][j + checkPosX] != 0:
                    return 0
            j += 1
        i += 1
    return 1        

def fill(field, objectsPlaced):
    copyField = createField(rows,cols)
    i = 0
    while i < len(field):
        j = 0
        while j < len(field[i]):
            copyField[i][j] = field[i][j]
            j += 1
        i += 1
    random.shuffle(shapes)
    random.shuffle(posX)
    random.shuffle(posY)
    for shape in shapes:
        for positionCol in posX:
            for positionRow in posY:
                if fit(shape, copyField, positionCol, positionRow):
                    objectsPlaced = objectsPlaced + 1
                    i = 0
                    while i < len(shape):
                        j = 0
                        while j < len(shape[i]):
                            if shape[i][j] != 0:
                                copyField[i + positionRow][j + positionCol] = objectsPlaced
                            j += 1
                        i += 1
                    if objectsPlaced >= upperLimit:
                        return copyField
                    else: 
                        return fill(copyField, objectsPlaced)                              
    return field

objectsPlaced = 0

initialField = createField(rows,cols)
result = fill(initialField, objectsPlaced)
for row in result:
    print (row)
print("finished")
                    



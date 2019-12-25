import copy

def getRestOfSection(i,j,allowed):
    ret = []
    startx = i-(i%3)
    starty = j-(j%3)
    for x in range(3):
        for y in range(3):
            ret.extend(allowed[startx+x][starty+y])
    for x in allowed[i][j]:
        if x in ret:
            ret.remove(x)
    return ret

def gridSame(g1, g2):
    for i in range(len(g1)):
        for j in range(len(g1[0])):
            if g1[i][j] != g2[i][j]:
                return False
    return True

def refreshSections(grid):
    sections = []
    for startx in range(3):
        for starty in range(3):
            toAdd = []
            for i in range(3):
                for j in range(3):
                    toAdd.append(grid[startx*3+i][starty*3+j])
            sections.append(toAdd)
    return sections

def refreshCols(grid):
    cols = []
    for j in range(len(grid[0])):
        column = []
        for i in range(len(grid)):
            column.append(grid[i][j])

        cols.append(column)
    return cols

# 9x9
grid = [[0,0,3,0,0,0,5,6,0],[0,9,0,4,0,0,0,0,2],[0,4,0,1,5,0,0,3,0],[0,0,1,0,0,8,4,0,7],[0,0,0,0,2,0,0,0,0],[3,0,6,7,0,0,2,0,0],[0,6,0,0,8,1,0,7,0],[7,0,0,0,0,5,0,2,0],[0,3,2,0,0,0,8,4,0]] 

# for i in range(len(grid)):
#     print(grid[i])

numbers = [1,2,3,4,5,6,7,8,9]

cols = refreshCols(grid)

# for each position, what is allowed in the position
allowed = [[0,0,3,0,0,0,5,6,0],[0,9,0,4,0,0,0,0,2],[0,4,0,1,5,0,0,3,0],[0,0,1,0,0,8,4,0,7],[0,0,0,0,2,0,0,0,0],[3,0,6,7,0,0,2,0,0],[0,6,0,0,8,1,0,7,0],[7,0,0,0,0,5,0,2,0],[0,3,2,0,0,0,8,4,0]] 

findSection = [[0,0,3,0,0,0,5,6,0],[0,9,0,4,0,0,0,0,2],[0,4,0,1,5,0,0,3,0],[0,0,1,0,0,8,4,0,7],[0,0,0,0,2,0,0,0,0],[3,0,6,7,0,0,2,0,0],[0,6,0,0,8,1,0,7,0],[7,0,0,0,0,5,0,2,0],[0,3,2,0,0,0,8,4,0]] 


sectionCounter = 0
for startx in range(3):
    for starty in range(3):
        for i in range(3):
            for j in range(3):
                findSection[startx*3+i][starty*3+j] = sectionCounter
        sectionCounter += 1

print("findSection")
print(findSection)



print("cols")

print(cols)

# sections
sections = refreshSections(grid)



print("sections")

print(sections)

oldGrid = copy.deepcopy(grid)

while(0 not in grid):
    allowed = copy.deepcopy(grid)
    sections = refreshSections(grid)
    print("Sections: ", sections)
    cols = refreshCols(grid)
    print("Cols: ", cols)

    # print(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == 0):
                # print("Doing ",i,", ",j)
                toAppend = [1,2,3,4,5,6,7,8,9]
                for x in grid[i]:
                    # once you remove the values not allowed, you're left with allowed
                    if(x in toAppend):
                        toAppend.remove(x)
                # print("Col, ", cols[j])
                for x in cols[j]:
                    if(x in toAppend):
                        toAppend.remove(x)
                for x in sections[findSection[i][j]]:
                    if(x in toAppend):
                        toAppend.remove(x)
                allowed[i][j] = toAppend
            else:
                allowed[i][j] = []

            

    # for i in range(9):
    #     print(allowed[i])
    print("********")

    # oldgrid = grid.copy()

    for i in range(9):
        print(oldGrid[i])
    

    print("*******")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                if len(allowed[i][j]) == 1:
                    grid[i][j] = allowed[i][j][0]
                    continue;
                restOfSection = getRestOfSection(i,j,allowed)
                # print("REST OF SECTION: ", restOfSection)
                # print("ALLOWED IN SPOT: ", i,j," ", allowed[i][j])
                for x in allowed[i][j]:
                    if x not in restOfSection:
                        # grid[i][j] = "NEW: " + str(x)
                        grid[i][j] = x
                        break;

    for i in range(9):
        print(grid[i])


    if gridSame(oldGrid, grid):
        print("Loop detected, breaking")
        break;
    # use deep copy because 2d array, one copy only copies the outer ring, the inner ring is still a reference
    oldGrid = copy.deepcopy(grid)

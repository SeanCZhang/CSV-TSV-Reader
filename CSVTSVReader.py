#Program takes either a .csv or .tsv file and creates a table. User can print all columns or choose certain columns to display.

#Function validates when user selects columns. Returns value if in range (or returns key if in parameter list and input matches)
def validInput(question, validRange, key=None):
    while True:
        try:
            currentColumn = input(question)
            if key != None:
                if currentColumn == key or currentColumn.upper() == key:
                    return key
            if int(currentColumn) in range(validRange):
                return int(currentColumn)
            else:
                print("Not a column in the table! Try again. ")
        except ValueError as e:
            print ("Not a valid input! Try again.")           
#User inputs the valid .csv or .tsv file to be read
while True:
    try:
        filename = input("Please type the name of your CSV or TSV file with its extension (ex. 'file.csv'): ")
        if filename.endswith(".csv") == False and filename.endswith(".tsv") == False:
            print("Not a valid extension! Please try again.")
            continue
        file = open(filename, "r")
        break
    except FileNotFoundError as e:
        print("File not found! Please try again.")
#Delimiter based on file extension
if filename.endswith(".csv"):
    delimiter = ","
elif filename.endswith(".tsv"):
    delimiter = "\t"
#Converts each line into a list and appends to table 
table = list()
while len(line := file.readline()) != 0:
    line = line.strip()
    row = line.split(delimiter)
    table.append(row)
file.close()
columnNames = table[0]
#Create list that stores length of longest entry in each column
maxColumnLengths = list()
for name in columnNames:
    max = -1
    for row in table:
        if len(row[columnNames.index(name)]) > max:
            max = len(row[columnNames.index(name)])
    maxColumnLengths.append(max)
columnCount = 0
print("The columns in this file are: ")
for name in columnNames:
    print ("(" + str(columnCount) + ")" + name, end=' ')
    columnCount = columnCount+1
print()
while True:
    readAll = input("Read all columns? (Y/N): ")
    if readAll.upper() == 'N':
        #Takes input and stores column
        selectedColumns = list()
        currentColumn = validInput("Add a column (0" + "-" + str(columnCount-1) + ") to be read: ", columnCount,)
        selectedColumns.append(currentColumn)
        print ("Selected columns: ", end='')
        for columnNum in selectedColumns:
            print("(" + str(columnNum) + ") " + columnNames[columnNum])
        #Keeps asking for columns to add until user inputs 'R' to print
        while True:
            currentColumn = validInput("Add a column (0" + "-" + str(columnCount-1) + ") to be read ('R' to read selected columns): ", columnCount, 'R')
            #Asks to input again if chosen column already selected
            while True:
                if currentColumn in selectedColumns:
                    print ("You have already selected that column!")
                    print ("Selected columns: ", end='')
                    for columnNum in selectedColumns:
                        print("(" + str(columnNum) + ") " + columnNames[columnNum], end='  ')
                    print()
                    currentColumn = validInput("Add a column (0" + "-" + str(columnCount-1) + ") to be read ('R' to read selected columns): ", columnCount, 'R')
                else:
                    break
            if currentColumn == 'R':
                break
            selectedColumns.append(currentColumn)
            print ("Selected columns: ", end='')
            for columnNum in selectedColumns:
                print("(" + str(columnNum) + ") " + columnNames[columnNum], end='  ')
            print()
        #Print selected columns with justification based on each column's longest entry
        for row in table:
            for columnNum in selectedColumns:
                print(row[columnNum].ljust(maxColumnLengths[columnNum]), end='   ')
            print()
        break
    if readAll.upper() == 'Y':
        #Print all columns with justification based on each column's longest entry
        for row in table:
            for name in columnNames:
                print (row[columnNames.index(name)].ljust(maxColumnLengths[columnNames.index(name)]), end='   ')
            print()
        break
    else:
        print("Not a valid input! Try again.")
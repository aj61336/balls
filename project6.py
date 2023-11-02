def main():
    # opens and reads file
    with open("student roster example.csv") as rosterFile:
        linees=rosterFile.readLines()
    
    # list for the program
    programCodeArray=[]
    
    dataArray=lines[0].split()
    print(dataArray)
    programCodeArray.append(dataArray[5])
    print(programCodeArray)

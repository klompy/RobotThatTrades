import pandas as pd 

class getData():
    def __init__(self):
        self.folder = "data//" #Assumes getData.py is in the same directory as data
        self.csv = ".csv"

    # Allows you to set path getData looks for the file in
    def setFolder(self, folder: str):
        self.folder = folder
    
    #returns DataFrame of symbol.csv from the specified folder, if it cannot find it -> returns file path and error message
    def getData(self, symbol: str):
        path = self.folder + symbol + self.csv
        try:
            return(pd.read_csv(path))
        
        except:
            # This is jank, trying to return path + '\n' + "..." was acting up so did this instead
            print(path)
            return("^^ Was not valid or your data has encoding which caused issues")
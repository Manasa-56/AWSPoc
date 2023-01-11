import pandas as pd
import pyorc

def converttoORC(inputFilePath, orcFilePath ):
    """Converts the .CSV file to .ORC format"""
    df = pd.read_csv(inputFilePath, low_memory= False)
    dtypes = df.dtypes 
    dtypes = dtypes.astype(str)
    df = df.astype(str)
    columnNames = list(df.columns)

    structure = "struct<" 
    for i,j in zip(columnNames, dtypes):
        structure = structure + i + ':'+ 'string' + ','
    structure = structure[:-1] + '>'
    with open(orcFilePath, "wb") as data:
        with pyorc.Writer(data, structure) as writer:
            for i in df.index:
                writer.write(
                    (df.iloc[:, 0][i], df.iloc[:, 1][i], df.iloc[:, 2][i], df.iloc[:, 3][i], df.iloc[:, 4][i], df.iloc[:, 5][i] , df.iloc[:, 6][i], df.iloc[:, 7][i], df.iloc[:, 8][i], df.iloc[:, 9][i], df.iloc[:, 10][i], df.iloc[:, 11][i],df.iloc[:, 12][i], df.iloc[:, 13][i], df.iloc[:, 14][i], df.iloc[:, 15][i], df.iloc[:, 16][i], df.iloc[:, 17][i])
                )


# , df.iloc[:, 6][i], df.iloc[:, 7][i], df.iloc[:, 8][i], df.iloc[:, 9][i], df.iloc[:, 10][i], df.iloc[:, 11][i],df.iloc[:, 12][i], df.iloc[:, 13][i], df.iloc[:, 14][i], df.iloc[:, 15][i], df.iloc[:, 16][i], df.iloc[:, 17][i])
    

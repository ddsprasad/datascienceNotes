##UTILITIES

#########References

def createDF_fromdir_csv(path):
    import pandas as pd
    import glob
    """
    This will create dataframe from a dir with all csv files in it
    input param: 
    """
    all_files = glob.glob(path+"/*.csv")
    li = []
    for file in all_files:
        df = pd.read_csv(file, header=0, index_col=None)
        li.append(df)
        
    all_data = pd.concat(li, axis=0, ignore_index=True)
    return all_data


#this converts $10M values to $10000000

def value_to_float(x):
    """
    This iterates over the each value of dataframe in column then converts  them from $10M to 10000000
    input param: dataframe row
    usage: ex: wage = df2['Wage'].apply(value_to_float)
    """
    import re
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(re.sub('[€K]', '', x,flags=re.UNICODE)) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(re.sub('[€M]', '', x,flags=re.UNICODE)) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(re.sub('[€B]', '', x,flags=re.UNICODE)) * 1000000000
    return 0.0

##########################################To create a connection for MYSQL

import mysql.connector


config = {
  'user': 'root',
  'password': 'Lagom@99',
  'host': 'localhost',
  'database': 'dictionary',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

# con = mysql.connector.connect(
#     user = 'ardit700_student',
#     password= 'ardit700_student',
#     host = '108.167.140.122',
#     database = 'ardit700_pm1database'
# )


# print(con)

cusr = cnx.cursor()

query = cusr.execute("SELECT * FROM entries WHERE word = 'flag' ")

resutls = cusr.fetchall()

for i in resutls:
    print("-----------\n")
    print(i[2])
    
##################################Quick Notes

#this enables mutiple prints on the notebook console
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
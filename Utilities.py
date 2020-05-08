###UTILITIES

#########References

#This will create dataframe from a dir with all csv files in it
import pandas as pd
import glob

def createDF_fromdir_csv(path):
    all_files = glob.glob(path+"/*.csv")
    li = []
    for file in all_files:
        df = pd.read_csv(file, header=0, index_col=None)
        li.append(df)
        
    all_data = pd.concat(li, axis=0, ignore_index=True)
    return all_data

##############To create a connection for MYSQL

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
    
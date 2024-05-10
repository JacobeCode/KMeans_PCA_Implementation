# Manual implementation of StandardScaler for project purpose - working for databases

import numpy as np
import pandas as pd

class standard_scaler:
    def __init__(self):
        pass
    def scale(self, database):
        data=[]
        for column in database:
            col=[]
            for iter, item in enumerate(database[column]):
                col.append((item-np.mean(database[column]))/np.std(database[column]))
            data.append(col)

        database = pd.DataFrame(np.transpose(data), columns=database.columns)
        return database
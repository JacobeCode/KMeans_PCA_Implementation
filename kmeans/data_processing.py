import matplotlib

import numpy as np
import pandas as pd

from pandas.plotting import scatter_matrix

class csv_data_processing:
    def __init__(self):
        self.database=pd.DataFrame

    def process_data(self, database_name):
        self.database=pd.read_csv(database_name)

        for column in self.database:
            unique=self.database[column].unique()
            for iter, token in enumerate(unique):
                if isinstance(token, str) is True:
                    for pos, item in enumerate(self.database[column]):
                        if token is item:
                            self.database.loc[pos, column]=iter
        return self.database


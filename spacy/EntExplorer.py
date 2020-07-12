import pandas as pd

class Ents:
    def __init__(self):
        self.df = pd.read_csv('../data/ent_counts/ents_1.csv')

    def Explorer(self):
        print (self.df['2016-01-22_ents'])








if __name__ == '__main__':
    Ents().Explorer()

import pandas as pd
import regex as re

class TextRunner:

    def __init__(self):
        self.df = pd.DataFrame()
        self.df_out = pd.DataFrame()

    def _Cleaner(self, file):
        self.df = pd.read_csv(file)
        cleaned = []
        curr = 1
        for item in self.df['body']:

            try:
                text = item.replace("'", "")
                text = text.replace("\n", "")
                cleaned.append(text)
            except:
                print(f'Skipping line {curr}')

            curr += 1

        self.df_out['text'] = cleaned
        self.df_out['text'] = self.df_out['text'].str.lower().apply(lambda x: re.sub("[^a-z\s]", " ", x))
        self.df_out['text'].dropna(inplace=True)
        return self.df_out
        # self.df_out.to_json('./training_data/cleaned_training_data.jsonl', orient='records', lines=True)

    def SpacyPrinter(self):
        self.df = pd.read_json('./CON_patters.jsonl', orient='records', lines=True)
        print(self.df.head())

    def Explorer(self):
        file = './the_donald/bq-results-1.csv'
        self.df = self._Cleaner(file)
        print(self.df.head())






if __name__ == '__main__':
    TextRunner().Explorer()
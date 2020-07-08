import pandas as pd
import regex as re

class TextRunner:

    def __init__(self):
        self.df = pd.read_csv('./training_data/collected_term_comments.csv')
        self.df_out = pd.DataFrame()

    def Cleaner(self):
        cleaned = []
        for item in self.df['text']:
            text = item.replace("'", "")
            text = text.replace("\n", "")
            cleaned.append(text)
        self.df['text'] = cleaned
        self.df['text'] = self.df['text'].str.lower().apply(lambda x: re.sub("[^a-z\s]", " ", x))
        self.df_out['text'] = self.df['text']
        self.df_out.to_json('./training_data/cleaned_training_data.jsonl', orient='records', lines=True)






if __name__ == '__main__':
    TextRunner().Cleaner()
import pandas as pd
import regex as re
import spacy

class TextRunner:

    def __init__(self):
        self.df = pd.DataFrame()
        self.df_out = pd.DataFrame()
        self.model = None

    def _Cleaner(self, file):
        self.df = pd.read_csv(file)
        cleaned = []
        dates = []
        curr = 1
        for text, date in zip(self.df['body'], self.df['created_utc']):

            try:
                text = text.replace("'", "")
                text = text.replace("\n", "")
                cleaned.append(text)
                dates.append(date)
            except:
                print(f'Skipping line {curr}')
            curr += 1

        self.df_out['text'] = cleaned
        self.df_out['date'] = dates
        self.df_out['text'] = self.df_out['text'].str.lower().apply(lambda x: re.sub("[^a-z\s]", " ", x))
        self.df_out['text'].dropna(inplace=True)
        self.df_out.sort_values(by='date', axis=0, ascending=True, inplace=True)
        return self.df_out
        # self.df_out.to_json('./training_data/cleaned_training_data.jsonl', orient='records', lines=True)

    def SpacyPrinter(self):
        self.df = pd.read_json('./CON_patters.jsonl', orient='records', lines=True)
        print(self.df.head())

    def SpacyExplorer(self, model):
        file = './the_donald/bq-results-1.csv'
        self.df = self._Cleaner(file)
        self.model = model
        print(f'Loading Model: {self.model}...')
        nlp = spacy.load(self.model)

        doc = nlp(text)
        ents = []
        for item in doc.ents:
            ents.append(item)
        print(ents)

    def SpacyTest(self, model):

        self.model = model
        print(f'Loading Model: {self.model}...')
        nlp = spacy.load(self.model)
        print(f'Processing Text...')
        a = "george soros went to the supermarket where he saw black lives matter protesting the killing of seth rich over hillarys emails, clintons emails, and podestas emails."
        b = 'george smiled knowing that blm and blue lives matter are just globalist plots to cover up the human trafficing and pedo pizzagate activities taking place in benghazi. jeffery epstein.'
        c = a + b
        doc = nlp(c)
        ents = []
        for item in doc.ents:
            ents.append(item)
        print(ents)



if __name__ == '__main__':
    TextRunner().SpacyTest('donald_model')
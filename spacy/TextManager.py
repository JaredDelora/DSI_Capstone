import pandas as pd
import regex as re
import spacy
import datetime

class TextRunner:

    def __init__(self):
        self.df = None
        self.df_out = None
        self.model = None

    @staticmethod
    def _Cleaners(file, column1, column2):
        df = pd.read_csv(file)
        df_out = pd.DataFrame()
        cleaned_text = []
        dates = []
        curr = 1
        for text, date in zip(df[column1], df[column2]):

            try:
                text = text.replace("'", "")
                text = text.replace("\n", "")
                text = text.replace("gopdebate", "")
                cleaned_text.append(text)
                dates.append(date)
            except:
                print(f'Skipping line {curr}')
            curr += 1

        df_out['text'] = cleaned_text
        df_out['date'] = dates
        df_out['text'] = df_out['text'].str.lower().apply(lambda x: re.sub("[^a-z\s]", " ", x))
        df_out['text'].dropna(inplace=True)
        df_out.sort_values(by='date', axis=0, ascending=True, inplace=True)
        return df_out
        # self.df_out.to_json('./training_data/cleaned_training_data.jsonl', orient='records', lines=True)

    def _SpacyPrinter(self):
        self.df = pd.read_json('./CON_patters.jsonl', orient='records', lines=True)
        print(self.df.head())

    def _RedditExplorer(self, file):
        print(f'Reading and Cleaning file: {file}')
        df_temp = self._Cleaners(file, "body", "created_utc")
        dates = []
        comments = []
        print('Reformating Dates...')
        for item in df_temp['date']:
            utc_date = datetime.datetime.utcfromtimestamp(item)
            date = str(utc_date).split()[0]
            dates.append(date)

        df_temp['date'] = dates
        return df_temp

    def EntCounter(self):
        month = 2
        in_file = './the_donald/bq-results-' + str(month) + '.csv'
        df = self._RedditExplorer(in_file)
        print(df.columns)

        df_out = pd.DataFrame()
        print(f'Loading spaCy Model...')

        nlp = spacy.load('donald_model')
        nlp.max_length = 2_000_000
        dates = []
        texts = []


        for i in range(1, 32):
            df_temp = pd.DataFrame()
            X_df = pd.DataFrame()
            ent_list = []
            #First we will create a string of our current date, we will loop through all the days in the month
            if i < 10:
                curr_date = '2016-02-0' + str(i)
            else:
                curr_date = '2016-02-' + str(i)
            print(f'Currently processing date: {curr_date}')

            # Now we will run through all the tweets of the day and build them into a single string
            # Passing the whole day in at once to spaCy is much more efficient than doing it one tweet at a time.
            print('Building string...')
            day_string = ""
            for tweet, date in zip(df['text'], df['date']):
                if date == curr_date:
                    day_string = day_string + " " + tweet

            # Now we'll pass our string into our spaCy model
            print('Passing string to spaCy...')
            doc = nlp(day_string)

            # Now we'l' convert each ent from a spaCy object to a string and stick them in a list
            print("Building Ent List...")
            for item in doc.ents:
                ent_list.append(str(item))

            # If there are ents present then we count them

            if len(ent_list) > 0:
                print("Creating Ent Counts...")
                df_temp['ents'] = ent_list

                # .value_counts() returns a pandas series object, not a dataframe
                X = df_temp['ents'].value_counts()

                # Populate a dataframe with the index (ent names) of the pandas series and the series values
                X_df['ents'] = X.index
                X_df['count'] = list(X)
                # Just gonna keep the top 15 so our dataframe columns are consistant
                X_df = X_df.head(15).copy()
                df_out[curr_date + '_ents'] = X_df['ents']
                df_out[curr_date + '_count'] = X_df['count']

        out_string = '../data/ent_counts/ents_' + str(month) + '.csv'
        df_out.to_csv(out_string)
        print(df_out.head(15))


    def TrumpTweets(self, model):
        print("Reading in Trump Tweets...")
        in_file = '../data/trumptweets.csv'

        print("Cleaning the Data...")
        self.df = self._Cleaner(file=in_file, column1='text', column2='created_at')
        print(f'Loading scaCy model: {model}...')
        nlp = spacy.load(model)
        dates = []
        texts = []

        print('Reformating the Data...')
        for text, date in zip(self.df['text'], self.df['date']):
            curr_date = date.split()[0]
            texts.append(text)
            dates.append(curr_date)

        self.df_out = pd.DataFrame()
        self.df_out['text'] = texts
        self.df_out['date'] = dates


        ent_list = []

        for tweet in self.df_out['text']:
            df_temp = pd.DataFrame()
            doc = nlp(tweet)

            for item in doc.ents:
                ent_list.append(str(item))

            ent_set = set(ent_list)
            ent_list = list(ent_set)

            if len(ent_list) > 0:
                df_temp['ents'] = ent_list
                try:
                    print(df_temp['ents'].value_counts())
                    return None

                except:
                    print('Error...')

    @staticmethod
    def SpacyTest(model):

        print(f'Loading Model: {model}...')
        nlp = spacy.load(model)
        print(f'Processing Text...')
        a = "george soros went to the seth rich supermarket where he saw black lives matter protesting the killing of seth rich over hillarys emails, clintons emails, and podestas emails."
        b = "george smiled knowing that blm, pizzagate blue lives matter are just globalist plots to cover up clintons email and the human trafficing and pedo pizzagate activities taking place in benghazi. jeffery epstein."
        c = a + b
        doc = nlp(c)
        ent_list = []
        ent_count = []
        # print(len(doc.ents))
        for item in doc.ents:
            ent_list.append(str(item))
        # print(ent_list)
        ent_set = set(ent_list)
        # print(len(ent_set))
        for ent in ent_set:
            curr_count = ent_list.count(ent)
            ent_count.append(curr_count)
            print(ent)
            print(curr_count)




if __name__ == '__main__':
    TextRunner().EntCounter()
    # TextRunner().SpacyTest('donald_model')
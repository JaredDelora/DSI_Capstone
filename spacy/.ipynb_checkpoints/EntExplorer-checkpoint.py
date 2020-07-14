import pandas as pd

class Ents:
    def __init__(self):
        self.df = None

    def SethRich(self):
        # Seth Rich was murdered on July 10, 2016
        df_SR = pd.DataFrame()
        month = 9
        in_file = '../data/ent_counts/ents_' + str(month) + '.csv'
        self.df = pd.read_csv(in_file)
        ent_list = []
        count_list = []
        dates = []
        for i in range(1, 32):
            if i < 10:
                curr_date = '2016-09-0' + str(i)
            else:
                curr_date = '2016-09-' + str(i)
            print(f'Currently processing date: {curr_date}')
            curr_ent_column = str(curr_date) + "_ents"
            curr_count_column = str(curr_date) + "_count"
            try:
                for ent, count in zip(self.df[curr_ent_column], self.df[curr_count_column]):
                    if ent == "seth rich":
                        ent_list.append(ent)
                        count_list.append(count)
                        dates.append(curr_date)


            except:
                print(f'Passing {curr_date}')
        df_SR['date'] = dates
        df_SR['ent'] = ent_list
        df_SR['count'] = count_list
        print(df_SR.head())
        df_SR.to_csv('./ent_dataframes/sept_seth_rich_ents')






if __name__ == '__main__':
    Ents().SethRich()

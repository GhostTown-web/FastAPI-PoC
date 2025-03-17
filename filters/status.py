import pandas as pd

class FilterStatus:

    def __init__(self):
        self.df = pd.read_csv('./final_clean_data.csv')

    def create_json(self):
        result = self.df.groupby("Trial Status")["Trial ID"].count()

        return result.to_dict()

obj = FilterStatus()
obj.create_json()
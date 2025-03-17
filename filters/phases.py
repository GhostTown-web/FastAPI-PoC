import pandas as pd

class FilterPhases:

    def __init__(self):
        self.df = pd.read_csv('./final_clean_data.csv')

    def create_json(self):
        result = self.df.groupby('Trial Phase')["Trial ID"].count()

        return result.to_dict()


# obj = FilterPhases()
# obj.create_json()
import pandas as pd

class FilterTherapeuticArea:

    def __init__(self):
        self.df = pd.read_csv('../final_clean_data.csv')

    def create_json(self):
        result = self.df.groupby(['Therapeutic Area', 'Disease'])["Trial ID"].count()

        # This will create a dictionary of the form
        # {('Therapeutic Area', 'Indication1'): count1,
        #   ('Therapeutic Area', 'Indication2'): count2, ... }
        result = result.to_dict()


        # Creating a new nested dictionary
        # { Therapeutic Area: { Indication1: count1, Indication2: count2 }, ... }
        therapeutic_indication_dict: dict[str, dict[str: int]] = {}
        for key in result:
            if key[0] not in therapeutic_indication_dict:
                therapeutic_indication_dict[key[0]] = {}

            therapeutic_indication_dict[key[0]][key[1]] = result[key]

        return therapeutic_indication_dict

# obj = FilterTherapeuticArea()
# obj.create_json()
from typing import List

import pandas as pd

class FilterSponsor:

    def __init__(self):
        self.df = pd.read_csv('./final_clean_data.csv')

        self.sponsor_list: List[int] = []
        self.sponsor_count: dict[str, int] = {}

    def create_json(self):
        for index, data in self.df.iterrows():
            self.sponsor_list = self.df["Sponsor"][index].split('\n')

            for sponsor_name in self.sponsor_list:
                if sponsor_name not in self.sponsor_count:
                    self.sponsor_count[sponsor_name] = 0

                self.sponsor_count[sponsor_name] += 1

        # Sorting the dictionary on the basis of values, in descending order
        self.sponsor_count = {k: v for (k, v) in sorted(self.sponsor_count.items(), key = lambda item: item[1], reverse=True)}

        return self.sponsor_count


# obj = FilterSponsor()
# print(obj.create_json())
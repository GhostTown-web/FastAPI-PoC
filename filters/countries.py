import pandas as pd


class FilterCountries:

    def __init__(self):
        self.df = pd.read_csv('./final_clean_data.csv')
        self.country_count: dict[str, int] = {}


    def create_json(self):

        for index, data in self.df.iterrows():
            countries_list = self.df['Countries'][index].replace(',', ';').split(';')

            # Stripping the country names of left spaces to make them unique
            # for a hashmap, so it will not consider " India" and "India" different
            for i in range(len(countries_list)):
                countries_list[i] = countries_list[i].lstrip()


            # Storing unique countries in the hashmap
            for country in countries_list:
                if country in self.country_count:
                    self.country_count[country] += 1
                else:
                    self.country_count[country] = 1


        # Sorting the dictionary on the basis of values in descending order
        self.country_count = {k: v for (k, v) in sorted(self.country_count.items(), key=lambda item: item[1], reverse=True)}

        return self.country_count

# obj = FilterCountries()
# obj.create_json()
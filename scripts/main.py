import os
from expconfig.locconfig import locconfig
from melhousing.classes import housingdata as hd
import random

from expconfig.locconfig import locconfig
# alternatively, use importlib.resources to read locconfig.json file
# using importlib will import the module as usual, hence module's __init__.py is run
# with importlib.resources.open_text("configfiles", "locconfig.json") as file:
    # locconfig = json.load(file) 

# configure input/output locations
inputfile = os.path.join(locconfig['raw']['dir'], locconfig['raw']['file'])
outputfile = os.path.join(locconfig['processed']['dir'], locconfig['processed']['file'])

# create HousingData object
def make_housing_data():
    housing_data = hd.HousingData(inputfile)
    return housing_data

def make_random_row_number():
    housing_data = make_housing_data()
    rownumber = random.randint(0, housing_data._number_of_listings)
    return rownumber

def main(rownumber: int):
    print('-'*50)
    print('location configuration:')
    print(locconfig)
    print('-'*50)
    print('csv file read from:')
    print(inputfile)
    print('-'*50)
    housing_data = make_housing_data()
    print(type(housing_data))
    print(type(housing_data._listing_list[rownumber]))
    print('-'*50)
    print('number of Listing objects inside HousingData class:')
    print(housing_data._number_of_listings)
    print('random listing object index:')
    print(rownumber)
    print('-'*50)
    print(f'listing object index {rownumber} details:')
    print(housing_data._listing_list[rownumber])
    print('-'*50)
    print('corresponding dataframe details:')
    print(housing_data._listing_dataframe.iloc[rownumber])

if __name__ == "__main__":
    main(make_random_row_number()) 
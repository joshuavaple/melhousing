# import melhousing
import os
from melhousing.classes import housingdata as hd
from configfiles.locconfig import locconfig

inputfile = os.path.join(locconfig['raw']['dir'], locconfig['raw']['file'])
outputfile = os.path.join(locconfig['processed']['dir'], locconfig['processed']['file'])
def make_housing_data():
    housing_data = hd.HousingData(inputfile)
    return housing_data

if __name__ == "__main__":
    print('-'*20)
    print('location configuration:')
    print(locconfig)
    print('-'*20)
    print('csv file read from:')
    print(inputfile)
    print('-'*20)
    housing_data = make_housing_data()
    print(type(housing_data))
    print(type(housing_data._listing_list[0]))
    print('first listing object details')
    print(housing_data._listing_list[0])

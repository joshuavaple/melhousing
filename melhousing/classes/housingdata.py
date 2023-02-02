import pandas as pd
import os
import pathlib
import sys

def say_hello():
    return 'housingdata says hello!'

class Listings(object): # each row is an object, created by
    def __init__(self, attribute_list, value_list):
        self._attribute_list = attribute_list # column headers = keys
        self._object = dict(zip(attribute_list, value_list)) # key value pairs = main data structure to store object data
    def get_value_of_attribute(self, attribute=None): # handling wrong/empty input
        if attribute not in self._attribute_list:
            return None
        return self._object[attribute]
    def __str__(self): # str method for printing
        return "\n".join([f"{attribute}: {value}" for attribute, value in self._object.items()])


class HousingData(object):
    def __init__(self, csv_data_table_path: str):
        self._listing_dataframe = self.__create_listing_dataframe(
            csv_data_table_path = csv_data_table_path
        )
        self.__generate_listing_objects(listing_dataframe = self._listing_dataframe)
        # method to return number of listings
        self._number_of_listings = len(self._listing_list)
    
    def __create_listing_dataframe(self, csv_data_table_path):
        return pd.read_csv(csv_data_table_path)
    
    def __generate_listing_objects(self, listing_dataframe):
        self._listing_list = list()
        listing_attribute_list = list(listing_dataframe.columns)
        for row in listing_dataframe.values:  # for each ndarray of object
            listing_value_list = row.tolist()  # convert it to a list of mixed types
            # create listing object for each record
            listing = Listings(
                attribute_list = listing_attribute_list, value_list = listing_value_list)
            self._listing_list.append(listing)



if __name__ == '__main__':
    say_hello()

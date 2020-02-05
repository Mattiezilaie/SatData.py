# Author: Mahtab Zilaie
# Date: January 2 2020
# Description: reads data from a Json file and then writes data into a csv file

import json


class SatData:
    """class SatData with an init method and save_as_csv method"""

    def __init__(self):

        """ method opens json file and reads from json file. goes through index 8-13 and
        gets titles from json file"""

        with open('sat.json', 'r') as infile:
            self.restored_list = json.load(infile)  # reads json file

            self.data = self.restored_list["data"]

            self.header = []  # sets header to list
        for i in range(8, 14):  # goes through index 8 -13
            self.header.append(self.restored_list['meta']['view']['columns'][i]['name'])  # gets title info from indices

    def save_as_csv(self, list_of_DBNs):

        """adds header information to csv file and sorts list of DBNs. compares user input
        DBNs to DBNs in json file. Then takes index 8-13 and adds the context from those indices to
        the csv file"""

        csvFile = open("output.csv", 'w')  # opens Csv file to write in
        csvFile.write(','.join(self.header))  # writes headers in csv file
        csvFile.write('\n')  # line break

        list_of_DBNs.sort()  # sorts list of DBNs

        for dbn in list_of_DBNs:  # iterates through list of DBNs
            for row in self.data:
                if dbn == row[8]:  # if DBN is equal to list of DBNs in json file
                    csvFile.write(','.join(row[8:14]))  # write info from indices 8-13
                    csvFile.write('\n')  # line break
                    break
        csvFile.close()
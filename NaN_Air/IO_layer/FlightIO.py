import csv
import sys
FILENAME = 'DataFiles/flightRoutes.csv'


class FlightRoute():

    def __init__(self):
        # self.get_flight_route_from_file()
        pass

    def get_flight_route_from_file(self):
        """Get flight routes from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList
        return self.__dictList

    def write_flight_route_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            newList = []
            newList.append(orderedDict['flight route id'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['flight route id'
                        ,'country'
                        ,'airport'
                        ,'flight distance'
                        ,'travel time'
                        ,'emergency contact'
                        ,'emergency number']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in self.__dictList:
                writer.writerow(dictionary)

    def getHighestID(self):
        """This method is only used by 'add_dict_to_list'.
        Returns the next id that is to be assigned."""
        highestID = 0
        for dictionary in self.__dictList:
            for key, value in dictionary.items():
                if key == "flight route id":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def convert_to_dict_with_id(self, aList):
        """Function converts list to dict, generates an ID
        and assigns it to the dictionary"""
        orderedDict, newId = {}, self.getHighestID()
        orderedDict['flight route id'] = newId
        orderedDict['country'] = aList[0]
        orderedDict['airport'] = aList[1]
        orderedDict['flight distance'] = aList[2]
        orderedDict['travel time'] = aList[3]
        orderedDict['emergency contact'] = aList[4]
        orderedDict['emergency number'] = aList[5]
        return orderedDict

    def convert_to_dict_no_id(self, aList):
        """Function converts list to dict but doesn't
        generate an id since ID should be provided in argument list"""
        orderedDict = {}
        orderedDict['flight route id'] = aList[0]
        orderedDict['country'] = aList[1]
        orderedDict['airport'] = aList[2]
        orderedDict['flight distance'] = aList[3]
        orderedDict['travel time'] = aList[4]
        orderedDict['emergency contact'] = aList[5]
        orderedDict['emergency number'] = aList[6]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'flight route id':
                    print("We here bro")
                    if value == aList[0]:
                        print('key found')
                        self.__dictList[index][aList[1]] = aList[2]
                        print(self.__dictList)
                        self.write_dictList_to_file()

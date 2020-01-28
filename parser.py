#Python code to illustrate parsing of XML files
#importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom


def parseXML():


    tree = ET.parse('test.xml')
    root = tree.getroot()

    csvfile = "NBA.csv"
    with open(csvfile, "a") as fp:
        filewriter = csv.writer(fp, dialect='excel')

        #for child in root:
            #filewriter.writerow([child.tag, child.attrib])

        for team in root.findall('team'):
            name = team.get('name')
            player = team.find('player').text

            filewriter.writerow([name, player])



    parTree = ET.parse('param_deploy.xml')
    parRoot = tree.getroot()

    csvfile = "deploy.csv"
    with open(csvfile, "a") as fp:
        filewriter = csv.writer(fp, dialect='excel')

        #for child in root:
            #filewriter.writerow([child.tag, child.attrib])

        for team in root.findall('team'):
            name = team.get('name')
            player = team.find('player').text

            filewriter.writerow([name, player])



    #mydoc = minidom.parse('test.xml')

    #teams = mydoc.getElementsByTagName('team')
    #players = mydoc.getElementsByTagName('player')


    #for elem in teams:
        #print(elem.attributes['name'].value)

    #for i in players:
        #print(i.firstChild.data)

    #csvfile = "NBA.csv"
    #with open(csvfile, "a") as fp:
        #filewriter = csv.writer(fp, dialect='excel')

        #for i in players:
            #filewriter.writerow([i.firstChild.data])

        #for elem in teams:
            #filewriter.writerow([elem.attributes['name'].value])


def main():

    # parse xml file
    parseXML()

    # store news items in a csv file
    #savetoCSV(nbaTeams, 'players.csv')


if __name__ == "__main__":

    main()

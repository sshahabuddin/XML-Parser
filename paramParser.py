#Python code to illustrate parsing of XML files
#importing the required modules
import csv
import requests
import struct
import xml.etree.ElementTree as ET
#def parseXML():
#    tree = ET.parse('param_deploy.xml')
#    root = tree.getroot()

#    csvfile = "param.csv"
#    with open(csvfile, "a") as fp:
#        filewriter = csv.writer(fp, dialect='excel')

        #header
#        for headers in root.findall('header'):
#            project = headers.find('project').text

#            print project
#            filewriter.writerow([project])

#            for verisons in headers.findall('version'):
#                ver_id = verisons.get('ver_id')
#                schema_version_id = verisons.get('schema_version_id')

#                print ver_id, schema_version_id
#                filewriter.writerow([ver_id, schema_version_id])

        #enum_definitions
#        for enum_definitions in root.findall('enum_definitions'):
#            name = enum_definitions.find('enum_table').get('name')

#            print name

#
#            for enum_tables in enum_definitions.findall('enum_table'):
#                for values in enum_tables.findall('value'):
#                    symbol = values.get('symbol')
#                    numeric = value.get('numeric')
#
#                    print symbol, numeric

        #param
#        for params in root.findall('param'):
#            param_name = params.get('param_name')
#            op_cat =  params.get('op_cat')
#            fsw_module = params.get('fsw_module')
#            modify_method = params.get('modify_method')
#            cmd_stem =  params.get('cmd_stem')
#            telem_type =  params.get('telem_type')
#            associated_telem =  params.get('associated_telem')
#            rationale =  params.get('rationale')

#            sysdesc = params.find('sysdesc').text
#            default_value = params.find('default_value').text

#            print param_name, op_cat, fsw_module, modify_method, cmd_stem, telem_type, associated_telem, rationale
#            filewriter.writerow([param_name, op_cat, fsw_module, modify_method, cmd_stem, telem_type, associated_telem, rationale])
#
#            print sysdesc, default_value
#            filewriter.writerow([sysdesc, default_value])
#
#            for parameter_types in params.findall('parameter_type'):
#                enum_param = parameter_types.find('enum_param').text
#
#                print enum_param
#                filewriter.writerow([enum_param])
#
#    return;
def parseBin():

    tree = ET.parse('param_deploy.xml')
    root = tree.getroot()

    hex = 16
    dec = 10

    fstream = open('paramDeploy.bin', 'wb')

    paramHead = struct.pack('i', int("5EE0CF60", hex))
    paramVer = struct.pack('i', 3)
    paramSys = struct.pack('i', 2)
    enumSym = []
    enumNum = []
    paramIndex = 0



    #fstream.write(paramHead)
    fstream.write(paramVer)
    fstream.write(paramSys)


    for enums in root.findall('enum_definitions/enum_table/values/enum'):
        symbol = enums.get('symbol')
        numeric = enums.get('numeric')

        if (numeric not in enumNum):
            enumSym.append(symbol)
            enumNum.append(numeric)


    for params in root.findall('param'):
        fstream.write(struct.pack('b', paramIndex))

        defaultValue = params.find('default_value').text

        i = 0
        while i < len(enumSym):
            if(enumSym[i] == defaultValue):
                fstream.write(struct.pack('b', int(enumNum[i])))
                paramIndex += 1
            i += 1

    fstream.close()

    return;


def main():
    # parse xml file
    #parseXML()
    parseBin()



if __name__ == "__main__":
    main()

import xml.etree.ElementTree as ET
import sys

def check_xml_for_string(xml_file, search_string):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Check if the search string is present in the XML content
        if search_string in ET.tostring(root).decode():
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred:", e)
        return False

# Path to the XML file
xml_file_path = "alu/results.xml"

# String to search for in the XML file
search_string = "Test failed"

# Check if the string is present in the XML file
if check_xml_for_string(xml_file_path, search_string):
    print(f"The string '{search_string}' is present in the XML file.")
    sys.exit(1)
else:
    print(f"The string '{search_string}' is not present in the XML file.")
    sys.exit(0)
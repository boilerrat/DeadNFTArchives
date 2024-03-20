import xml.etree.ElementTree as ET
import json

def parse_xml_to_json(xml_content):
    root = ET.fromstring(xml_content)
    
    # Extract album metadata
    album_metadata = {
        "identifier": root.find("identifier").text,
        "uploader": root.find("uploader").text,
        "date_added": root.find("addeddate").text,
        "concert_date": root.find("date").text,
        "title": root.find("title").text,
        "creator": root.find("creator").text,
        "mediatype": root.find("mediatype").text,
        "collection": [collection.text for collection in root.findall("collection")],
        "venue": root.find("venue").text,
        "location": root.find("coverage").text,
        "source": root.find("source").text,
        "description": root.find("description").text
    }

    # Extract files metadata
    files_metadata = []
    for file in root.findall("./file"):
        file_data = {
            "name": file.get("name"),
            "format": file.find("format").text if file.find("format") is not None else None,
            "length": file.find("length").text if file.find("length") is not None else None,
            "title": file.find("title").text if file.find("title") is not None else None,
            "size": file.find("size").text if file.find("size") is not None else None,
            "md5": file.find("md5").text if file.find("md5") is not None else None,
            "track": file.find("track").text if file.find("track") is not None else None,
            "creator": file.find("creator").text if file.find("creator") is not None else None,
            "album": file.find("album").text if file.find("album") is not None else None
        }
        files_metadata.append(file_data)

    # Combine metadata into one dictionary
    combined_metadata = {
        "album_metadata": album_metadata,
        "files_metadata": files_metadata
    }

    # Convert dictionary to JSON
    return json.dumps(combined_metadata, indent=4)

def process_xml_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    json_output = parse_xml_to_json(xml_content)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(json_output)

# Specify the path to your input XML file and the desired output JSON file path
input_file_path = 'your_input_file_path_here.xml'
output_file_path = 'your_output_file_path_here.json'

# Call the function to process the XML and output JSON
process_xml_file(input_file_path, output_file_path)

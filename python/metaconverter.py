import xml.etree.ElementTree as ET
import json
import os
from pathlib import Path

def parse_xml_to_json(xml_content):
    # Placeholder for your XML parsing logic
    root = ET.fromstring(xml_content)
    metadata = {"example": "Adjust this logic to parse your XML structure."}
    return json.dumps(metadata, indent=4)

def find_xml_file(show_directory, filename):
    # Check for a specific XML file in the show directory
    xml_file_path = os.path.join(show_directory, filename)
    if os.path.exists(xml_file_path):
        return xml_file_path
    return None

def process_show(show_date, project_directory):
    # Adjusted to match your directory structure without adding '19'
    year = show_date[:2]  # Extracting '81' from '81-03-05'
    show_directory = Path(project_directory) / year / f'GD{show_date}'
    json_directory = Path(project_directory) / "json"
    json_directory.mkdir(exist_ok=True)  # Ensure json directory exists

    meta_xml_path = find_xml_file(show_directory, 'meta.xml')
    if not meta_xml_path:
        print(f"Missing meta.xml for show GD{show_date}. Check directory and filename.")
        return

    with open(meta_xml_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    json_output = parse_xml_to_json(xml_content)

    output_file_path = json_directory / f'GD{show_date}.json'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(json_output)
    print(f"Processed and saved JSON for GD{show_date}.")

# Example usage
project_directory = '/media/boilerrat/Jerry/DeadNFTArchives'
show_date = '81-03-05'
process_show(show_date, project_directory)

import xml.etree.ElementTree as ET
import json
import os
from pathlib import Path

def parse_xml_to_json(xml_content):
    # Your existing XML parsing logic...
    # Returns json.dumps(combined_metadata, indent=4)

def find_xml_file(show_directory):
    # Assuming there's only one XML file per show directory
    for file in os.listdir(show_directory):
        if file.endswith('.xml'):
            return os.path.join(show_directory, file)
    return None

def process_show(show_date, project_directory):
    # Constructing directory paths
    year = "19" + show_date[2:4]  # Assuming all shows are in the 1900s
    show_directory = Path(project_directory) / year / f'GD{show_date}'
    json_directory = Path(project_directory) / "json"
    json_directory.mkdir(exist_ok=True)  # Ensure json directory exists
    
    xml_file_path = find_xml_file(show_directory)
    if not xml_file_path:
        print(f"No XML file found for show GD{show_date}.")
        return

    # Processing XML to JSON
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    json_output = parse_xml_to_json(xml_content)

    # Saving JSON output
    output_file_path = json_directory / f'GD{show_date}.json'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(json_output)
    print(f"Processed and saved JSON for GD{show_date}.")

# Example usage
project_directory = '/path/to/DeadNFTArchives'
show_date = '81-03-05'  # Example show date
process_show(show_date, project_directory)

import requests
import gzip

# URL of the XML file
url = "https://raw.githubusercontent.com/buhtigd1/EPG2/main/epg.xml"

# Output file names
xml_file = "epg.xml"
gz_file = "epg.xml.gz"

# Replacement mapping for channel IDs
channel_replacements = {
    '<channel id="TNTSports1.uk@HD">': '<channel id="TNT 1 - AQ">',
    '<channel id="TNTSports2.uk@HD">': '<channel id="TNT 2 - AQ">',
    '<channel id="TNTSports3.uk@HD">': '<channel id="TNT 3 - AQ">',
    '<channel id="TNTSports4.uk@HD">': '<channel id="TNT 4 - AQ">',
}

# Replacement mapping for programme channel attributes
programme_replacements = {
    'channel="TNTSports1.uk@HD"': 'channel="TNT 1 - AQ"',
    'channel="TNTSports2.uk@HD"': 'channel="TNT 2 - AQ"',
    'channel="TNTSports3.uk@HD"': 'channel="TNT 3 - AQ"',
    'channel="TNTSports4.uk@HD"': 'channel="TNT 4 - AQ"',
}

def download_and_compress():
    # Download the XML content
    response = requests.get(url)
    response.raise_for_status()
    xml_content = response.text  # decode as text for replacements

    # Perform channel replacements
    for old, new in channel_replacements.items():
        xml_content = xml_content.replace(old, new)

    # Perform programme replacements
    for old, new in programme_replacements.items():
        xml_content = xml_content.replace(old, new)

    # Save updated epg.xml
    with open(xml_file, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"Updated {xml_file}")

    # Save compressed epg.xml.gz
    with gzip.open(gz_file, "wb") as f:
        f.write(xml_content.encode("utf-8"))
    print(f"Saved {gz_file}")

if __name__ == "__main__":
    download_and_compress()

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
    '<channel id="TNTLatinAmerica.us@Mexico">': '<channel id="TNT MX - AQ">',
    '<channel id="Willow.us@SD">': '<channel id="WILLOW - AQ">',
    '<channel id="beINSports1.qa@MENA">': '<channel id="beIN Sports 1 - AQ">',
    '<channel id="beINSports2.qa@MENA">': '<channel id="beIN Sports 2 - AQ">',
    '<channel id="beINSports3.qa@MENA">': '<channel id="beIN Sports 3 - AQ">',
    '<channel id="8C1EC4FC-35E6-4866-A75D-37FCFAE18839">': '<channel id="beIN ENGLISH 1">',
    '<channel id="beINSports1.qa@Australia">': '<channel id="beIN Sports 1 AU - AQ">',
    '<channel id="beINSports2.qa@Australia">': '<channel id="beIN Sports 2 AU - AQ">',
    '<channel id="C938A2D0-375A-4876-B05D-08EE29D33B07">': '<channel id="beIN Sports Xtra">',
}

# Replacement mapping for programme channel attributes
programme_replacements = {
    'channel="TNTSports1.uk@HD"': 'channel="TNT 1 - AQ"',
    'channel="TNTSports2.uk@HD"': 'channel="TNT 2 - AQ"',
    'channel="TNTSports3.uk@HD"': 'channel="TNT 3 - AQ"',
    'channel="TNTSports4.uk@HD"': 'channel="TNT 4 - AQ"',
    'channel="TNTLatinAmerica.us@Mexico"': 'channel="TNT MX - AQ"',
    'channel="Willow.us@SD"': 'channel="WILLOW - AQ"',
    'channel="beINSports1.qa@MENA"': 'channel="beIN Sports 1 - AQ"',
    'channel="beINSports2.qa@MENA"': 'channel="beIN Sports 2 - AQ"',
    'channel="beINSports3.qa@MENA"': 'channel="beIN Sports 3 - AQ"',
    'channel="8C1EC4FC-35E6-4866-A75D-37FCFAE18839"': 'channel="beIN ENGLISH 1"',
    'channel="beINSports1.qa@Australia"': 'channel="beIN Sports 1 AU - AQ"',
    'channel="beINSports2.qa@Australia"': 'channel="beIN Sports 2 AU - AQ"',
    'channel="C938A2D0-375A-4876-B05D-08EE29D33B07"': 'channel="beIN Sports Xtra"',

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

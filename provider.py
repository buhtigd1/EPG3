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
    '<channel id="US1#Willow.Cricket.HDTV.(WILLOWHD).us">': '<channel id="WILLOW - AQ">',
    '<channel id="beINSports1.qa@MENA">': '<channel id="beIN Sports 1 - AQ">',
    '<channel id="beINSports2.qa@MENA">': '<channel id="beIN Sports 2 - AQ">',
    '<channel id="beINSports3.qa@MENA">': '<channel id="beIN Sports 3 - AQ">',
    '<channel id="8C1EC4FC-35E6-4866-A75D-37FCFAE18839">': '<channel id="beIN ENGLISH 1">',
    '<channel id="beINSports1.qa@Australia">': '<channel id="beIN Sports 1 AU - AQ">',
    '<channel id="beINSports2.qa@Australia">': '<channel id="beIN Sports 2 AU - AQ">',
    '<channel id="C938A2D0-375A-4876-B05D-08EE29D33B07">': '<channel id="beIN Sports Xtra">',
    '<channel id="1vi4p39obt24i1dtsmthi921tl">': '<channel id="DAZN Fast - AQ">',
    '<channel id="1xx7lone8fvv21a2rpc5cji3jx">': '<channel id="DAZN RISE - AQ">',
    '<channel id="us#ta9r7upeuzb1koxdxu1g5br3">': '<channel id="Fubo 1">',
    '<channel id="TSN1.ca@SD">': '<channel id="TSN AQ1">',
    '<channel id="TSN2.ca@SD">': '<channel id="TSN AQ2">',
    '<channel id="TSN3.ca@SD">': '<channel id="TSN AQ3">',
    '<channel id="TSN4.ca@SD">': '<channel id="TSN AQ4">',
    '<channel id="TSN5.ca@SD">': '<channel id="TSN AQ5">',
    '<channel id="PremierSports1.ie@HD">': '<channel id="PREMIER SPORTS 1 - AQ">',
    '<channel id="PremierSports2.ie@HD">': '<channel id="PREMIER SPORTS 2 - AQ">',
}

# Replacement mapping for programme channel attributes
programme_replacements = {
    'channel="TNTSports1.uk@HD"': 'channel="TNT 1 - AQ"',
    'channel="TNTSports2.uk@HD"': 'channel="TNT 2 - AQ"',
    'channel="TNTSports3.uk@HD"': 'channel="TNT 3 - AQ"',
    'channel="TNTSports4.uk@HD"': 'channel="TNT 4 - AQ"',
    'channel="TNTLatinAmerica.us@Mexico"': 'channel="TNT MX - AQ"',
    'channel="US1#Willow.Cricket.HDTV.(WILLOWHD).us"': 'channel="WILLOW - AQ"',
    'channel="beINSports1.qa@MENA"': 'channel="beIN Sports 1 - AQ"',
    'channel="beINSports2.qa@MENA"': 'channel="beIN Sports 2 - AQ"',
    'channel="beINSports3.qa@MENA"': 'channel="beIN Sports 3 - AQ"',
    'channel="8C1EC4FC-35E6-4866-A75D-37FCFAE18839"': 'channel="beIN ENGLISH 1"',
    'channel="beINSports1.qa@Australia"': 'channel="beIN Sports 1 AU - AQ"',
    'channel="beINSports2.qa@Australia"': 'channel="beIN Sports 2 AU - AQ"',
    'channel="C938A2D0-375A-4876-B05D-08EE29D33B07"': 'channel="beIN Sports Xtra"',
    'channel="1vi4p39obt24i1dtsmthi921tl"': 'channel="DAZN Fast - AQ"',
    'channel="1xx7lone8fvv21a2rpc5cji3jx"': 'channel="DAZN RISE - AQ"',
    'channel="us#ta9r7upeuzb1koxdxu1g5br3"': 'channel="Fubo 1"',
    'channel="TSN1.ca@SD"': 'channel="TSN AQ1"',
    'channel="TSN2.ca@SD"': 'channel="TSN AQ2"',
    'channel="TSN3.ca@SD"': 'channel="TSN AQ3"',
    'channel="TSN4.ca@SD"': 'channel="TSN AQ4"',
    'channel="TSN5.ca@SD"': 'channel="TSN AQ5"',
    'channel="PremierSports1.ie@HD"': 'channel="PREMIER SPORTS 1 - AQ"',
    'channel="PremierSports2.ie@HD"': 'channel="PREMIER SPORTS 2 - AQ"',
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

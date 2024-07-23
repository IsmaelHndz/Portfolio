import xml.etree.ElementTree as ET

def timestamps_by_description(xml, description):
    root = ET.fromstring(xml)
    timestamps = []

    for event in root.findall('event'):
        d = event.find('description').text.strip().lower()
        if d == description.strip().lower():
            timestamps.append(int(event.get('timestamp')))

    return timestamps

xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <event timestamp="1614285589">
        <description>Intrusion detected</description>
    </event>
    <event timestamp="1614286432">
        <description>Intrusion ended</description>
    </event>
</log>"""
print(timestamps_by_description(xml, 'Intrusion ended'))

# Icon url https://kml4earth.appspot.com/icons.html

import pandas as pd
import numpy as np
import time
import os

filename = "merge.txt"
kmlfile = "merge3d.kml"

# Readout data every 1 sec (mock of the instrument)
def mock_dataread(filename):
    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline() 

        for line in f:
            line = line.strip()
            if not line:
                continue

            yield line
            
            time.sleep(1)

colors = ["ff0000ff", "ff00ffff", "ff00ff00", "ff00ff00", "ff0000ff"]

def init_kml_5step(filename="merge2.kml"):
    tmp = filename + ".tmp"

    styles = """
<Style id="CH4_1C2H6_1"><IconStyle><color>ff0000ff</color><scale>0.2</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_1C2H6_2"><IconStyle><color>ff00ffff</color><scale>0.2</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_1C2H6_3"><IconStyle><color>ff00ff00</color><scale>0.2</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_1C2H6_4"><IconStyle><color>ff00ffff</color><scale>0.2</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_1C2H6_5"><IconStyle><color>ff0000ff</color><scale>0.2</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>

<Style id="CH4_2C2H6_1"><IconStyle><color>ff0000ff</color><scale>0.4</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_2C2H6_2"><IconStyle><color>ff00ffff</color><scale>0.4</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_2C2H6_3"><IconStyle><color>ff00ff00</color><scale>0.4</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_2C2H6_4"><IconStyle><color>ff00ffff</color><scale>0.4</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_2C2H6_5"><IconStyle><color>ff0000ff</color><scale>0.4</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>

<Style id="CH4_3C2H6_1"><IconStyle><color>ff0000ff</color><scale>0.6</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_3C2H6_2"><IconStyle><color>ff00ffff</color><scale>0.6</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_3C2H6_3"><IconStyle><color>ff00ff00</color><scale>0.6</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_3C2H6_4"><IconStyle><color>ff00ffff</color><scale>0.6</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_3C2H6_5"><IconStyle><color>ff0000ff</color><scale>0.6</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>

<Style id="CH4_4C2H6_1"><IconStyle><color>ff0000ff</color><scale>0.8</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_4C2H6_2"><IconStyle><color>ff00ffff</color><scale>0.8</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_4C2H6_3"><IconStyle><color>ff00ff00</color><scale>0.8</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_4C2H6_4"><IconStyle><color>ff00ffff</color><scale>0.8</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_4C2H6_5"><IconStyle><color>ff0000ff</color><scale>0.8</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>

<Style id="CH4_5C2H6_1"><IconStyle><color>ff0000ff</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_5C2H6_2"><IconStyle><color>ff00ffff</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_5C2H6_3"><IconStyle><color>ff00ff00</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_5C2H6_4"><IconStyle><color>ff00ffff</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
<Style id="CH4_5C2H6_5"><IconStyle><color>ff0000ff</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href></Icon></IconStyle><LabelStyle><scale>0</scale></LabelStyle></Style>
"""

    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
<name>Realtime Track</name>
{styles}
<Folder>
<!-- INSERT_HERE -->
</Folder>
</Document>
</kml>
"""
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)

    os.replace(tmp, filename)


def ch4_to_step(ch4, vmin=1.9, vmax=2.1):
    steps = 5
    step = int((ch4 - vmin) / (vmax - vmin) * steps) + 1
    step = max(1, min(5, step))  
    return step

def c2h6_to_step(c2h6, vmin= -1.8, vmax = 1.8):
    steps = 5
    step = int((c2h6 - vmin) / (vmax - vmin) * steps) + 1
    step = max(1, min(5, step))  
    return step

def add_point_5step(lat, lon, name, ch4, c2h6, alt,  filename="merge2.kml"):
    ch4_step = ch4_to_step(ch4)
    c2h6_step = c2h6_to_step(c2h6)
    style_id = f"CH4_{ch4_step}C2H6_{c2h6_step}"

    tmp = filename + ".tmp"

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    placemark = f"""
<Placemark>
  <name>{name}</name>
  <styleUrl>#{style_id}</styleUrl>
  <Point>
  <extrude>1</extrude>
    <altitudeMode>relativeToGround</altitudeMode>
    <coordinates>{lon},{lat},{alt}</coordinates>
  </Point>
</Placemark>
"""

    new_text = text.replace(
        "<!-- INSERT_HERE -->",
        placemark + "\n<!-- INSERT_HERE -->"
    )

    with open(tmp, "w", encoding="utf-8") as f:
        f.write(new_text)

    os.replace(tmp, filename)


# == Main ====
init_kml_5step(kmlfile)

for line in mock_dataread(filename):
    print(line)
    cols = line.split(",")
    time_utc = cols[0]
    lat = float(cols[2])
    lon = float(cols[3])
    ch4 = float(cols[9])
    c2h6 = float(cols[12])
    alt = float(cols[4])

    add_point_5step(lat, lon, time_utc, ch4, c2h6, alt,  kmlfile)

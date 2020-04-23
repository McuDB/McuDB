import os
import datetime

from tomlkit import comment
from tomlkit import document
from tomlkit import nl
from tomlkit import table
from tomlkit import integer as toml_int
from tomlkit.toml_file import TOMLFile
from xml.etree.ElementTree import parse as parse_xml

from lib import toml_file_header

xml_file = os.path.join(
    os.path.dirname(__file__), "..", "srcdata", "stm32_db", "mcu", "families.xml"
)
xml_tree = parse_xml(xml_file)
xml_root = xml_tree.getroot()

toml_file = os.path.join(
    os.path.dirname(__file__), "..", "data", "mcu_families", "stm.toml"
)
toml = TOMLFile(toml_file)

doc = document()

toml_file_header(doc)

for xml_family in xml_root.findall("./Family"):
    family = table()
    family.add("name", xml_family.get("Name"))
    family.add("object_type", "family")
    for xml_subfamily in xml_family.findall("./SubFamily"):
        subfamily = table()
        subfamily.add("name", xml_subfamily.get("Name"))
        subfamily.add("object_type", "subfamily")
        for xml_mcu in xml_subfamily.findall("./Mcu"):
            mcu = table()
            mcu.add("name", xml_mcu.get("RefName"))
            mcu.add("object_type", "mcu")
            mcu.add("package", xml_mcu.get("PackageName"))
            if xml_mcu.findtext("./Core"):
                mcu.add("core", xml_mcu.findtext("./Core"))
            if xml_mcu.findtext("./Frequency"):
                mcu.add("max_frequency", toml_int(xml_mcu.findtext("./Frequency")))
            if xml_mcu.findtext("./Ram"):
                mcu.add("ram", toml_int(xml_mcu.findtext("./Ram")))
            if xml_mcu.findtext("./IONb"):
                mcu.add("io_count", toml_int(xml_mcu.findtext("./IONb")))
            if xml_mcu.findtext("./Flash"):
                mcu.add("flash", toml_int(xml_mcu.findtext("./Flash")))
            subfamily.add(xml_mcu.get("RefName"), mcu)
        family.add(xml_subfamily.get("Name"), subfamily)
    doc.add(xml_family.get("Name"), family)

toml.write(doc)

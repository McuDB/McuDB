import os
import datetime

from tomlkit import comment
from tomlkit import document
from tomlkit import nl
from tomlkit import table
from tomlkit import integer as toml_int
from tomlkit import boolean as toml_boolean
from tomlkit.toml_file import TOMLFile
from pathlib import Path
from lxml import etree

from lib import toml_file_header

src_dir = os.path.join(os.path.dirname(__file__), "..", "srcdata", "stm32_db", "mcu")

pathlist = Path(src_dir).glob("STM32*.xml")
for path in pathlist:
    xml_tree = etree.parse(str(path))
    xml_root = xml_tree.getroot()

    toml_file = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "mcu",
        "stm",
        path.stem.lower() + ".toml",
    )
    toml = TOMLFile(toml_file)

    doc = document()

    toml_file_header(doc)

    doc.add(nl())

    doc.add("name", xml_root.get("RefName"))
    doc.add("object_type", "mcu")
    if xml_root.get("Package"):
        doc.add("package", xml_root.get("Package"))
    if xml_root.get("Family"):
        doc.add("family", xml_root.get("Family"))
    if xml_root.get("Line"):
        doc.add("line", xml_root.get("Line"))
    if xml_root.get("HasPowerPad"):
        doc.add("has_power_pad", toml_boolean(xml_root.get("HasPowerPad")))
    if xml_root.findtext("Core", None, xml_root.nsmap):
        doc.add("core", xml_root.findtext("./Core", None, xml_root.nsmap))
    if xml_root.findtext("Frequency", None, xml_root.nsmap):
        doc.add(
            "max_frequency",
            toml_int(xml_root.findtext("Frequency", None, xml_root.nsmap)),
        )
    if xml_root.findtext("Ram", None, xml_root.nsmap):
        doc.add("ram", toml_int(xml_root.findtext("Ram", None, xml_root.nsmap)))
    if xml_root.findtext("IONb", None, xml_root.nsmap):
        doc.add("io_count", toml_int(xml_root.findtext("IONb", None, xml_root.nsmap)))
    if xml_root.findtext("Flash", None, xml_root.nsmap):
        doc.add("flash", toml_int(xml_root.findtext("Flash", None, xml_root.nsmap)))
    toml.write(doc)

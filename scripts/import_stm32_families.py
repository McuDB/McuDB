import os
import datetime

from tomlkit import comment
from tomlkit import document
from tomlkit import nl
from tomlkit import table
from tomlkit import integer as toml_int
from tomlkit.toml_file import TOMLFile
from xml.etree.ElementTree import parse as parse_xml

xml_file = os.path.join(os.path.dirname(__file__), "..", "srcdata", "stm32_db", "mcu", "families.xml")
xml_tree = parse_xml(xml_file)
xml_root = xml_tree.getroot()

toml_file = os.path.join(os.path.dirname(__file__), "..", "data", "mcu_families", "stm.toml")
toml = TOMLFile(toml_file)

doc = document()

doc.add(comment("This file is part of the McuDB project, https://github.com/McuDB"))
doc.add(comment(""))
doc.add(comment("The MIT License (MIT)"))
doc.add(comment(""))
doc.add(comment("Copyright (c) 2020 Mark Olsson for McuDB"))
doc.add(comment(""))
doc.add(comment("Permission is hereby granted, free of charge, to any person obtaining a copy"))
doc.add(comment("of this software and associated documentation files (the \"Software\"), to deal"))
doc.add(comment("in the Software without restriction, including without limitation the rights"))
doc.add(comment("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"))
doc.add(comment("copies of the Software, and to permit persons to whom the Software is"))
doc.add(comment("furnished to do so, subject to the following conditions:"))
doc.add(comment(""))
doc.add(comment("The above copyright notice and this permission notice shall be included in"))
doc.add(comment("all copies or substantial portions of the Software."))
doc.add(comment(""))
doc.add(comment("THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR"))
doc.add(comment("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"))
doc.add(comment("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"))
doc.add(comment("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"))
doc.add(comment("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"))
doc.add(comment("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN"))
doc.add(comment("THE SOFTWARE."))

for xml_family in xml_root.findall("./Family"):
    family = table()
    family.add("name", xml_family.get("Name"))
    family.add("type", "family")
    for xml_subfamily in xml_family.findall("./SubFamily"):
        subfamily = table()
        subfamily.add("name", xml_subfamily.get("Name"))
        subfamily.add("type", "subfamily")
        for xml_mcu in xml_subfamily.findall("./Mcu"):
            mcu = table()
            mcu.add("name", xml_mcu.get("RefName"))
            mcu.add("type", "mcu")
            mcu.add("package", xml_mcu.get("PackageName"))
            if (xml_mcu.findtext("./Core")):
                mcu.add("core", xml_mcu.findtext("./Core"))
            if (xml_mcu.findtext("./Frequency")):
                mcu.add("max_frequency", toml_int(xml_mcu.findtext("./Frequency")))
            if (xml_mcu.findtext("./Ram")):
                mcu.add("ram", toml_int(xml_mcu.findtext("./Ram")))
            if (xml_mcu.findtext("./IONb")):
                mcu.add("io_count", toml_int(xml_mcu.findtext("./IONb")))
            if (xml_mcu.findtext("./Flash")):
                mcu.add("flash", toml_int(xml_mcu.findtext("./Flash")))
            subfamily.add(xml_mcu.get("RefName"), mcu)
        family.add(xml_subfamily.get("Name"), subfamily)
    doc.add(xml_family.get("Name"), family)

toml.write(doc)
from tomlkit import comment


def toml_file_header(doc):
    doc.add(comment("This file is part of the McuDB project, https://github.com/McuDB"))
    doc.add(comment(""))
    doc.add(comment("The MIT License (MIT)"))
    doc.add(comment(""))
    doc.add(comment("Copyright (c) 2020 Mark Olsson for McuDB"))
    doc.add(comment(""))
    doc.add(
        comment(
            "Permission is hereby granted, free of charge, to any person obtaining a copy"
        )
    )
    doc.add(
        comment(
            'of this software and associated documentation files (the "Software"), to deal'
        )
    )
    doc.add(
        comment(
            "in the Software without restriction, including without limitation the rights"
        )
    )
    doc.add(
        comment(
            "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"
        )
    )
    doc.add(
        comment("copies of the Software, and to permit persons to whom the Software is")
    )
    doc.add(comment("furnished to do so, subject to the following conditions:"))
    doc.add(comment(""))
    doc.add(
        comment(
            "The above copyright notice and this permission notice shall be included in"
        )
    )
    doc.add(comment("all copies or substantial portions of the Software."))
    doc.add(comment(""))
    doc.add(
        comment(
            'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR'
        )
    )
    doc.add(
        comment(
            "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"
        )
    )
    doc.add(
        comment(
            "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"
        )
    )
    doc.add(
        comment(
            "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"
        )
    )
    doc.add(
        comment(
            "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"
        )
    )
    doc.add(
        comment(
            "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN"
        )
    )
    doc.add(comment("THE SOFTWARE."))

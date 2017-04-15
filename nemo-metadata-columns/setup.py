#!/usr/bin/python3

import DistUtilsExtra.auto

data = [
    (
        '/usr/share/nemo-python/extensions',
        [
            'src/nemo-metadata-columns.py'
        ]
    )
]

DistUtilsExtra.auto.setup(
    name         = "nemo-metadata-columns",
    version      = "3.2.0",
    description  = "Nemo extension, adding columns for media metadata",
    author       = "Eduard Dopler",
    author_email = "kontakt@eduard-dopler.de",
    url          = "https://github.com/EduardDopler/nemo-extensions",
    license      = "GPL3",
    data_files   = data
)

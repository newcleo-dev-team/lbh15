import os


basepath = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(basepath, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()


__doi__ = {
    "OECD-2015_NEA.No.7268":
        {"author": "NEA",
         "title":  "Handbook on Lead-bismuth Eutectic Alloy "
                   "and Lead Properties, Materials Compatibility, "
                   "Thermal-hydraulics and Technologies",
         "ref": "2015",
         "doi": ""}
}

# zenly-html-converter

Python scripts for converting HTML files exported from Zenly, an app which recently bought by Snap and confirmed end of service to more general geocode formats. I am supporting the conversion from zenly HTML to kml format, which is used by another application Fog of World supports for imports.

The kml format is introduced by google as a simple encoding for displaying geological data: https://developers.google.com/kml/documentation


### requirements
note: I am not testing specific versions on these packages.

- python == 3.9.7
- simplekml == 1.3.6
- beautifulsoup4 == 4.10.0

### usage

Make sure you have all the dependencies, and your data in `/data` organized in the same way as specified in `/test_data`. Then you may run the following command from root to convert your data into kml files. The results are written in `/out`. Add tag `--all` to make it output one kml file.

<code> python ./script/convert_kml.py data </code>

Use the notebook under `/notebook` to test your changes, if needed.
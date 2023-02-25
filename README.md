# zenly-html-to-kml

Python scripts for converting HTML files exported from Zenly, an app which recently bought by Snap and confirmed end of service to more general geocode formats. I am supporting the conversion from zenly HTML to both kml and gpx formats, which are the two that another application Fog of World supports for imports.

The kml format is introduced by google as a simple encoding for displaying geological data: https://developers.google.com/kml/documentation

The gpx format is used by the open-source software openstreetmap to encode gps tracks: https://wiki.openstreetmap.org/wiki/GPX

### requirements
note: I am not testing specific versions on these packages.

- python == 3.9.7
- gpxpy == 1.5.0
- simplekml == 1.3.6
- beautifulsoup4 == 4.10.0

### usage

Make sure you have all the dependencies, and your data in `/data` organized in the same way as specified in `/test_data`. Then you may run the following command from root to convert your data into kml files. Replace `convert_kml` with `convert_gpx` to produce gpx data. The results are written in `/out`.

<code> python ./script/convert_kml.py data </code>

Use the notebook under `/notebook` to test your changes, if needed.
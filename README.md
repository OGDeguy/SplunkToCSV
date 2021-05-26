# Splunk To CSV

This is a simple python program for converting large chunked splunk json exports into csv files. Windows users please see the latest [release](https://github.com/OGDeguy/SplunkToCSV/releases) for a compiled version.


```batch
usage: SplunkToCSV.exe [-h] [--target TARGET] [--output OUTPUT]

███████╗██████╗ ██╗     ██╗   ██╗███╗   ██╗██╗  ██╗         ██╗       ██████╗███████╗██╗   ██╗
██╔════╝██╔══██╗██║     ██║   ██║████╗  ██║██║ ██╔╝         ╚██╗     ██╔════╝██╔════╝██║   ██║
███████╗██████╔╝██║     ██║   ██║██╔██╗ ██║█████╔╝     █████╗╚██╗    ██║     ███████╗██║   ██║
╚════██║██╔═══╝ ██║     ██║   ██║██║╚██╗██║██╔═██╗     ╚════╝██╔╝    ██║     ╚════██║╚██╗ ██╔╝
███████║██║     ███████╗╚██████╔╝██║ ╚████║██║  ██╗         ██╔╝     ╚██████╗███████║ ╚████╔╝
╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝         ╚═╝       ╚═════╝╚══════╝  ╚═══╝

© 2021 Sage Infrastructure Solutions Group Inc. All rights reserved.         
www.sageisg.com

This program will convert all of the JSON files in the target (-t) directory into the output (-o) CSV formatted file.
JSON elements with child list or dict elements will be flattened using the string representation of them.

Example Usage (Linux):
python3 SplunkToCSV.py -t splunk/export/ -o today.csv

Example Usage (Windows):
.\SplunkToCSV.exe -t splunk\export\ -o today.csv

optional arguments:
  -h, --help            show this help message and exit
  --target TARGET, -t TARGET
                        Directory where JSON files can be found
  --output OUTPUT, -o OUTPUT
                        File to output the data to. This file will be in CSV format


```
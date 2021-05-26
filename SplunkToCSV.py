import argparse
import logging
from os import listdir, getcwd
from os.path import isfile, join
from csv import writer
from json import load
from datetime import datetime
logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.DEBUG)
banner = """

███████╗██████╗ ██╗     ██╗   ██╗███╗   ██╗██╗  ██╗         ██╗       ██████╗███████╗██╗   ██╗
██╔════╝██╔══██╗██║     ██║   ██║████╗  ██║██║ ██╔╝         ╚██╗     ██╔════╝██╔════╝██║   ██║
███████╗██████╔╝██║     ██║   ██║██╔██╗ ██║█████╔╝     █████╗╚██╗    ██║     ███████╗██║   ██║
╚════██║██╔═══╝ ██║     ██║   ██║██║╚██╗██║██╔═██╗     ╚════╝██╔╝    ██║     ╚════██║╚██╗ ██╔╝
███████║██║     ███████╗╚██████╔╝██║ ╚████║██║  ██╗         ██╔╝     ╚██████╗███████║ ╚████╔╝ 
╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝         ╚═╝       ╚═════╝╚══════╝  ╚═══╝  

© 2021 Sage Infrastructure Solutions Group Inc. All rights reserved.         
www.sageisg.com                                                                                                           
"""
description = f"""
{banner}
This program will convert all of the JSON files in the target (-t) directory into the output (-o) CSV formatted file.
JSON elements with child list or dict elements will be flattened using the string representation of them.

Example Usage (Linux):
python3 SplunkToCSV.py -t splunk/export/ -o today.csv

Example Usage (Windows):
.\SplunkToCSV.exe -t splunk\export\ -o today.csv
"""
parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--target', '-t', help='Directory where JSON files can be found', default=getcwd())
parser.add_argument('--output', '-o', help="File to output the data to. This file will be in CSV format",
                    default=join(getcwd(), 'out.csv'))
args = parser.parse_args()
start = datetime.now()
print(banner)
from re import compile


def flatten_dict(item):
    """
    Flattens dictionaries so we can easily write them to the CSV file
    :param item: dict
    :return: dict
    """
    for value, key in item.items():
        if isinstance(value, list):
            item[key] = str(value)
        if isinstance(value, dict):
            item[key] = str(value)
    return item


logging.info("Indexing target files...")
target_files = listdir(args.target)
json_re = compile("\.json$")
remove_list = []
for file in target_files:
    if not isfile(join(args.target, file)):
        continue
    if not json_re.search(file):
        remove_list.append(file)
logging.info(f"Removing {len(remove_list)} non-json files from index")
for file in remove_list:
    target_files.remove(file)
files_written = 0
logging.info(f"Indexed {len(target_files)} files in target dir")
record_counter = 0
with open(args.output, 'w', newline='') as csvfile:
    csvwriter = writer(csvfile)
    keys = []
    header_written = False
    headers = []
    logging.info("Processing files...")
    current = 0
    last_progress = 0
    for file in target_files:
        if current != 0:
            progress = ((current/ len(target_files)) * 100)
            if round(progress) > last_progress:
                logging.info(f"Processing progress: {round(progress)}%    Total records written: {record_counter}")
                last_progress = round(progress)
        try:
            file = open(join(args.target,file), 'r')
            values = load(file)
            file.close()
            flattened_values = []
            for value in values:
                flattened_values.append(flatten_dict(value))
            if not header_written:
                for key, data in flattened_values[0].items():
                    headers.append(key)
                csvwriter.writerow(headers)
                header_written = True
            for value in flattened_values:
                values = []
                for key, data in value.items():
                    values.append(data)
                record_counter += 1
                csvwriter.writerow(values)
        except Exception as e:
            from traceback import print_exc
            logging.error(f"Encountered error parsing JSON: {e}")
            print_exc()
            logging.debug(f"Continuing...")
        current += 1
    finish = datetime.now()
logging.info(f"Processing complete. Total time: {finish - start}")
logging.info(f"Output file is available: {args.output}")



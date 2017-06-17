import csv
import sys
import os
import traceback
import time

if sys.version_info[0] < 3:
    import ConfigParser
else:
    import configparser as ConfigParser

# Helper function to get an exception
def get_exception():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    return repr(traceback.format_exception(exc_type, exc_value, exc_traceback))

# Main
if __name__ == "__main__":

    print("Script started")

    start_time = time.time()

    config_file_name = None
    csv_file_name1 = None
    csv_file_name2 = None
    csv_column1 = None
    csv_column2 = None

    print(sys.argv)

    # Determine the config file path
    if len(sys.argv) == 2:

        config_file_name = sys.argv[1]

        # Read the config file
        config = ConfigParser.ConfigParser()
        config.read(config_file_name)

        try:
            csv_file_name1 = config.get('Data', 'csv_file_name1')
            csv_file_name2 = config.get('Data', 'csv_file_name2')
            csv_column1 = int(config.get('Data', 'csv_column1'))
            csv_column2 = int(config.get('Data', 'csv_column2'))
        except Exception as e:
            print("Configuration Error")
            print(e)
            print(get_exception())
            sys.exit(1)

    # Get any command line arguments
    if len(sys.argv) > 4:
        csv_file_name1 = sys.argv[1]
        csv_file_name2 = sys.argv[2]
        csv_column1 = int(sys.argv[3])
        csv_column2 = int(sys.argv[4])

    # Exit if we don't have a CSV File or Column
    if csv_file_name1 is None or csv_file_name2 is None or csv_column1 is None or csv_column2 is None:
        print("Exiting as required configuration data is not present")
        sys.exit(1)

    print("CSV File Name 1: %s" % csv_file_name1)
    print("CSV File Name 2: %s" % csv_file_name2)
    print("CSV Column Index 1: %s" % csv_column1)
    print("CSV Column Index 2: %s" % csv_column2)

    config_end_time = time.time()

    print("Script started")

    root, ext = os.path.splitext(csv_file_name2)
    output = root + '-new.csv'

    with open(csv_file_name1) as r1, open(csv_file_name2) as r2, open(output, 'w') as w:
        writer = csv.writer(w)
        merge_from = csv.reader(r1)
        merge_to = csv.reader(r2)
        index = 0
        for merge_from_row, merge_to_row in zip(merge_from, merge_to):
            # replace to col 2 with from col 1
            if index > 0:
                merge_to_row[csv_column2] = merge_from_row[csv_column1]
            index+=1
            writer.writerow(merge_to_row)

    end_time = time.time()

    print("Script finished successfully")

    print("Script finished successfully")
    print("Run Time: %s" % (end_time - start_time))
    print("Configuration Time: %s" % (config_end_time - start_time))

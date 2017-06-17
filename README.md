# CsvHelper

![](https://travis-ci.org/AO-StreetArt/PythonCsvHelper.svg?branch=master)

The CSV Helper is a small set of scripts which are targeted at use in CI systems.

Current functionality is limited to copying a single CSV column from one file to another.

## Use
Arguments can be passed to the CSV Helper via configuration file to command line arguments.

    python CsvHelper.py config.ini

    python CsvHelper.py test/file1.csv test/file2.csv 0 1

These examples will copy col1 from file1.csv into col2 of file2.csv

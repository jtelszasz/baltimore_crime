# Baltimore Crime and Arrests

Justin Elszasz is analyzes open data for the Baltimore community at his website [The Training Set](http://www.thetrainingset.com).

## Description

This repository contains analysis files that investigate the change in policing tactics, primarily through changes in arrests, for Baltimore in 2015.	

## Data

**"raw_data/BPD_Arrests_2015-11-07.csv"**  
'BPD Arrests' dataset exported in csv format from [data.baltimorecity.gov](https://data.baltimorecity.gov/Public-Safety/BPD-Arrests/3i3v-ibrt) on November 7, 2015.

## Analysis Files

**"time_parser.py"**
Contains only time_parser() function for parsing dates/times from NOAA datasets.

* **time_parser()**

**"import_funcs.py"**
Contains several functions for importing Baltimore arrest and weather data.

* **import_BPD_arrests()**

* **import_CHI_arrests()**

* **import_weather()**

* **import_employees()**

#### "arrests_immed_after_FreddieGray.ipynb"

#### "post_freddie_gray_trends.ipynb"
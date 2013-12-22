import sys
import numpy as np
import pandas as pd
from datetime import datetime
import time_parser
#reload(time_parser)

def import_weather():

	bcWeather = pd.read_csv('bcWeather_201301.csv',skiprows=6,parse_dates=['Date'])


	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201302.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201303.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201304.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201305.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201306.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201307.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201308.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201309.csv',skiprows=6,parse_dates=['Date']))
	bcWeather = bcWeather.append(pd.read_csv('bcWeather_201310.csv',skiprows=6,parse_dates=['Date']))

	bcWeather.index = list(xrange(len(bcWeather['Date'])))

	bcWeather['timestamp'] = time_parser.time_parser(bcWeather['Date'],bcWeather['Time'])
	bcWeather.index = bcWeather['timestamp']
	del bcWeather['Date']
	del bcWeather['Time']
	del bcWeather['timestamp']

	return bcWeather

def import_BPDarrests():

	BPD_arrests = pd.read_csv('BPD_Arrests.csv',parse_dates=[['arrestDate','arrestTime']])
	BPD_arrests['timestamp'] = BPD_arrests['arrestDate_arrestTime']
	BPD_arrests.index = pd.to_datetime(BPD_arrests['timestamp'])
	del BPD_arrests['arrestDate_arrestTime']
	del BPD_arrests['timestamp']

	return BPD_arrests

def import_CHIarrests():

	header_chi=['CASE','TIMESTAMP','BLOCK','IUCR','PRIM_DESCR','SEC_DESCR','LOC_DESCR','ARREST','DOMESTIC','BEAT','WARD','FBI_CD','X_COORD','Y_COORD','LAT','LONG','LOCATION']
	Chicago_crimes = pd.read_csv('Chicago_All_Crimes.csv',dtype={'FBI CD': str},names=header_chi,skiprows=1)
	Chicago_crimes.index = pd.to_datetime(Chicago_crimes['TIMESTAMP'])
	del Chicago_crimes['TIMESTAMP']

	return Chicago_crimes

def import_employees():

	BLT_AllEmployees = pd.read_csv('Baltimore_City_Employee_Salaries_FY2013.csv')

	return BLT_AllEmployees




import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lost_spc')))
from error import addressReachable

def requ1(URL):
	addressReachable(URL)
	r = requests.get(f'{URL}')
	DB = r.json()
	DB =DB["Databases"]
	return DB

def requ2(DB):
	addressReachable(f'http://hlf01.ost.ch:8080/HLFInterface/getMeasurements?db={DB}')
	l = requests.get(f'http://hlf01.ost.ch:8080/HLFInterface/getMeasurements?db={DB}')
	Mea = l.json()
	Mea = Mea["Measurements"]
	return Mea 

def requ3(DB,Mea):
	addressReachable(f'http://hlf01.ost.ch:8080/HLFInterface//getData?db={DB}+measurement={Mea}')
	l = requests.get(f'http://hlf01.ost.ch:8080/HLFInterface//getData?db={DB}+measurement={Mea}')
	Live = l.json()
	return Live




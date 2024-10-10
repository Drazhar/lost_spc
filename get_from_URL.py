import requests
def requ1(URL):
	r = requests.get(f'{URL}')
	DB = r.json()
	DB =DB["Databases"]
	return DB
def requ2(DB):
	l = requests.get(f'http://hlf01.ost.ch:8080/HLFInterface/getMeasurements?db={DB}')
	Mea = l.json()
	Mea = Mea["Measurements"]
	return Mea 
def requ3(DB,Mea):
	l = requests.get(f'http://hlf01.ost.ch:8080/HLFInterface//getData?db={DB}+measurement={Mea}')
	Live = l.json()
	return Live
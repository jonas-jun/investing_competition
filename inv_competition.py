import pandas as pd
import numpy as np
import datetime
from bs4 import BeautifulSoup
import requests

# setting date
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

def get_code_list(df):
	code_list = list(df.loc[df['비고'].isnull(), 'code'])
	return code_list

def get_price(codes):
	base = 'https://finance.naver.com/item/sise_day.nhn?code='
	result = {'code': [], today: []}

	for code in codes:
		url = base + str(code)
		web = requests.get(url)
		source = BeautifulSoup(web.text, 'lxml')
		price = source.find_all('span', {'class': 'tah p11'})
		price = price[0].get_text().replace(',', '')
		result['code'].append(code)
		result[today].append(int(price))

	return result

def import_sheet(date):
	filename = 'gjy_'+str(date)+'.xlsx'
	df = pd.read_excel(filename)
	df['code'] = df['code'].apply(six_digits)

	# change date column name from '2020-07-23 00:00:00 (in excel) to like '2020-07-23'
	# 이 부분이 먹히질 않음.. 왜?
	df1 = df.copy()
	cols = list(df1.columns)
	cols[-1] = date
	df1.columms = cols

	return df1

def six_digits(codes):
	code_six = '{0:06d}'.format(codes)
	return code_six

def fill(df):
	t1, t0 = df[today], df[yesterday]
	t1_bull = t1.isnull()
	for i in range(len(t1)):
		if t1_bull[i]:
			t1[i] = t0[i]

# calculate change rates (수익률 0:01f 에서 0:02f 집계로 수정)
def cal_rates(df):
	df['수익률'] = round((df[today] - df['기준가'])/df['기준가']*100, 2)

# ordering by profit rate
def ordering(df, standard='수익률'):
	df['전일순위'] = df['현재순위']
	df_new = df.sort_values(by=standard, ascending=False, axis=0)
	t = np.array(range(len(df)))+1
	df_new['현재순위'] = t
	df_new['변동'] = df_new['전일순위'] - df_new['현재순위']
	return df_new

# export excel
def export_sheet(df):
	filename = 'gjy_'+str(today)+'.xlsx'
	df.to_excel(filename, index=False)


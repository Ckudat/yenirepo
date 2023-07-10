# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:48:37 2023

@author: monster
"""
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from datetime import datetime, timedelta

station = 'ITEKIRDA7'

chromedriver_path = "C:\chromedriver"
date = '2023-07-10'
freq = '5min'
start_date = '2023-07-09'
end_date = '2023-07-10'
def render_page(url,chromedriver_path):
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    driver.quit()
    return page_source

def scrape_wunderground(station, date, freq):
    
   
    
    if freq == '5min':
        timespan = 'daily'
    elif freq == 'daily':
        timespan = 'monthly'
    url = f'https://www.wunderground.com/dashboard/pws/{station}/table/{start_date}/{end_date}/{timespan}'

    page_source = render_page(url, chromedriver_path)
    soup = BS(page_source, "html.parser",)

    container = soup.find('lib-history-table', class_='ng-star-inserted')
    if container is None:
        raise ValueError(f"{url} adresinde lib-history-table bulunamadı")

    all_checks = container.find_all('tbody')
    time_check = all_checks[0]
    data_check = all_checks[1]
    hours = []
    for i in time_check.find_all('tr'):
        trial = i.get_text()
        hours.append(trial)

    classes = ['wu-value wu-value-to', 'wu-unit-no-value ng-star-inserted']

    data = []
    for i in data_check.find_all('span', class_=classes):
        trial = i.get_text()
        data.append(trial)

    columns = {'5min': ['sicaklik', 'Dew Point', 'nem', 'ruzgar', 
                        'sert ruzgar', 'basinc', 'Precip. Rate', 'Precip. Accum.'],
               'daily': ['Temperature_High', 'Temperature_Avg', 'Temperature_Low', 
                         'DewPoint_High', 'DewPoint_Avg', 'DewPoint_Low', 
                         'Humidity_High', 'Humidity_Avg', 'Humidity_Low', 
                         'WindSpeed_High', 'WindSpeed_Avg', 'WindSpeed_Low', 
                         'Pressure_High', 'Pressure_Low', 'Precip_Sum']
    }

    data_nan = [np.nan if x == '--' else x for x in data]

    data_array = np.array(data_nan, dtype=float)
    data_array = data_array.reshape(-1, len(columns[freq]))
    if freq == '5min':
        timestamps = ['%s %s' % (date, t) for t in hours]
    else:
        timestamps = hours
  

    df = pd.DataFrame(index=timestamps, data=data_array, columns=columns[freq])
    df.index = pd.to_datetime(df.index)

    return df


def scrape_multiattempt(station, date, attempts=4, wait_time=5.0, freq='daily'):

    df_list = [] 

    for n in range(attempts):
        try:
            df = scrape_wunderground(station, date, freq=freq)
            print("scrape_wunderground() df:", df)
            df_list.append(df)  
        except:
            time.sleep(wait_time)
        else:
            break
    else:
        df_list = [] 

    if df_list:
        df = pd.concat(df_list)
    else:
        df = pd.DataFrame() 
    return df  


def scrape_multidate(station, start_date, end_date, freq):

    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    delta = end_date - start_date

    dates = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        dates.append(day.strftime('%Y-%m-%d'))

    stations = [station] * len(dates)

    df_list = []

    for station, date in zip(stations, dates):
        df = scrape_multiattempt(station, date, freq=freq)
        df_list.append(df)


    df = pd.concat(df_list)

    return df





df = scrape_multiattempt(station, date, freq=freq)
filename = f'{station}_{date}.csv'
df.to_csv(filename)

if __name__=="__main__":
    print("df", df)
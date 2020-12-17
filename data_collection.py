# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:45:13 2020

@author: Akshay
"""


import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/Akshay/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',2, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:12:10 2020

@author: Sadat
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:04:32 2018

@author: ashwin.monpur
"""

from sqlalchemy import create_engine
engine = create_engine("mysql://root:pass@123@localhost/mf")

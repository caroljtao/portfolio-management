# portfolio-management.py
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

JNJ=wb.DataReader("JNJ",data_source="yahoo",start="2020-09-01")

#!/usr/bin/env python

import pandas as pd

df0 = pd.ExcelFile("/Users/TommasHuang/Desktop/Test/test3.xlsx").parse("AA")
# Will read and parse excel files using Pandas. First excel file, and parse which sheet name.
df1 = pd.ExcelFile("/Users/TommasHuang/Desktop/Test/test4.xlsx").parse("BB")
# Will read and parse excel files using Pandas. Second excel file, and parse which sheet name.
a0, a1 = df0.align(df1)
# Indexing and Selecting Data
different = (a0 != a1).any(axis=1)
# Calculates the difference of a DataFrame element compared with another element in the DataFrame 
# (default is the element in the same column of the previous row).
comp = a0[different].join(a1[different], lsuffix='_old', rsuffix='_new')
# Join DataFrames using their indexes.
#lsuffix : string - Suffix to use from left frame’s overlapping columns.
#rsuffix : string - Suffix to use from right frame’s overlapping columns
comp.to_excel("comparison.xls")
#Compare records of column from 2 different Excel files, report what is missing or added output comparison XLS.
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from transformation_functions import func_4

# Read recipe inputs
medium_articles = dataiku.Dataset("medium_articles")
df = medium_articles.get_dataframe()

columns = ["link"]
func_4_df = func_4(df,columns) 


# Write recipe outputs
func_4 = dataiku.Dataset("func_4")
func_4.write_with_schema(func_4_df)

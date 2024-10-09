# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from transformation_functions import func_3

# Read recipe inputs
medium_articles = dataiku.Dataset("medium_articles")
df = medium_articles.get_dataframe()

columns = ["link"]
func_3_df = func_3(df,columns) 


# Write recipe outputs
func_3 = dataiku.Dataset("func_3")
func_3.write_with_schema(func_3_df)


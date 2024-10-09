# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from transformation_functions import func_1

# Read recipe inputs
medium_articles = dataiku.Dataset("medium_articles")
df = medium_articles.get_dataframe()

columns = [""]
func_1_df = func_1(df,  # For this sample code, simply copy input to output


# Write recipe outputs
func_1 = dataiku.Dataset("func_1")
func_1.write_with_schema(func_1_df)

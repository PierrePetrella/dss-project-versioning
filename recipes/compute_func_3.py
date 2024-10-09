# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
medium_articles = dataiku.Dataset("medium_articles")
medium_articles_df = medium_articles.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

func_3_df = medium_articles_df # For this sample code, simply copy input to output


# Write recipe outputs
func_3 = dataiku.Dataset("func_3")
func_3.write_with_schema(func_3_df)

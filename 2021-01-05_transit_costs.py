import pandas as pd
import numpy as np
import pycountry
import country_converter as coco

# UDFs
def iso2c(dataf, column):
    cc = coco.CountryConverter()
    dataf[column] = coco.convert(names=dataf[column].tolist(), to='name_short')
    dataf[column] = dataf[column].replace('not found', np.nan).astype('string')
    return dataf


def objects_to_strings(dataf):
    for column in dataf.select_dtypes("object").columns:
        print(column)
        dataf[column] = dataf[column].astype('string')
    return dataf


# Getting the data
transit_cost = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-05/transit_cost.csv") \
    .copy() \
    .pipe(objects_to_strings) \
    .assign(country=lambda tc: tc['country'].replace('UK', 'GB')) \
    .pipe(iso2c, 'country')

# First view
transit_cost.info()

# Analysis
transit_cost['country'].value_counts(dropna=False)

transit_cost.query("country == 'United States'")



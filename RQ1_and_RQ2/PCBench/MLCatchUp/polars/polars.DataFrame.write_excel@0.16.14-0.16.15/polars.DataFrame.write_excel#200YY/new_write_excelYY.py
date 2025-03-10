import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(row_heights=None, float_precision=3, has_header=True, sparklines=None, column_widths=None, worksheet=None, column_totals=None, table_name=None, dtype_formats=None, autofilter=True, conditional_formats=None, column_formats=None, workbook=None, position='A1', table_style=None)

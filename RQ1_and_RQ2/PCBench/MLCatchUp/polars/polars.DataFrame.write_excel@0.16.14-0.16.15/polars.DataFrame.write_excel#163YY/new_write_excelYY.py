import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, row_heights=None, table_style=None, conditional_formats=None, column_formats=None, column_totals=None, worksheet=None, sparklines=None, table_name=None, dtype_formats=None, position='A1', column_widths=None)

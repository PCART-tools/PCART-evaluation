import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(table_name=None, column_formats=None, conditional_formats=None, worksheet=None, float_precision=3, dtype_formats=None, has_header=True, position='A1', row_heights=None, table_style=None, workbook=None, sparklines=None, column_widths=None, column_totals=None)

import os
import pandas
import sqlite3

dir = os.path.abspath(os.path.dirname(__file__))

if_exists = os.environ.get('DROP_TABLES') or 'fail'

restaurant_db_filepath = os.environ.get('RESTAURANT_DB_FILEPATH') or ('./restaurant_db.sqlite')
restaurant_csv_filepath = os.environ.get('RESTAURANT_CSV_FILEPATH') or ('csv_data/geoplaces2.csv')
con = sqlite3.connect(restaurant_db_filepath)
restaurant_df = pandas.read_csv(restaurant_csv_filepath, index_col='placeID')
restaurant_df.drop(['the_geom_meter'], axis=1, inplace=True)
restaurant_df.rename(columns={'Rambience': 'ambience'}, inplace=True)
print(restaurant_df.columns)
restaurant_df.to_sql('Restaurant', con, if_exists=if_exists)
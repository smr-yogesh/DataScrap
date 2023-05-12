import os
import json
import sqlite3
import datetime
import time
import subprocess
from sqlalchemy import true


def read_nepse_data():
    subprocess.run("./engine.py")
    with open("data\data.json", "r") as d:
        nepse = json.load(d)
        return nepse

# below this is experimental and contains heavy bugs and unnecessary code.
# conn = sqlite3.connect('data.db')
# date = datetime.datetime.now().strftime("%x")
# table_name = f"T_{date.replace('/', '_')}"

# def set_database():
#     c = conn.cursor()
#     c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (symbols text, Closing number, Change number, High number, Low number, Open number)")
#     conn.commit()

# def data_to_database():
#     while true:
#         set_database()
#         scrape().to_sql(f'{table_name}', conn, if_exists='replace', index = False)
#         print("Job done \n\nTime to sleep")
#         now = datetime.datetime.now()
#         tomorrow = now + datetime.timedelta(days=1)
#         noon = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=12, minute=0, second=0)
#         if now>=noon:
#             noon += datetime.timedelta(days=1)
#         time_to_sleep = (noon - now).total_seconds()

#         # Sleep for the calculated time
#         time.sleep(time_to_sleep)

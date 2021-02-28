from utils.database_manager import db_manager
from sqlite3 import connect
from os.path import join
from pathlib import Path


database = db_manager(connect(join(Path(__file__).resolve().parent, 'data/database.sqlite3')))


HOST = '''localhost'''
USER = '''root'''
PASSWORD = ''''''

FILE_PATH = '''input.json'''

DB_NAME = '''OTRS_DATA'''
TBL_NAME = '''KEYWRDS'''

COLUMN_0 = '''KEYWORD'''
COLUMN_1 = '''VALUE'''

CMD_MKDB = '''CREATE DATABASE {0} ;'''
CMD_MKTBL = '''CREATE TABLE {0} ({1} varchar(255),{2} varchar(255));'''
CMD_INSERT = '''INSERT INTO {0}.{1} ({2}, {3}) VALUES ('{4}', '{5}');'''

CMD_SHWDB = '''SHOW DATABASES ;'''
CMD_SHWTBL = '''SHOW TABLES ;'''

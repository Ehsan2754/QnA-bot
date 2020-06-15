import constant
import mysql.connector as socket
import json


def getFileData():
    file = open(constant.FILE_PATH, 'r')
    return json.load(file)


def connectDBserver():
    return socket.connect(
        host=constant.HOST,
        user=constant.USER,
        password=constant.PASSWORD
    )


def listDB(DBshell, cmd):
    DBshell.execute(cmd)
    return [item[0] for item in DBshell]


if __name__ == "__main__":
    DBserver = connectDBserver()
    DBshell = DBserver.cursor()
    if constant.DB_NAME not in listDB(DBshell, constant.CMD_SHWDB):
        DBshell.execute(constant.CMD_MKDB.format(constant.DB_NAME))
        DBserver.commit()
    DBserver.database = constant.DB_NAME
    if constant.TBL_NAME not in listDB(DBshell, constant.CMD_SHWTBL):
        DBshell.execute(constant.CMD_MKTBL.format(
            constant.TBL_NAME, constant.COLUMN_0, constant.COLUMN_1))
        DBserver.commit()
    for item in getFileData():
        DBshell.execute(
            constant.CMD_INSERT.format
            (
                constant.DB_NAME,
                constant.TBL_NAME,
                constant.COLUMN_0,
                constant.COLUMN_1,
                item[constant.COLUMN_0],
                item[constant.COLUMN_1])
        )
        DBserver.commit()

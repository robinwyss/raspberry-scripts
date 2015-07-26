from ftplib import FTP
from os.path import basename
import config

ftp_config = config.getFtpConfig()

def _openConnection():
    address = ftp_config["address"]
    user = ftp_config["user"]
    password = ftp_config["password"]
    folder = ftp_config["folder"]
    connection = FTP(address, user, password)
    connection.cwd(folder)
    return connection

def uploadFile(path):
    name = basename(path)
    connection = _openConnection()
    with open(path, 'rb') as file:
        connection.storbinary('STOR ' + name, file)
        file.close()
        connection.quit()
from ftplib import FTP
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

def uploadFile(path, name):
    connection = _openConnection()
    file = open(path, 'rb')
    connection.storbinary('STOR ' + name, file)
    file.close()
    connection.quit()


uploadFile("/Users/robinwyss/Downloads/DSC_0643.JPG", "DSC_0643.JPG")
import os
import shutil
import datetime

src = "/home/abhi/backup"
des = "/home/abhi/backup"

def getDate(file_name):
    date = os.path.getmtime(file_name)
    return datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d')


for file_name in os.listdir(src):
    src_file_name = os.path.join(src,file_name)
    file_date = getDate(os.path.join(src, file_name))
    des_folder_name = os.path.join(des, file_date)
    os.makedirs(des_folder_name, exist_ok=True)
    des_file_name = os.path.join(des_folder_name, file_name)
    shutil.move(src_file_name, des_file_name)

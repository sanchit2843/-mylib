import os
os.system("pip install wget requests")
os.system("pip install -q kaggle")
import shutil
import requests
import wget
import tarfile
import zipfile
def zipextract(src,des=None):
    if(des == None):
        zip_ref = zipfile.ZipFile(src, 'r')
        zip_ref.extractall(os.getcwd())
        zip_ref.close()
    else:
        zip_ref = zipfile.ZipFile(src, 'r')
        zip_ref.extractall(des)
        zip_ref.close()
    os.remove(src)
def tarextract(src):
    tar = tarfile.open(src)
    tar.extractall()
    tar.close()
def download(url,path= None):
    if(path==None):
        wget.download(url,os.getcwd())
    else:
        wget.download(url,path)
def kaggle():
    from google.colab import files
    files.upload()
    os.system("mkdir -p ~/.kaggle")
    os.system("cp kaggle.json ~/.kaggle/")
    os.system("chmod 600 ~/.kaggle/kaggle.json")
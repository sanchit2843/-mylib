import os
import shutil
def kaggle(path = None):
    if(path == None):
        from google.colab import files
        files.upload()
        !pip install -q kaggle
        a = os.getcwd()
        os.mkdir("kaggle")
        b = os.join(a,"kaggle.json")
        c = os.join(a,kaggle)
        shutil.copyfile(b,c)
        os.chmod("./kaggle/kaggle.json", 600)
    else:
        !pip install -q kaggle
        os.mkdir("kaggle")
        b = os.join(path,"kaggle.json")
        a = os.getcwd()
        c = os.join(a,kaggle)
        shutil.copyfile(b,c)
        os.chmod("./kaggle/kaggle.json", 600)        
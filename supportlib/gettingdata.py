import os
import shutil
def kaggle(path = None):
    if(path == None):
        from google.colab import files
        files.upload()
        a = os.getcwd()
        os.mkdir("kaggle")
        b = os.path.join(a,"kaggle.json")
        c = os.path.join(a,kaggle)
        shutil.copyfile(b,c)
        os.chmod("./kaggle/kaggle.json", 600)
    else:
        os.mkdir("kaggle")
        b = os.path.join(path,"kaggle.json")
        a = os.getcwd()
        c = os.path.join(a,kaggle)
        shutil.copyfile(b,c)
        os.chmod("./kaggle/kaggle.json", 600)        
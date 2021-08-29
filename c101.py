from __future__ import with_statement
from os import name
import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videocaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame=videocaptureObject.read()
        imagename='img'+str(number)+'.png'
        cv2.imwrite(imagename,frame)
        start_time=time.time()
        result=False
    
    return imagename
    print('Snapshot Taken')
    videocaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imagename):
    access_token = 'sl.A3UQYVo_CYwoMA529qyDsKTE9FNCpBVxDOBcBvnIn5dVkFMUHwYyvx6KScWjLdmDCYdCQBU3gC-jkcebtcfItLjB_640Nfj3dyMxxXBv8TV2SWuHbS_MOd7wcvsNe-RcmxeuOjU'
    file=imagename
    file_from = file
    file_to = '/newFolder/'+(imagename)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded.')

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()
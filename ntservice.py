import sys
import os
import time
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
from subprocess import call
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from pytz import utc, timezone


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "servicerclone"
    _svc_display_name_ = "Service rclone AWS"
    command = 'dir' #'C:\\Tools\\rclone\\rclone sync bcksnapshot:itpedia/SQLDEMO_ERACENT_SKUMAPPING_PUB_SKUMAPP E:\\!ReplData\\unc\\SQLDEMO_ERACENT_SKUMAPPING_PUB_SKUMAPP'
    value = '0'


    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def check():
        if 1 in open('check.txt').read():
            os.system(command)
            with open('check.txt','w') as f:
                f.write(value)
        pass

    def main(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(check, 'interval', minutes=2)
        scheduler.start()
        try:
            print('Press <Ctrl + C> to stop! datetime={}'.format(datetime.now()))
            time.sleep(100000)
        except KeyboardInterrupt:
            print('Stopping...')
            scheduler.shutdown() 

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
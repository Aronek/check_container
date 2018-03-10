import sys
from subprocess import call
from apscheduler.schedulers.background import BackgroundScheduler
import os
import time
from datetime import datetime, timedelta
from pytz import utc, timezone

cmd = 'C:\\Tools\\rclone\\rclone sync bcksnapshot:itpedia/SQLDEMO_ERACENT_SKUMAPPING_PUB_SKUMAPP E:\\!ReplData\\unc\\SQLDEMO_ERACENT_SKUMAPPING_PUB_SKUMAPP'
cmd2 = 'dir'
text = '0'
def check():
    if '1' in open('check.txt').read():
        os.system(cmd2)
        with open('check.txt', 'w') as f:
                f.write(text)
    else:
        print('waitning for data to synchronized')

def main():
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
    main()
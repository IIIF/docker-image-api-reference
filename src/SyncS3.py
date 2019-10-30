#!/usr/bin/env python3

import hashlib
from os import path
import os
import boto3

from pytz import timezone
from dateutil.tz import tzlocal
from tzlocal import get_localzone
import datetime

def syncS3(): 
    session = boto3.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
    s3client = session.resource('s3')

    bucketcontents = s3client.Bucket('iiif-fixtures').objects.filter(Prefix='images')
    localDir = './iiif/testimages'
    log = ''
    for s3fileinfo in bucketcontents:
        if not s3fileinfo.key.endswith('/metadata.json') and not s3fileinfo.key.endswith('/'):
            localfilename = '{}/{}'.format(localDir, shorternFilename(s3fileinfo.key))
            download = False
            if path.exists(localfilename):
                # check lastmod
                localLastMod = timestamp(localfilename)
                if localLastMod < s3fileinfo.last_modified:
                    # download
                    download = True
                    log += '<li>Updating: {} from {}</li>'.format(localfilename, s3fileinfo.key)
            else:
                download = True
                log += '<li>Downloading: {} from {}</li>'.format(s3fileinfo.key, localfilename)
                
            if download:
                s3client.meta.client.download_file('iiif-fixtures', s3fileinfo.key, localfilename)
    return '<html><body><h1>Sync actions:</h1><ul>{}</ul></body></html>'.format(log)

def timestamp(filepath):
    return localtimezone.localize(datetime.datetime.fromtimestamp(os.stat(filepath).st_mtime))

def shorternFilename(filepath):
    dirpath = hashlib.md5(path.dirname(filepath).encode('utf-8')).hexdigest()
    basename = path.basename(filepath)

    return "{}-{}".format(dirpath, basename)


def loadApp(app):
    app.add_url_rule('/sync.html', 'SyncS3', syncS3, methods=['GET'])
    
localtimezone = get_localzone()

if __name__ == "__main__":
    syncS3()

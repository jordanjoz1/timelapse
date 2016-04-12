import urllib
from datetime import datetime
import os
import time
import argparse
import sys

DEF_POLL_FREQ = 10  # seconds


def main():

    # parse arguments
    name, output_dir, dlUrl, pollFreq = parseArgs()

    pidfile = checkIfRunning(name)

    try:
        while True:
            dt = datetime.now()

            dirPath = createDirPath(dt, output_dir)
            createDirIfNotExists(dirPath)

            fname = createFileName(dt)
            fpath = createFilePath(dirPath, fname)

            sys.stdout.flush()
            print fpath

            saveImage(dlUrl, fpath)

            time.sleep(pollFreq)
    finally:
        os.unlink(pidfile)


def parseArgs():
    # parse arguments and do error checking
    parser = argparse.ArgumentParser()
    parser.add_argument('name',
                        help='Used for process tracking to verify not '
                             'already running')
    parser.add_argument('output_dir',
                        help='The name of the directory where the images '
                             'will be saved')
    parser.add_argument('url',
                        help='The url to download the image from')
    parser.add_argument('--poll_freq',
                        help='How often (in seconds) to poll for image',
                        default=DEF_POLL_FREQ)
    args = parser.parse_args()
    return args.name, args.output_dir, args.url, args.poll_freq


def checkIfRunning(name):
    pid = str(os.getpid())
    pidfile = '/tmp/EYECAPTURE-' + name + '.pid'

    if os.path.isfile(pidfile):
        print "%s already exists, exiting" % pidfile
        sys.exit()
    file(pidfile, 'w').write(pid)
    return pidfile


def createDirPath(dt, outDir):
    return os.path.join(os.getcwd(), outDir, str(dt.year), str(dt.month),
                        str(dt.day))


def createFilePath(dirPath, fname):
    return os.path.join(dirPath, fname)


def createFileName(dt):
    return dt.strftime('%H%M%S') + '.jpg'


def createDirIfNotExists(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)


def saveImage(dlUrl, fpath):
    try:
        fname, message = urllib.urlretrieve(dlUrl, fpath)
    except IOError as e:
        # don't do anything with errors, we'll just try again on the next save
        print 'Request failed. Sad face.'


if __name__ == "__main__":
    main()

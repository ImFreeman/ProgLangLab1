import http.client
import os
import time
import threading
import sys

def download_file(url: str):
    domain = url.split('/')
    path = '/' + '/'.join(url.split('/')[3:])
    conn = http.client.HTTPSConnection(domain[0])
    conn.request('GET', path)
    resp = conn.getresponse()
    filename = os.path.basename(url)
    file = open(filename, 'wb')
    size = 0
    while True:
        lock = threading.Lock()
        lock.acquire()
        try:
            chunk = resp.read(1024)
            size += len(chunk)
            file.write(chunk)
            time.sleep(1)
            print(f'{size} bytes received')
        finally:
            lock.release()
        if not chunk:
            break
    file.close()
    conn.close()
    return 'Download complete'


if __name__ == '__main__':
    url:str = sys.argv[1]
    print(download_file(url))




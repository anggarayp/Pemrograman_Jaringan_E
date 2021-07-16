import logging
import requests
import socket
import os
import time
import datetime

def get_url_list():
    urls = dict()
    # urls['its']='https://awsimages.detik.net.id/customthumb/2012/03/02/398/ITS-Tech-dalam.jpg'
    urls['niki']='https://images.bisnis-cdn.com/thumb/posts/2020/09/10/1289694/screenshot_20200910-091215_instagram_copy_800x500.jpg?w=744&h=465'
    urls['bonek']='https://pbs.twimg.com/profile_images/1399902340895842306/BiQEKdL6.jpg'
    return urls

def download_gambar(url=None,tuliskefile='image'):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/gif']='gif'
    tipe['image/jpeg']='jpg'
    tipe['application/zip']='jpg'
    tipe['video/quicktime']='mov'
#    time.sleep(2) #untuk simulasi, diberi tambahan delay 2 detik

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        if (tuliskefile):
            fp = open(f"{tuliskefile}.{ekstensi}","wb")
            fp.write(ff.content)
            fp.close()
        waktu_process = datetime.datetime.now() - waktu_awal
        waktu_akhir =datetime.datetime.now()
        logging.warning(f"writing {tuliskefile}.{ekstensi} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
        return waktu_process
    else:
        return False

def kirim_gambar(IP_ADDRESS, PORT, filename):
    print(IP_ADDRESS, PORT, filename)
    ukuran=os.stat(filename).st_size
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    fp=open(filename,'rb')
    k=fp.read()
    terkirim=0
    for x in k:
        k_bytes=bytes([x])
        clientSock.sendto(k_bytes,(IP_ADDRESS,PORT))
        terkirim=terkirim+1
#        print(k_bytes,f"terkirim {terkirim} of {ukuran}")


if __name__=='__main__':
    #check fungsi
    k = download_gambar('https://images.bisnis-cdn.com/thumb/posts/2020/09/10/1289694/screenshot_20200910-091215_instagram_copy_800x500.jpg?w=744&h=465')
    print(k)
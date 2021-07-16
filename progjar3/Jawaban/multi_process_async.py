from library import download_gambar, get_url_list, kirim_gambar
import time
import datetime
from multiprocessing import Process, Pool

def kirim_file():
    texec = dict()
    urls = get_url_list()
    a = 0
    status_task = dict()
    task_pool = Pool(processes=15) #2 task yang dapat dikerjakan secara simultan, dapat diset sesuai jumlah core
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k],k)
        print(f"mendownload {urls[k]}")
        UDP_IP_ADDRESS = "192.168.122.205"
        UDP_IP_ADDRESS2 = "192.168.122.31"
        PORT = 88
        if a == 0:
            texec[k] = task_pool.apply_async(func=kirim_gambar, args=(UDP_IP_ADDRESS, PORT, f"{k}.jpg"))
            print('--Server 1--')
            a = a + 1
        elif a == 1:
            print('--Server 2--')
            texec[k] = task_pool.apply_async(func=kirim_gambar, args=(UDP_IP_ADDRESS2, PORT, f"{k}.jpg"))

    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan mengambil hasilnya dengan get
    for k in urls:
        status_task[k]=texec[k].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)

#fungsi download_gambar akan dijalankan secara multi process
if __name__=='__main__':
    kirim_file()
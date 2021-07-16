from library import download_gambar,get_url_list, kirim_gambar
import time
import datetime
import concurrent.futures

def kirim_file():
    texec = dict()
    urls = get_url_list()
    a = 0
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        UDP_IP_ADDRESS = "192.168.122.205"
        UDP_IP_ADDRESS2 = "192.168.122.31"
        PORT = 88
        if a == 0:
            texec[k] = task.submit(kirim_gambar,UDP_IP_ADDRESS, PORT, f"{k}.jpg")
            print('--Server 1--')
            a = a + 1
        elif a == 1:
            print('--Server 2--')
            texec[k] = task.submit(kirim_gambar,UDP_IP_ADDRESS2, PORT, f"{k}.jpg")

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan memanggil result
    for k in urls:
        status_task[k]=texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)

#fungsi download_gambar akan dijalankan secara multithreading
if __name__=='__main__':
    kirim_file()
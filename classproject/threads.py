import time
import threading


counter = 0
def watcher():
    global counter
    for i in range(50):
        print("counter = ",i, counter)
        time.sleep(0.1)



def update():
    name = threading.current_thread().ident
    global counter
    for i in range(5):
        counter += 1
        time.sleep(0.1)


def main():
    thread1 = threading.Thread(target=update)
    thread2 = threading.Thread(target=update)
    thread3 = threading.Thread(target=watcher)
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == '__main__':
    main()

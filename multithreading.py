import threading
import time

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk boiled.")

def toast_bun():
    print(f"Toasting bun...")
    time.sleep(3)
    print("Bun toasted.")

start = time.time();

milk_thread = threading.Thread(target=boil_milk)
bun_thread = threading.Thread(target=toast_bun)

milk_thread.start()
bun_thread.start()
milk_thread.join()
bun_thread.join()

end = time.time();
print(f"Total time taken: {end - start:.2f} seconds")
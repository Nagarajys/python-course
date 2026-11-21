import time


def process_data():
    start = time.time()
    print("DATA PROCESSING STARTED")
    time.sleep(3)
    print("DATA PROCESSING COMPLETED")
    end = time.time()
    excecution_time = end - start
    print("Execution time:", f"approximetly{excecution_time} seconds")


process_data()

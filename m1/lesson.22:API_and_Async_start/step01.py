import time


start_time = time.time()
print("Start")
time.sleep(3)
print("pause")

time.sleep(3)
print("End")

end_time = time.time()
result = end_time - start_time
print(result)
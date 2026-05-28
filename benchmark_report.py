import time
from verification_service import execute_ipc_subtraction

print("==================================================================")
print("IPC LATENCY BENCHMARK: EXECUTING ULTRA-HIGH VELOCITY CYCLE TESTS



")
print("==================================================================")

start_time = time.time()
iterations = 500000

for i in range(iterations):
    execute_ipc_subtraction(100, 100)

elapsed = time.time() - start_time
print(f"Total Computation Operations Run: {iterations:,} cycles")
print(f"Total Execution Time Consumed:     {elapsed:.4f} seconds")
print(f"Average Processing Speed:          {iterations/elapsed:,.2f} operations/sec")
print("==================================================================")


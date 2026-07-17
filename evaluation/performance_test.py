import json
import time
from concurrent.futures import ThreadPoolExecutor

from Ai_pipeline import run_pipeline

# -------------------------
# Load Golden Set
# -------------------------

with open("golden_set/stories.json", "r") as file:
    stories = json.load(file)

# Create 10 requests
requests = stories * 10

# -------------------------
# Function executed by each thread
# -------------------------

def process_story(story):

    start = time.perf_counter()

    run_pipeline(story["user_story"])

    end = time.perf_counter()

    return end - start

# -------------------------
# Performance Test
# -------------------------

print("=" * 50)
print("Load Test")
print("=" * 50)

overall_start = time.perf_counter()

with ThreadPoolExecutor(max_workers=10) as executor:

    response_times = list(
        executor.map(process_story, requests)
    )

overall_end = time.perf_counter()

print(f"Total Requests : {len(requests)}")
print(f"Concurrent Users : 10")
print(f"Total Time : {overall_end-overall_start:.4f} sec")
print(f"Average Response Time : {sum(response_times)/len(response_times):.4f} sec")
print(f"Fastest Request : {min(response_times):.4f} sec")
print(f"Slowest Request : {max(response_times):.4f} sec")
import statistics

file_names = [
    "ori-f1-c-fuzzer_result.csv",
    "limit-fuzzer-no-jit_result.csv",
    "limit-fuzzer-nr-no-jit_result.csv",
    "LimitFuzzer-pypy_result.csv",
    "LimitFuzzer-NR-pypy_result.csv"
]

for f_name in file_names:
    with open(f_name, "r") as f:
        data = []
        for line in f.readlines():
            data.append(float(line.strip()))
        print("---------------------------")
        print(f"Filename: {f_name}, Data entries count: {len(data)}")
        print(f"Max: {max(data)}, Mean: {statistics.mean(data)}, Min: {min(data)}")
        print(f"Median: {statistics.median(data)}")
        print(f"Standard deviation: {statistics.stdev(data)}")
        print(f"Variance: {statistics.variance(data)}")
#!/bin/sh

REPEAT_N_TIMES=5
RUNS=100000
ORIGINAL_BIN_SEED=123459090
DEPTH=10
RAND_IN='1048576B_rand_data'

ORI_BIN_NAME='ori-f1-c-fuzzer'
LIMIT_FUZZER_BIN_NAME='limit-fuzzer-no-jit'
LIMIT_FUZZER_NR_BIN_NAME='limit-fuzzer-nr-no-jit'
PYPY_LIMIT_FUZZER_NAME='LimitFuzzer-pypy'
PYPY_LIMIT_FUZZER_PATH='rpy_limitfuzzer/main_recursive.py'
PYPY_LIMIT_FUZZER_NR_NAME='LimitFuzzer-NR-pypy'
PYPY_LIMIT_FUZZER_NR_PATH='rpy_limitfuzzer/main.py'

export PYTHONPATH=../pypy
# Exit on error
set -e

# Build original fuzzer
python3 original/main.py > original/fuzzer.c
gcc -O2 -o "$ORI_BIN_NAME" original/fuzzer.c

# Build RPython recursive limitfuzzer
# pypy ../pypy/rpython/bin/rpython --output "$LIMIT_FUZZER_BIN_NAME" rpy_limitfuzzer/main_recursive.py

# Build RPython iterative limitfuzzer
# pypy ../pypy/rpython/bin/rpython --output "$LIMIT_FUZZER_NR_BIN_NAME" rpy_limitfuzzer/main.py


echo "Running $ORI_BIN_NAME"
RESULT_FILE="$ORI_BIN_NAME"_result.csv
# AVG_FILE="$RESULT_FILE"_avg.csv
AVG_FILE=result_avg.csv
echo -n '' > $RESULT_FILE
for N in $(seq $REPEAT_N_TIMES)
do
    /usr/bin/time -p ./$ORI_BIN_NAME $ORIGINAL_BIN_SEED $RUNS $DEPTH 2>&1 > /dev/null | grep real | sed -e 's/real //' >> $RESULT_FILE
done
python -c "
sum = 0.0
count = 0
with open('$RESULT_FILE', 'r') as f:
    for line in f.readlines():
        sum += float(line.strip())
        count += 1
print(f'$ORI_BIN_NAME,{sum / count}')
" > $AVG_FILE


echo "Running $LIMIT_FUZZER_BIN_NAME"
RESULT_FILE="$LIMIT_FUZZER_BIN_NAME"_result.csv
# AVG_FILE="$RESULT_FILE"_avg.csv
echo -n '' > $RESULT_FILE
for N in $(seq $REPEAT_N_TIMES)
do
    /usr/bin/time -p ./$LIMIT_FUZZER_BIN_NAME --runs $RUNS < $RAND_IN 2>&1 > /dev/null | grep real | sed -e 's/real //' >> $RESULT_FILE
done
python -c "
sum = 0.0
count = 0
with open('$RESULT_FILE', 'r') as f:
    for line in f.readlines():
        sum += float(line.strip())
        count += 1
print(f'$LIMIT_FUZZER_BIN_NAME,{sum / count}')
" >> $AVG_FILE


echo "Running $LIMIT_FUZZER_NR_BIN_NAME"
RESULT_FILE="$LIMIT_FUZZER_NR_BIN_NAME"_result.csv
# AVG_FILE="$RESULT_FILE"_avg.csv
echo -n '' > $RESULT_FILE
for N in $(seq $REPEAT_N_TIMES)
do
    /usr/bin/time -p ./$LIMIT_FUZZER_NR_BIN_NAME --runs $RUNS < $RAND_IN 2>&1 > /dev/null | grep real | sed -e 's/real //' >> $RESULT_FILE
done
python -c "
sum = 0.0
count = 0
with open('$RESULT_FILE', 'r') as f:
    for line in f.readlines():
        sum += float(line.strip())
        count += 1
print(f'$LIMIT_FUZZER_NR_BIN_NAME,{sum / count}')
" >> $AVG_FILE


echo "Running $PYPY_LIMIT_FUZZER_NAME"
RESULT_FILE="$PYPY_LIMIT_FUZZER_NAME"_result.csv
# AVG_FILE="$RESULT_FILE"_avg.csv
echo -n '' > $RESULT_FILE
for N in $(seq $REPEAT_N_TIMES)
do
    /usr/bin/time -p pypy $PYPY_LIMIT_FUZZER_PATH --runs $RUNS < $RAND_IN 2>&1 > /dev/null | grep real | sed -e 's/real //' >> $RESULT_FILE
done
python -c "
sum = 0.0
count = 0
with open('$RESULT_FILE', 'r') as f:
    for line in f.readlines():
        sum += float(line.strip())
        count += 1
print(f'$PYPY_LIMIT_FUZZER_NAME,{sum / count}')
" >> $AVG_FILE

echo "Running $PYPY_LIMIT_FUZZER_NR_NAME"
RESULT_FILE="$PYPY_LIMIT_FUZZER_NR_NAME"_result.csv
# AVG_FILE="$RESULT_FILE"_avg.csv
echo -n '' > $RESULT_FILE
for N in $(seq $REPEAT_N_TIMES)
do
    /usr/bin/time -p pypy $PYPY_LIMIT_FUZZER_PATH --runs $RUNS < $RAND_IN 2>&1 > /dev/null | grep real | sed -e 's/real //' >> $RESULT_FILE
done
python -c "
sum = 0.0
count = 0
with open('$RESULT_FILE', 'r') as f:
    for line in f.readlines():
        sum += float(line.strip())
        count += 1
print(f'$PYPY_LIMIT_FUZZER_NR_NAME,{sum / count}')
" >> $AVG_FILE

gnuplot plot.gp
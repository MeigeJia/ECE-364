#! /bin/bash
for i in {1..12}
do
    python3 test.py $i > test/test${i}.out
    #python3 test.py $i > test/test${i}_rehana.out
    echo "Diff for function# ${i}:"
    diff test/test${i}.out test/test${i}_rehana.out
done

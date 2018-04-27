i=0
while :
do
    echo "Testing case $i"
    python3 gen.py > test.txt

    python3 $1 < test.txt > a.txt
    if (($? != 0))
    then
        break
    fi
    if [ $2 == "organic" ]
    then
        cp a.txt b.txt
    else
        python3 $2 < test.txt > b.txt
    fi

    difference=`diff a.txt b.txt`

    if [ ! -z  "$difference" ]
    then
        echo
        echo "Test case $i failed."
        echo $difference > diff.txt
        break
    fi
    i=$((i + 1))
done

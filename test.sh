i=0
while :
do
    echo $i
    #echo Generating inputs...
    python3 gen.py > test.txt

    #echo Running IUT...
    python3 $1 < test.txt > a.txt
    if (($? != 0))
    then
        break
    fi
    #echo Running oracle...
    if [ $2 == "smoke" ]
    then
        cp a.txt b.txt
    else
        python3 $2 < test.txt > b.txt
    fi

    difference=`diff a.txt b.txt`

    if [ ! -z  "$difference" ]
    then
        echo "Test case $i failed."
        echo $difference > diff.txt
        break
    fi
    i=$((i + 1))
done

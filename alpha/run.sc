

if [[ "$1" == "" ]]
then
	python ./test.py
else
	if [[ "$1" == "clean" ]]
	then
		rm -rf *.pyc output.spx
	fi
fi

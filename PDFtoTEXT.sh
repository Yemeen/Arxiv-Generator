for i in ./data/*.pdf
do 
	pdftotext -q -layout $i
	rm -rf $i
done

#! /bin/bash

pdftoppm Flashcards_Analitica.pdf outputname -png


# convert names to front F and back B enumeration
#for 


for FILE in *.png; 
do
 
	convert -crop 100%x33.33% $FILE q_$FILE ; 
done

rm output*.png
rm q_outputname-*-3.png


for FILE in *.png;
do 
	echo "${FILE#*-}"
done




#convert -crop 100%x33.33% outputname-01.png outputname11.png

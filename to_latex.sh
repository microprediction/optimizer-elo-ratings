#lynx -dump -source https://microprediction.github.io/optimizer-elo-ratings/ > source.html

for k in `seq 1 20`
do
sed 's/<a href=./\
	/g' source.html >data 
cat data | sed 's/^[ 	]*/https:\/\/microprediction.github.io\/optimizer\-elo\-ratings\//g' | sed 's/.>.*//g' | grep '\.html'> data2
touch all_results.tex
rm all_results.tex
for l in `cat data2`
do
	echo "\\subsection{Results for `echo $l | sed 's/.*\///g' | sed 's/_/ /g' | sed 's/.html//g'`}" 
	#lynx -dump $l -source > `echo $l | sed 's/.*\///g'`.data.txt
	touch `echo $l | sed 's/.*\///g'`.data.txt 
	file=`ls -ctr *.data.txt | tail -n 1`
	echo '\begin{itemize}'
	grep ' <h3>' $file  | sed 's/<h3>//g' | sed 's/<.h3>//g' | sed 's/^/\\item /g'
	echo -n '\item Num algorithms: '
	sed 's/<tr>/\
		/g' $file | grep -i 'td>yes<' | wc -l
	echo '\end{itemize}'
	echo '\begin{tabular}{|c|c|c|c|}'
	echo '\hline'
	echo ' Algorithm& ELO & num games \\'
	echo '\hline'
	sed 's/<tr>/\
		/g' $file | grep -i 'td>yes<' | head -n $k | sed 's/<td>/ \& /g' | sed 's/<.td>//g' | sed 's/$/\\\\/g' | sed 's/^[ 	]*&//g' | sed 's/..yes..tr.//g' | sed 's/_/\-/g'
	echo '\hline'
	echo '\end{tabular}'
done | tee all_results.tex
grep '^ ' all_results.tex  | grep '^[^&]*&[^&]*&[^&]*\\$' | sed 's/&.*//g' | sort | uniq -c | sort -n >> all_results.tex
mv all_results.tex all_results_${k}.tex
done
tail -n 15 all_results_*.tex

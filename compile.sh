python3 "./gen/$1.py" > "./gen/$1_gen.tex"
pdflatex -output-directory="./compiled" "./gen/$1_gen.tex"
open "./compiled/$1_gen.pdf"
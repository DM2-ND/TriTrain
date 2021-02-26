echo $1
python preprocessing.py $1 distant-corpus_par.json
python parthesis.py  distant-corpus_par.json ../SCHBase-Relabel/distant-corpus.json
rm distant-corpus_par.json
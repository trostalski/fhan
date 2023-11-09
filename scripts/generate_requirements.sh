sed '/^-e/d' requirements.lock > requirements.tmp
sed '/^-e/d' requirements-dev.lock >> requirements.tmp
cat requirements.tmp > requirements.txt
rm requirements.tmp

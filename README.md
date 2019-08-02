# tagcounter


# create archive sdist
python setup.py sdist

# Install aplication tagcounter
pip install .

# Usage

get tags using config file
tagcounter --get "yahoo.com"

get from any resource
tagcounter -r yahoo.com

get statistic from database
tagcounter -v yahoo.com

run tests(not implemented!)
tagcounter -t
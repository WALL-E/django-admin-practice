#!/bin/bash

#!/bin/bash

PWD=$(cd "$(dirname "$0")"; pwd)

cd ${PWD}

./get_balance.py
./get_currencies.py
./get_symbols.py

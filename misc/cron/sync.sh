#!/bin/bash

#!/bin/bash

PWD=$(cd "$(dirname "$0")"; pwd)

cd ${PWD}

./load_balance.py
./load_currencie.py
./load_symbol.py

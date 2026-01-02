#!/bin/bash


# -- Saver version of scipt ---------------------
# https://www.howtogeek.com/782514/how-to-use-set-and-pipefail-in-bash-scripts-on-linux/
# (-e)xit on error
# (-u)nset variables raise error
# (-o)option:
# pipefail: the return value of a pipeline is the status of
#           the last command to exit with a non-zero status,
#           or zero if no command exited with a non-zero statu
set -euo pipefail
rm -rf build

# -E ignore cached environment; -a write all files
sphinx-build -b html -E -a ./src ./build

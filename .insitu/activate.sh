#!
export_ () { export $1=$2; }
export_ POET        $(dirname ${PWD})
export_ POET_BIN    ${POET}/bin
export_ POET_USER   ${POET}/user
export_ POET_POEM   ${POET}/poem
export_ POET_VENDOR ${POET}/.vendor
export_ PATH        ${POET_BIN}:$(./fixpath.py ${POET_BIN})

. ${POET_USER}/dotfiles/dot$1

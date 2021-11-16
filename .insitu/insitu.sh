#!/source/this/sh
[ ! "${1}" == "" ] && \
[ -d "${1}"      ] && \
{
    pushd ${1} > /dev/null
    shift
    $*
    popd > /dev/null
}

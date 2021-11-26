#!/bin/bash
pushd > /dev/null $(dirname $0)/suite.foo/.insitu
. ./activate
popd > /dev/null
proxy-foo

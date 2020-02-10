#!/bin/bash
set -e
docker run -d -i -t -e python_ver=$PYTHON_VER --name manylinux10 -v `pwd`:/io rthz/manylinux-gtda /bin/bash
docker exec manylinux10 sh -c "sh /io/.azure-ci/manylinux2010/build_test.sh"

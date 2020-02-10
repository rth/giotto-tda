# A manylinux2010 image with boost pre-installed
FROM quay.io/pypa/manylinux2010_x86_64

# Install boost
RUN yum install -y wget tar && \
    wget https://dl.bintray.com/boostorg/release/1.69.0/source/boost_1_69_0.tar.gz  && \
    tar -zxvf /boost_1_69_0.tar.gz && \ 
    mkdir boost && \
    cd /boost_1_69_0 && \
    ./bootstrap.sh --prefix=/boost && \
    ./b2 install && \
    rm -f /boost_1_69_0.tag.gz

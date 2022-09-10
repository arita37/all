FROM openjdk:8

MAINTAINER Fokko Driesprong <fokkodriesprong@godatadriven.com>

RUN update-ca-certificates -f \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y \
    software-properties-common \
    wget \
    git \
    libatlas3-base \
    libopenblas-base \
    libatlas-base-dev \
    build-essential \
  && apt-get clean



#####################################################################################################
# Miniconda
ENV CONDA_DIR=/opt/miniconda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    chmod a+x miniconda.sh && \
    ./miniconda.sh -b -p $CONDA_DIR && \
    rm ./miniconda.sh && \
    conda install python=3.8.1



###### work folder  ################################################################################
WORKDIR /opt/work/ 


#RUN pip install --upgrade pip \
RUN conda env -n dcgpy  python=3.8.1 && source activate dcgpy && \
    conda  install -c conda-forge -y   \
#abseil-cpp                20200225.2           ha925a31_2    conda-forge
#arb                       2.17.0               h1439f5e_1    conda-forge
#boost                     1.72.0           py38hfd46600_1    conda-forge
#boost-cpp                 1.72.0               h5b4e17d_7    conda-forge
#bzip2                     1.0.8                h8ffe710_4    conda-forge
#ca-certificates           2022.6.15            h5b45459_0    conda-forge
#certifi                   2022.6.15                pypi_0    pypi
#charset-normalizer        2.1.1                    pypi_0    pypi
#cloudpickle               2.1.0              pyhd8ed1ab_0    conda-forge
#dcgp-python               1.5              py38h31c2246_1    conda-forge
#fire                      0.4.0                    pypi_0    pypi
#idna                      3.3                      pypi_0    pypi
#intel-openmp              2022.1.0          h57928b3_3787    conda-forge
#ipopt                     3.11.1                        2    conda-forge
#joblib                    1.1.0                    pypi_0    pypi
#libblas                   3.9.0                     8_mkl    conda-forge
#libcblas                  3.9.0                     8_mkl    conda-forge
#libflint                  2.6.3                hc326f10_0    conda-forge
#liblapack                 3.9.0                     8_mkl    conda-forge
#libsqlite                 3.39.2               h8ffe710_1    conda-forge
#libzlib                   1.2.12               h8ffe710_2    conda-forge
#m2w64-gcc-libgfortran     5.3.0                         6    conda-forge
#m2w64-gcc-libs            5.3.0                         7    conda-forge
#m2w64-gcc-libs-core       5.3.0                         7    conda-forge
#m2w64-gmp                 6.1.0                         2    conda-forge
#m2w64-libwinpthread-git   5.0.0.4634.697f757               2    conda-forge
#mkl                       2020.4             hb70f87d_311    conda-forge
#mpc                       1.2.1                h54e1faf_0    conda-forge
#mpfr                      4.1.0                h8d14728_1    conda-forge
#mpir                      3.0.0             he025d50_1002    conda-forge
#mpmath                    1.2.1                    pypi_0    pypi
#mppp                      0.20                 h93e08bc_2    conda-forge
#msys2-conda-epoch         20160418                      1    conda-forge
#networkx                  2.8.5              pyhd8ed1ab_0    conda-forge
#nlopt                     2.6.1            py38ha735ab1_2    conda-forge
#numpy                     1.23.2           py38h223ccf5_0    conda-forge
#obake                     0.6.0                h6b3e41e_0    conda-forge
#openssl                   1.1.1q               h8ffe710_0    conda-forge
#pagmo                     2.15.0               h16f1493_1    conda-forge
#pandas                    1.4.3                    pypi_0    pypi
#pip                       22.2.2             pyhd8ed1ab_0    conda-forge
#pthreads-win32            2.9.1                hfa6e2cd_3    conda-forge
#pyaudi                    1.8.1            py38h17917ce_0    conda-forge
#pygmo                     2.15.0           py38h89a189c_0    conda-forge
#python                    3.8.1                he1f5543_2    conda-forge
#python-box                6.0.2                    pypi_0    pypi
#python-dateutil           2.8.2                    pypi_0    pypi
#python_abi                3.8                      2_cp38    conda-forge
#pytz                      2022.2.1                 pypi_0    pypi
#pyyaml                    6.0                      pypi_0    pypi
#requests                  2.28.1                   pypi_0    pypi
#scikit-learn              1.1.2                    pypi_0    pypi
#scipy                     1.9.0            py38h91810f7_0    conda-forge
#setuptools                65.1.0           py38haa244fe_0    conda-forge
#six                       1.16.0                   pypi_0    pypi
#sqlite                    3.39.2               h8ffe710_1    conda-forge
#stdlib-list               0.8.0                    pypi_0    pypi
#symengine                 0.6.0                hc326f10_1    conda-forge
#sympy                     1.11.1                   pypi_0    pypi
#tbb                       2020.2               h2d74725_4    conda-forge
#termcolor                 1.1.0                    pypi_0    pypi
#threadpoolctl             3.1.0                    pypi_0    pypi
#ucrt                      10.0.20348.0         h57928b3_0    conda-forge
#urllib3                   1.26.11                  pypi_0    pypi
#utilmy                    0.1.16609156             pypi_0    pypi
#vc                        14.2                 hb210afc_6    conda-forge
#vs2015_runtime            14.29.30037          h902a5da_6    conda-forge
#wheel                     0.37.1             pyhd8ed1ab_0    conda-forge
#zstd                      1.5.2                h7755175_4    conda-forge
# pystan>=2.14 \







COPY pip_list.txt   /opt/work/
RUN pip  install -r /opt/work/pip_list.txt


# COPY bin/entrypoint.sh /usr/local/bin/
# COPY bin/vscode.sh /usr/local/bin/

#EXPOSE 8888
#VOLUME /notebooks
#WORKDIR /notebooks
ENTRYPOINT ["/bin/bash"]

# CMD /usr/spark/bin/spark-class org.apache.spark.deploy.master.Master









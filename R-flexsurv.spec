#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-flexsurv
Version  : 1.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/flexsurv_1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/flexsurv_1.1.tar.gz
Summary  : Flexible Parametric Survival and Multi-State Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-flexsurv-lib
Requires: R-Rcpp
Requires: R-deSolve
Requires: R-eha
Requires: R-mstate
Requires: R-muhaz
Requires: R-mvtnorm
Requires: R-quadprog
Requires: R-stringi
BuildRequires : R-Rcpp
BuildRequires : R-deSolve
BuildRequires : R-eha
BuildRequires : R-mstate
BuildRequires : R-muhaz
BuildRequires : R-mvtnorm
BuildRequires : R-quadprog
BuildRequires : R-stringi
BuildRequires : clr-R-helpers
BuildRequires : texlive

%description
including the Royston-Parmar spline model, generalized gamma and
    generalized F distributions.  Any user-defined parametric
    distribution can be fitted, given at least an R function defining
    the probability density or hazard. There are also tools for
    fitting and predicting from fully parametric multi-state models.

%package lib
Summary: lib components for the R-flexsurv package.
Group: Libraries

%description lib
lib components for the R-flexsurv package.


%prep
%setup -q -c -n flexsurv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530424710

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530424710
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flexsurv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flexsurv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flexsurv
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library flexsurv|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/flexsurv/CITATION
/usr/lib64/R/library/flexsurv/DESCRIPTION
/usr/lib64/R/library/flexsurv/INDEX
/usr/lib64/R/library/flexsurv/Meta/Rd.rds
/usr/lib64/R/library/flexsurv/Meta/data.rds
/usr/lib64/R/library/flexsurv/Meta/features.rds
/usr/lib64/R/library/flexsurv/Meta/hsearch.rds
/usr/lib64/R/library/flexsurv/Meta/links.rds
/usr/lib64/R/library/flexsurv/Meta/nsInfo.rds
/usr/lib64/R/library/flexsurv/Meta/package.rds
/usr/lib64/R/library/flexsurv/Meta/vignette.rds
/usr/lib64/R/library/flexsurv/NAMESPACE
/usr/lib64/R/library/flexsurv/NEWS
/usr/lib64/R/library/flexsurv/R/flexsurv
/usr/lib64/R/library/flexsurv/R/flexsurv.rdb
/usr/lib64/R/library/flexsurv/R/flexsurv.rdx
/usr/lib64/R/library/flexsurv/data/Rdata.rdb
/usr/lib64/R/library/flexsurv/data/Rdata.rds
/usr/lib64/R/library/flexsurv/data/Rdata.rdx
/usr/lib64/R/library/flexsurv/doc/flexsurv-examples.R
/usr/lib64/R/library/flexsurv/doc/flexsurv-examples.pdf
/usr/lib64/R/library/flexsurv/doc/flexsurv.R
/usr/lib64/R/library/flexsurv/doc/flexsurv.pdf
/usr/lib64/R/library/flexsurv/doc/index.html
/usr/lib64/R/library/flexsurv/help/AnIndex
/usr/lib64/R/library/flexsurv/help/aliases.rds
/usr/lib64/R/library/flexsurv/help/flexsurv.rdb
/usr/lib64/R/library/flexsurv/help/flexsurv.rdx
/usr/lib64/R/library/flexsurv/help/paths.rds
/usr/lib64/R/library/flexsurv/html/00Index.html
/usr/lib64/R/library/flexsurv/html/R.css
/usr/lib64/R/library/flexsurv/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/flexsurv/libs/flexsurv.so
/usr/lib64/R/library/flexsurv/libs/flexsurv.so.avx2
/usr/lib64/R/library/flexsurv/libs/flexsurv.so.avx512

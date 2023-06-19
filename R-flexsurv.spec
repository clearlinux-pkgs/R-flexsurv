#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-flexsurv
Version  : 2.2.2
Release  : 50
URL      : https://cran.r-project.org/src/contrib/flexsurv_2.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/flexsurv_2.2.2.tar.gz
Summary  : Flexible Parametric Survival and Multi-State Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-flexsurv-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-assertthat
Requires: R-deSolve
Requires: R-dplyr
Requires: R-generics
Requires: R-ggplot2
Requires: R-magrittr
Requires: R-mstate
Requires: R-muhaz
Requires: R-mvtnorm
Requires: R-numDeriv
Requires: R-purrr
Requires: R-quadprog
Requires: R-rlang
Requires: R-rstpm2
Requires: R-statmod
Requires: R-tibble
Requires: R-tidyr
Requires: R-tidyselect
BuildRequires : R-Rcpp
BuildRequires : R-assertthat
BuildRequires : R-deSolve
BuildRequires : R-dplyr
BuildRequires : R-generics
BuildRequires : R-ggplot2
BuildRequires : R-magrittr
BuildRequires : R-mstate
BuildRequires : R-muhaz
BuildRequires : R-mvtnorm
BuildRequires : R-numDeriv
BuildRequires : R-purrr
BuildRequires : R-quadprog
BuildRequires : R-rlang
BuildRequires : R-rstpm2
BuildRequires : R-statmod
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : buildreq-R

%description
including the Royston-Parmar spline model, generalized gamma and
    generalized F distributions.  Any user-defined parametric
    distribution can be fitted, given at least an R function defining
    the probability density or hazard. There are also tools for
    fitting and predicting from fully parametric multi-state models,
    based on either cause-specific hazards or mixture models.

%package lib
Summary: lib components for the R-flexsurv package.
Group: Libraries

%description lib
lib components for the R-flexsurv package.


%prep
%setup -q -n flexsurv
cd %{_builddir}/flexsurv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678819465

%install
export SOURCE_DATE_EPOCH=1678819465
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/flexsurv/doc/distributions.Rnw
/usr/lib64/R/library/flexsurv/doc/distributions.pdf
/usr/lib64/R/library/flexsurv/doc/flexsurv-examples.R
/usr/lib64/R/library/flexsurv/doc/flexsurv-examples.pdf
/usr/lib64/R/library/flexsurv/doc/flexsurv.R
/usr/lib64/R/library/flexsurv/doc/flexsurv.pdf
/usr/lib64/R/library/flexsurv/doc/index.html
/usr/lib64/R/library/flexsurv/doc/multistate.R
/usr/lib64/R/library/flexsurv/doc/multistate.Rnw
/usr/lib64/R/library/flexsurv/doc/multistate.pdf
/usr/lib64/R/library/flexsurv/doc/standsurv.R
/usr/lib64/R/library/flexsurv/doc/standsurv.Rmd
/usr/lib64/R/library/flexsurv/doc/standsurv.html
/usr/lib64/R/library/flexsurv/help/AnIndex
/usr/lib64/R/library/flexsurv/help/aliases.rds
/usr/lib64/R/library/flexsurv/help/flexsurv.rdb
/usr/lib64/R/library/flexsurv/help/flexsurv.rdx
/usr/lib64/R/library/flexsurv/help/paths.rds
/usr/lib64/R/library/flexsurv/html/00Index.html
/usr/lib64/R/library/flexsurv/html/R.css
/usr/lib64/R/library/flexsurv/tests/test_base.R
/usr/lib64/R/library/flexsurv/tests/testthat/simulate.R
/usr/lib64/R/library/flexsurv/tests/testthat/test-broom.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_custom.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_flexsurvmix.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_flexsurvreg.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_fmixmsm.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_fmsm.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_genf.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_genf_orig.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_gengamma.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_gengamma_orig.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_gompertz.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_llogis.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_mstate.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_outputs.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_predict.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_rtrunc.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_simulate.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_spline.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_splinedist.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_standsurv.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/flexsurv/libs/flexsurv.so
/usr/lib64/R/library/flexsurv/libs/flexsurv.so.avx2
/usr/lib64/R/library/flexsurv/libs/flexsurv.so.avx512

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-flexsurv
Version  : 2.3.2
Release  : 54
URL      : https://cran.r-project.org/src/contrib/flexsurv_2.3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/flexsurv_2.3.2.tar.gz
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
BuildRequires : R-covr
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
pushd ..
cp -a flexsurv buildavx2
popd
pushd ..
cp -a flexsurv buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724081753

%install
export SOURCE_DATE_EPOCH=1724081753
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/flexsurv/NEWS.md
/usr/lib64/R/library/flexsurv/R/flexsurv
/usr/lib64/R/library/flexsurv/R/flexsurv.rdb
/usr/lib64/R/library/flexsurv/R/flexsurv.rdx
/usr/lib64/R/library/flexsurv/data/Rdata.rdb
/usr/lib64/R/library/flexsurv/data/Rdata.rds
/usr/lib64/R/library/flexsurv/data/Rdata.rdx
/usr/lib64/R/library/flexsurv/doc/distributions.Rnw
/usr/lib64/R/library/flexsurv/doc/distributions.pdf
/usr/lib64/R/library/flexsurv/doc/flexsurv-examples.R
/usr/lib64/R/library/flexsurv/doc/flexsurv-examples.Rnw
/usr/lib64/R/library/flexsurv/doc/flexsurv-examples.pdf
/usr/lib64/R/library/flexsurv/doc/flexsurv.R
/usr/lib64/R/library/flexsurv/doc/flexsurv.Rnw
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
/usr/lib64/R/library/flexsurv/help/figures/flexsurv_hex.png
/usr/lib64/R/library/flexsurv/help/flexsurv.rdb
/usr/lib64/R/library/flexsurv/help/flexsurv.rdx
/usr/lib64/R/library/flexsurv/help/paths.rds
/usr/lib64/R/library/flexsurv/html/00Index.html
/usr/lib64/R/library/flexsurv/html/R.css
/usr/lib64/R/library/flexsurv/tests/test_base.R
/usr/lib64/R/library/flexsurv/tests/testthat/simulate.R
/usr/lib64/R/library/flexsurv/tests/testthat/test-broom.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_aic.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_contrasts.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_custom.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_flexsurvmix.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_flexsurvmix_opt.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_flexsurvreg.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_fmixmsm.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_fmixmsm_outputs.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_fmsm.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_genf.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_genf_orig.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_gengamma.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_gengamma_orig.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_gompertz.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_hess.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_llogis.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_mstate.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_outputs.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_predict.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_residuals.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_rtrunc.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_simulate.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_spline.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_splinedist.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_standsurv.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_survsplinek.R
/usr/lib64/R/library/flexsurv/tests/testthat/test_utils.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/flexsurv/libs/flexsurv.so
/V4/usr/lib64/R/library/flexsurv/libs/flexsurv.so
/usr/lib64/R/library/flexsurv/libs/flexsurv.so

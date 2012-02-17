%bcond_without bootstrap
%global packname  rgeos
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.2_2
Release:          1
Summary:          Interface to Geometry Engine - Open Source (GEOS)
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
Requires:         R-methods R-sp R-stringr 
%if %{with bootstrap}
Requires:         R-testthat R-plyr R-XML 
%else
Requires:         R-maptools R-testthat R-plyr R-XML 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-sp R-stringr
%if %{with bootstrap}
BuildRequires:    R-testthat R-plyr R-XML 
%else
BuildRequires:    R-maptools R-testthat R-plyr R-XML 
%endif
BuildRequires:    gdal
BuildRequires:    gdal-devel
BuildRequires:    proj

%description
Interface to Geometry Engine - Open Source (GEOS) using the C API for
topology operations on geometries.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/README*
%doc %{rlibdir}/%{packname}/SVN_VERSION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/poly-ex-gpc
%{rlibdir}/%{packname}/tests

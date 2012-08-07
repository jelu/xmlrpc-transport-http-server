%global subver 1

Name:           perl-XMLRPC-Transport-HTTP-Server
Version:        0.12
Release:        1%{?dist}
Summary:        xxx

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            https://github.com/jelu/xmlrpc-transport-http-server/
Source0:        xmlrpc-transport-http-server-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Needed for test
BuildRequires:  perl(Test::Simple)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
xxx


%prep
%setup -q -n xmlrpc-transport-http-server


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'


%check
# PERL_ANYEVENT_NET_TESTS shoudn't be set to avoid network tests
# on our builder.
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/XMLRPC*
%{_mandir}/man3/*.3*


%changelog
* Tue Aug 07 2012 Jerry Lundström < lundstrom.jerry at gmail.com > - 0.12-1
- Initial package for Fedora


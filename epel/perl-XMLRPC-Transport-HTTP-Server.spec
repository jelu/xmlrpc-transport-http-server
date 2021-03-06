Name:           perl-XMLRPC-Transport-HTTP-Server
Version:        0.14
Release:        1%{?dist}
Summary:        XMLRPC::Transport::HTTP::Server - XMLRPC::Lite HTTP Server

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            https://github.com/jelu/xmlrpc-transport-http-server/
Source0:        xmlrpc-transport-http-server-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(SOAP::Lite)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module extends the XMLRPC::Lite suite with a XMLRPC::Transport::HTTP::Server
which is just a SOAP::Transport::HTTP::Server with the XMLRPC::Server functions
for understanding the XMLRPC protocol.


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
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/XMLRPC*
%{_mandir}/man3/*.3*


%changelog
* Sun Aug 04 2013 Jerry Lundström < lundstrom.jerry at gmail.com > - 0.14-1
- New upsteam release.
  - Remove pod-coverage from MANIFEST also.
  - Rewrite Makefile.PL to better check ExtUtils::MakeMaker version and
    use BUILD_REQUIRES.

* Sun Aug 19 2012 Jerry Lundström < lundstrom.jerry at gmail.com > - 0.13-1
- New upsteam release.
  - Removed pod-coverage since it just fails, the 3 subs don't need
    individual documentation since its covered by XMLRPC::Server and
    XMLRPC::Transport::HTTP::CGI.
  - Added encoding to pod.

* Tue Aug 07 2012 Jerry Lundström < lundstrom.jerry at gmail.com > - 0.12-1
- Initial package for Fedora


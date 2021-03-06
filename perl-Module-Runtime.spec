#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Runtime
Summary:	Module::Runtime - runtime module handling
Summary(pl.UTF-8):	Module::Runtime - obsługa modułów w czasie działania
Name:		perl-Module-Runtime
Version:	0.016
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3d47222fa2e3dfcb4526f6cc8437b20
URL:		https://metacpan.org/release/Module-Runtime
BuildRequires:	perl-Module-Build
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.41}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The functions exported by this module deal with runtime handling of
Perl modules, which are normally handled at compile time.

%description -l pl.UTF-8
Ten moduł eksportuje funkcje pozwalające obsłużyć w czasie działania
programu moduły Perla, które są zwykle obsługiwane w czasie
kompilacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/Runtime.pm
%{_mandir}/man3/Module::Runtime.3pm*

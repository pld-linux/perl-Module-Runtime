#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Module
%define		pnam	Runtime
Summary:	Module::Runtime - runtime module handling
Summary(pl.UTF-8):	Module::Runtime - obsługa modułów w czasie działania
Name:		perl-Module-Runtime
Version:	0.018
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	455eedb62183b9d9e437c59c375c1054
URL:		https://metacpan.org/dist/Module-Runtime
BuildRequires:	perl-ExtUtils-MakeMaker
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Module/Runtime.pm
%{_mandir}/man3/Module::Runtime.3pm*

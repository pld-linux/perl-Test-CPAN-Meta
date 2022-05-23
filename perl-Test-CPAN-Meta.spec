#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	CPAN-Meta
Summary:	Test::CPAN::Meta - Validate your CPAN META.yml files
Summary(pl.UTF-8):	Test::CPAN::Meta - sprawdzanie poprawności plików CPAN META.yml
Name:		perl-Test-CPAN-Meta
Version:	0.25
Release:	1
License:	artistic_2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1582df35cc1e8875357702c687ed22f
URL:		https://metacpan.org/dist/Test-CPAN-Meta
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution was written to ensure that a META.yml file, provided
with a standard distribution uploaded to CPAN, meets the
specifications that are slowly being introduced to module uploads, via
the use of package makers and installers such as ExtUtils::MakeMaker,
Module::Build and Module::Install.

See CPAN::Meta for further details of the CPAN Meta Specification.

%description -l pl.UTF-8
Ten pakiet powstał, aby zapewnić, że plik META.yml, dostarczany ze
standardową dystrybucją przesyłaną do CPAN, jest zgodny ze
specyfikacją powoli wprowadzaną do przesyłania modułów, poprzez użycie
narzędzi do tworzenia i instalowania modułów, takich jak
ExtUtils::MakeMaker, Module::Build czy Module::Install.

Więcej szczegółów na temat CPAN Meta Specification można znaleźć w
CPAN::Meta.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%dir %{perl_vendorlib}/Test/CPAN
%{perl_vendorlib}/Test/CPAN/Meta.pm
%{perl_vendorlib}/Test/CPAN/Meta
%{_mandir}/man3/Test::CPAN::Meta*.3*
%{_examplesdir}/%{name}-%{version}

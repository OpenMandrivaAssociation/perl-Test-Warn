%define module  Test-Warn
%define name    perl-%{module}
%define version 0.08
%define release %mkrel 6

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl extension to test methods for warnings
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
Requires:       perl(Tree::DAG_Node)
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Array::Compare)
BuildRequires:  perl(Tree::DAG_Node)
BuildRequires:  perl(Test::Builder::Tester)
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
This module provides a few convenience methods for testing warning based code.

If you are not already familiar with the Test::More manpage now would be the
time to go take a look.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


%define upstream_name    Test-Warn
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl extension to test methods for warnings
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Array::Compare)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Tree::DAG_Node)
BuildRequires:  perl(Test::Exception)

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

Requires:       perl(Tree::DAG_Node)

%description 
This module provides a few convenience methods for testing warning based code.

If you are not already familiar with the Test::More manpage now would be the
time to go take a look.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

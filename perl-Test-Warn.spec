%define modname	Test-Warn

Summary:	Perl extension to test methods for warnings
Name:		perl-%{modname}
Version:	0.37
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::Warn
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl(Array::Compare)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Tree::DAG_Node)
BuildRequires:	perl(Test::Exception)
Requires:	perl(Tree::DAG_Node)

%description 
This module provides a few convenience methods for testing warning based code.

If you are not already familiar with the Test::More manpage now would be the
time to go take a look.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
%make test

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*

%define modname	Test-Warn
%define modver 0.32

Summary:	Perl extension to test methods for warnings
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*



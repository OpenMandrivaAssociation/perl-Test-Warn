%define upstream_name    Test-Warn
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl extension to test methods for warnings
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Array::Compare)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Tree::DAG_Node)
BuildRequires:	perl(Test::Exception)

Requires:	perl(Tree::DAG_Node)

BuildArch:	noarch

%description 
This module provides a few convenience methods for testing warning based code.

If you are not already familiar with the Test::More manpage now would be the
time to go take a look.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-3mdv2012.0
+ Revision: 765753
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1
+ Revision: 685640
- update to new version 0.23

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-3
+ Revision: 667393
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-2mdv2011.0
+ Revision: 609168
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 0.22

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 422888
- update to 0.21

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 405601
- rebuild using %%perl_convert_version

* Fri Jul 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 233691
- update to new version 0.11

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 224203
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdv2008.1
+ Revision: 180607
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
+ Revision: 47738
- update to new version 0.10


* Wed Jul 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2007.0
- spec cleanup
- rpmbuildupdate aware

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.08-5mdk
- fix deps

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.08-4mdk
- fix buildrequires in a backward compatible way

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.08-3mdk
- BuildRequires

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.08-2mdk 
- fix directory ownership (distlint)

* Mon Mar 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.08-1mdk
- first mdk release


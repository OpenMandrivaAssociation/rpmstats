Summary:	Gather statistics from installed packages
Name:		rpmstats
Version:	0.7
Release:	11
# maintained at http://svn.mandriva.com/viewvc/soft/rpm/rpmstats/
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Packaging
BuildRequires:	rpm-devel >= 5.0

%description
rpmstats retrieves statistics about installed packages.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

%files
%doc ChangeLog
%doc %{_mandir}/*/*
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}


%changelog
* Wed Nov 02 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.7-4
+ Revision: 712268
- rebuild against new rpm 5.4
- remove obsolete rpm stuff

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7-3
+ Revision: 669439
- mass rebuild
- rebuild

* Wed Nov 24 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.7-1mdv2011.0
+ Revision: 600807
- new release:
  	o refactorized and rewrite for native rpm5 api
  	o get rid of reports about missing files that we don't care about
  	o fix memleaks
  	o add signal handler so rpmstats can be interrupted by ie. Ctrl+C

* Tue Jan 05 2010 Pascal Terjan <pterjan@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 486313
- Fix memory corruption (#56176)

* Tue Sep 22 2009 Pascal Terjan <pterjan@mandriva.org> 0.6-1mdv2010.0
+ Revision: 447042
- 0.6

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new rpm

* Mon Jul 07 2008 Olivier Blin <blino@mandriva.org> 0.5.1-3mdv2009.0
+ Revision: 232565
- do not package debug files in main package

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-2mdv2009.0
+ Revision: 225334
- rebuild

* Tue Mar 04 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5-3mdv2008.1
+ Revision: 178770
- 0.5.1:
  	o better version detection
  	o rpm5.org support
- drop Prefix tag
- cosmetics

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun May 07 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5-3mdk
- rebuild for sparc

* Wed May 11 2005 Olivier Thauvin <nanardon@mandriva.org> 0.5-2mdk
- rebuild for rpm 4.4

* Thu Jan 27 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.5-1mdk
- don't manage menu files (bug #13209)

* Fri Jan 21 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.4.1-1mdk
- rebuild


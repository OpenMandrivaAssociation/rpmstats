Summary:	Gather statistics from installed packages
Name:		rpmstats
Version:	0.5.1
Release:	%mkrel 4
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Configuration/Packaging
BuildRequires:	rpm-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
rpmstats retrieves statistics about installed packages.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%doc %{_mandir}/*/*
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}

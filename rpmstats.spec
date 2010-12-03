Summary:	Gather statistics from installed packages
Name:		rpmstats
Version:	0.7
Release:	%mkrel 2
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

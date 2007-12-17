%define name rpmstats
%define version 0.5
%define release %mkrel 3

Summary: Gather statistics from installed packages
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Configuration/Packaging
BuildRequires:	rpm-devel
Prefix: %{_prefix}

%description
rpmstats retrieves statistics about installed packages.

%prep
%setup -q

%build
%configure2_5x
%make CPPFLAGS=-DRPM_42

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
%{_libdir}/*


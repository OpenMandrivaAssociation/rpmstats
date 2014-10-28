Summary:	Gather statistics from installed packages
Name:		rpmstats
Version:	0.7
Release:	14
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
%configure
%make

%install
%makeinstall

%files
%doc ChangeLog
%doc %{_mandir}/*/*
%{_bindir}/*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}


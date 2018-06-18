Summary:	Gather statistics from installed packages
Name:		rpmstats
Version:	0.7
Release:	19
# maintained at http://svn.mandriva.com/viewvc/soft/rpm/rpmstats/
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Packaging
Patch0:		rpm-4.6-adapt.patch
Patch1:		fix-bad-deref.patch
Patch2:		drop-old-rpm-support.patch
BuildRequires:	pkgconfig(rpm) >= 4.12.90

%description
rpmstats retrieves statistics about installed packages.

%prep
%setup -q
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc ChangeLog
%doc %{_mandir}/*/*
%{_bindir}/*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}

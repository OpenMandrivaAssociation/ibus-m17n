%define	version 1.2.0.20091217
%define	release %mkrel 1

Name:      ibus-m17n
Summary:   ibus - m17n engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: m17n-lib-devel m17n-db
BuildRequires: ibus-devel >= 1.2.0
Requires:	ibus >= 1.2.0
Requires:	m17n-lib

%description
ibus - M17N engine.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_libexecdir}/ibus-engine-*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml

Summary:	ibus - m17n engine
Name:		ibus-m17n
Version:	1.3.4
Release:	2
License:	GPLv2+
Group:		System/Internationalization
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	m17n-db
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(m17n-core)
Requires:	ibus
Requires:	m17n-lib
Requires(post,preun):	GConf2

%description
ibus - M17N engine.

%files -f %{name}.lang
%{_libexecdir}/ibus-*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}


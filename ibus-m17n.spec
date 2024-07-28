Summary:	ibus - m17n engine
Name:		ibus-m17n
Version:	1.4.31
Release:	1
License:	GPLv2+
Group:		System/Internationalization
URL:       https://github.com/ibus/ibus-m17n
Source0:   https://github.com/ibus/ibus-m17n/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	m17n-db
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(m17n-core)
BuildRequires:  pkgconfig(m17n-db)
BuildRequires:  gettext-devel
Requires:	ibus
Requires:	m17n-lib
Requires(post,preun):	GConf2

%description
ibus - M17N engine.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %name

%files -f %name.lang
%{_libexecdir}/ibus-*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml
%{_datadir}/applications/ibus-setup-m17n.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.m17n.gschema.xml
%{_datadir}/metainfo/m17n.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/ibus-m17n.png
%{_iconsdir}/hicolor/scalable/apps/ibus-m17n.svg

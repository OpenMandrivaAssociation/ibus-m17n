%define	version 1.3.2
%define	release %mkrel 3

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
BuildRequires: ibus-devel >= 1.3.9-5
BuildRequires: gtk+2-devel
Requires:	ibus >= 1.3.0
Requires:	m17n-lib
Requires(post,preun): GConf2

%description
ibus - M17N engine.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%post
%post_ibus_register_engine m17n:sr:kbd sr
%post_ibus_register_engine m17n:or:itrans or
%post_ibus_register_engine m17n:sv:post sv
%post_ibus_register_engine m17n:cmc:kbd cmc
%post_ibus_register_engine m17n:ka:kbd ka
%post_ibus_register_engine m17n:dv:phonetic dv
%post_ibus_register_engine m17n:he:kbd he
%post_ibus_register_engine m17n:kn:itrans kn
%post_ibus_register_engine m17n:ml:itrans ml
%post_ibus_register_engine m17n:te:itrans te
%post_ibus_register_engine m17n:en:ispell en
%post_ibus_register_engine m17n:si:samanala si
%post_ibus_register_engine m17n:si:wijesekera si
%post_ibus_register_engine m17n:ar:kbd ar
%post_ibus_register_engine m17n:da:post da
%post_ibus_register_engine m17n:grc:mizuochi grc
%post_ibus_register_engine m17n:kk:arabic kk
%post_ibus_register_engine m17n:kk:kbd kk
%post_ibus_register_engine m17n:fa:isiri fa
%post_ibus_register_engine m17n:ug:kbd ug
%post_ibus_register_engine m17n:ko:han2 ko
%post_ibus_register_engine m17n:ko:romaja ko
%post_ibus_register_engine m17n:el:kbd el
%post_ibus_register_engine m17n:ta:lk-renganathan ta
%post_ibus_register_engine m17n:ta:itrans ta
%post_ibus_register_engine m17n:am:sera am
%post_ibus_register_engine m17n:bn:unijoy bn
%post_ibus_register_engine m17n:bn:itrans bn
%post_ibus_register_engine m17n:gu:itrans gu
%post_ibus_register_engine m17n:sk:kbd sk
%post_ibus_register_engine m17n:pa:itrans pa
%post_ibus_register_engine m17n:sa:harvard-kyoto sa
%post_ibus_register_engine m17n:hr:kbd hr
%post_ibus_register_engine m17n:lo:lrt lo
%post_ibus_register_engine m17n:lo:kbd lo
%post_ibus_register_engine m17n:km:yannis km
%post_ibus_register_engine m17n:fr:azerty fr
%post_ibus_register_engine m17n:hi:itrans hi
%post_ibus_register_engine m17n:hi:typewriter hi
%post_ibus_register_engine m17n:my:kbd my
%post_ibus_register_engine m17n:bo:wylie bo
%post_ibus_register_engine m17n:bo:ewts bo
%post_ibus_register_engine m17n:bo:tcrc bo
%post_ibus_register_engine m17n:th:kesmanee th
%post_ibus_register_engine m17n:th:pattachote th
%post_ibus_register_engine m17n:th:tis820 th
%post_ibus_register_engine m17n:ru:yawerty ru
%post_ibus_register_engine m17n:ru:phonetic ru
%post_ibus_register_engine m17n:ru:kbd ru
%post_ibus_register_engine m17n:hy:kbd hy
%post_ibus_register_engine m17n:zh:pinyin zh
%post_ibus_register_engine m17n:zh:cangjie zh
%post_ibus_register_engine m17n:zh:bopomofo zh
%post_ibus_register_engine m17n:zh:quick zh
%post_ibus_register_engine m17n:zh:py zh
%post_ibus_register_engine m17n:zh:tonepy zh
%post_ibus_register_engine m17n:vi:viqr vi
%post_ibus_register_engine m17n:vi:telex vi
%post_ibus_register_engine m17n:vi:tcvn vi
%post_ibus_register_engine m17n:vi:vni vi
%post_ibus_register_engine m17n:ja:trycode ja
%post_ibus_register_engine m17n:ja:anthy ja
%post_ibus_register_engine m17n:ja:tcode ja
%post_ibus_register_engine m17n:as:itrans as

%preun
%preun_ibus_unregister_engine m17n:sr:kbd
%preun_ibus_unregister_engine m17n:or:itrans
%preun_ibus_unregister_engine m17n:sv:post
%preun_ibus_unregister_engine m17n:cmc:kbd
%preun_ibus_unregister_engine m17n:ka:kbd
%preun_ibus_unregister_engine m17n:dv:phonetic
%preun_ibus_unregister_engine m17n:he:kbd
%preun_ibus_unregister_engine m17n:kn:itrans
%preun_ibus_unregister_engine m17n:ml:itrans
%preun_ibus_unregister_engine m17n:te:itrans
%preun_ibus_unregister_engine m17n:en:ispell
%preun_ibus_unregister_engine m17n:si:samanala
%preun_ibus_unregister_engine m17n:si:wijesekera
%preun_ibus_unregister_engine m17n:ar:kbd
%preun_ibus_unregister_engine m17n:da:post
%preun_ibus_unregister_engine m17n:grc:mizuochi
%preun_ibus_unregister_engine m17n:kk:arabic
%preun_ibus_unregister_engine m17n:kk:kbd
%preun_ibus_unregister_engine m17n:fa:isiri
%preun_ibus_unregister_engine m17n:ug:kbd
%preun_ibus_unregister_engine m17n:ko:han2
%preun_ibus_unregister_engine m17n:ko:romaja
%preun_ibus_unregister_engine m17n:el:kbd
%preun_ibus_unregister_engine m17n:ta:lk-renganathan
%preun_ibus_unregister_engine m17n:ta:itrans
%preun_ibus_unregister_engine m17n:am:sera
%preun_ibus_unregister_engine m17n:bn:unijoy
%preun_ibus_unregister_engine m17n:bn:itrans
%preun_ibus_unregister_engine m17n:gu:itrans
%preun_ibus_unregister_engine m17n:sk:kbd
%preun_ibus_unregister_engine m17n:pa:itrans
%preun_ibus_unregister_engine m17n:sa:harvard-kyoto
%preun_ibus_unregister_engine m17n:hr:kbd
%preun_ibus_unregister_engine m17n:lo:lrt
%preun_ibus_unregister_engine m17n:lo:kbd
%preun_ibus_unregister_engine m17n:km:yannis
%preun_ibus_unregister_engine m17n:fr:azerty
%preun_ibus_unregister_engine m17n:hi:itrans
%preun_ibus_unregister_engine m17n:hi:typewriter
%preun_ibus_unregister_engine m17n:my:kbd
%preun_ibus_unregister_engine m17n:bo:wylie
%preun_ibus_unregister_engine m17n:bo:ewts
%preun_ibus_unregister_engine m17n:bo:tcrc
%preun_ibus_unregister_engine m17n:th:kesmanee
%preun_ibus_unregister_engine m17n:th:pattachote
%preun_ibus_unregister_engine m17n:th:tis820
%preun_ibus_unregister_engine m17n:ru:yawerty
%preun_ibus_unregister_engine m17n:ru:phonetic
%preun_ibus_unregister_engine m17n:ru:kbd
%preun_ibus_unregister_engine m17n:hy:kbd
%preun_ibus_unregister_engine m17n:zh:pinyin
%preun_ibus_unregister_engine m17n:zh:cangjie
%preun_ibus_unregister_engine m17n:zh:bopomofo
%preun_ibus_unregister_engine m17n:zh:quick
%preun_ibus_unregister_engine m17n:zh:py
%preun_ibus_unregister_engine m17n:zh:tonepy
%preun_ibus_unregister_engine m17n:vi:viqr
%preun_ibus_unregister_engine m17n:vi:telex
%preun_ibus_unregister_engine m17n:vi:tcvn
%preun_ibus_unregister_engine m17n:vi:vni
%preun_ibus_unregister_engine m17n:ja:trycode
%preun_ibus_unregister_engine m17n:ja:anthy
%preun_ibus_unregister_engine m17n:ja:tcode
%preun_ibus_unregister_engine m17n:as:itrans

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%{_libexecdir}/ibus-*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml

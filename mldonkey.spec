#
# Conditional build:
%bcond_without 	audiogalaxy	# without Audio Galaxy support
%bcond_without	opennap		# without Open Napster support
%bcond_without	limewire	# without Gnutella LimeWire support
%bcond_without	directconnect	# without Direct Connect support
%bcond_without	soulseek	# without Soulseek support
%bcond_without	openft	# without OpenFT support
%bcond_without	cymes	# without Cymes support
%bcond_without	donkey	# without eDonkey support
%bcond_without	gui	# without mlgui
#
Summary:	eDonkey 2000 p2p network client
Summary(pl.UTF-8):   Klient sieci p2p eDonkey 2000
Name:		mldonkey
%define	main_ver	2.5
%define	sub_ver		11
%define ocaml_ver	3.07
%define ocaml_rel	-1
Version:	%{main_ver}.%{sub_ver}
Release:	1
License:	GPL
Group:		Applications/Networking
#Source0:	http://cvs.berlios.de/cgi-bin/viewcvs.cgi/mldonkey/mldonkey/mldonkey.tar.gz?tarball=1
Source0:	http://savannah.nongnu.org/download/mldonkey/%{name}-%{main_ver}.%{sub_ver}.tar.gz
# Source0-md5:	7d88005f7a14354f02fb0bbee0ad4f51

Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.sh
Source4:	%{name}.png
Source5:	%{name}-gui.desktop
Patch0:		%{name}-configwin.patch
Patch1:		%{name}-newgtk.patch
URL:		http://www.nongnu.org/mldonkey/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel
BuildRequires:	ocaml-camlp4 >= %{ocaml_ver}%{ocaml_rel}
BuildRequires:	ocaml-lablgtk-devel >= 1:1.2.6
BuildRequires:	perl-base
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLDonkey is a door to the 'donkey' network, a decentralized network
used to exchange big files on the Internet. It is written in a
wonderful language, called Objective-Caml, and present most features
of the basic Windows donkey client, plus some more:
  - It should work on most UNIX-compatible platforms.
  - You can remotely command your client, either by telnet, on a WEB
    browser, or with the GTK interface.
  - You can connect to several servers, and each search will query all
    the connected servers.
  - You can select mp3s by bitrates in queries (useful ?).
  - You can select the name of a downloaded file before moving it to
    your incoming directory.
  - You can have several queries in the graphical user interface at the
    same time.
  - You can remember your old queries results in the command-line
    interface.
  - You can search in the history of all files you have seen on the
    network.

It can also access other peer-to-peer networks:
- Direct Connect
- Open Napster
- Gnutella LimeWire
- Soulseek
- Audio Galaxy
- OpenFT

%description -l pl.UTF-8
mldonkey jest nowym klientem do eDonkey 2000, zdecentralizowanej sieci
peer-to-peer bardzo wydajnej przy przesyłaniu dużych plików dzieki
protokołowi pobierania danych z wielu źródeł. Klient ten został
napisany w języku Objective-Caml i ma większość cech podstawowego
klienta windowsowego, a ponadto:
 - działa na większości platform uniksowych,
 - pozwala zdalnie sterować klientem przez interfejs telnet, WWW lub
   GTK,
 - można łączyć się z kilkoma serwerami, wtedy każde przeszukiwanie
   odpyta połączone serwery,
 - można wybierać pliki mp3 po bitrate w zapytaniach,
 - można wybierać nazwę pliku do ściągnięcia przed przejściem do
   katalogu incoming,
 - można jednocześnie wykonywać kilka zapytań w graficznym
   interfejsie,
 - można zapamiętać wyniki zapytań w interfejsie z linii poleceń,
 - można przeszukiwać historię wszystkich plików widzianych w sieci.

Klient umożliwia także dostęp do innych sieci peer-to-peer:
 - Direct Connect,
 - Open Napster,
 - Gnutella LimeWire,
 - Soulseek,
 - Audio Galaxy,
 - OpenFT.

%package gui
Summary:	Graphical frontend for mldonkey based on GTK
Summary(pl.UTF-8):   Graficzny interfejs użytkownika GTK dla mldonkey
Group:		X11/Applications/Networking

%description gui
The GTK interface for mldonkey provides a convenient way of managing
all mldonkey operations. It gives details about connected servers,
downloaded files, friends and lets one search for files in a pleasing
way.

%description gui -l pl.UTF-8
Interfejs użytkownika GTK dla mldonkey daje wygodny sposób zarządzania
wszystkimi operacjami mldonkey. Udostępnia szczegóły dotyczące
połączonych serwerów, ściąganych plików, znajomych oraz pozwala
wyszukiwać pliki w przyjemny sposób.

%package submit
Summary:	This tool gives you an easy way to add a ed2k-link
Summary(pl.UTF-8):   Narzędzie pozwalające łatwo dodać odnośniki ed2k
Group:		X11/Applications
Requires:	kdebase
Requires:	perl-libwww

%description submit
This tool gives you an easy way to add a ed2k-link (like
ed2k://|file|filename.exe|21352658|72b0b287cab7d875ccc1d89ebe910b9g|)
with a single click to your mldonkey download queue.

You need to edit /etc/sysconfig/mldonkey_submit.

%description submit -l pl.UTF-8
To narzędzie pozwala łatwo dodać odnośnik ed2k (w rodzaju
ed2k://|file|filename.exe|21352658|72b0b287cab7d875ccc1d89ebe910b9g|)
pojedynczym kliknięciem na kolejkę ściągania mldonkey.

Trzeba zmodyfikować plik /etc/sysconfig/mldonkey_submit.

%prep
%setup -q -n %{name}-%{main_ver}.%{sub_ver}
%patch0 -p1
%patch1 -p1

%build
# perl -pi -e 's|/etc/sysconfig/mldonkey|/etc/sysconfig/mldonkey_submit|' distrib/ed2k_submit/mldonkey_submit
cd config
%{__autoconf}
cd ..

%configure2_13 \
	--enable-ocamlver=%{ocaml_ver} \
	%{?!with_audiogalaxy:--disable-audiogalaxy} \
	%{?!with_opennap:--disable-opennap} \
	%{?!with_limewire:--disable-limewire} \
	%{?!with_directconnect:--disable-directconnect} \
	%{?!with_soulseek:--disable-soulseek} \
	%{?!with_openft:--disable-openft} \
	%{?!with_cymes:--disable-cymes} \
	%{?!with_donkey:--disable-donkey} \
	%{?!with_gui:--disable-gui}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/mldonkey,%{_initrddir},%{_sysconfdir}/sysconfig} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_datadir}/services}

# core
install mlnet $RPM_BUILD_ROOT%{_bindir}/mlnetd
install distrib/mldonkey_command $RPM_BUILD_ROOT%{_bindir}/mldonkey_command
install distrib/kill_mldonkey $RPM_BUILD_ROOT%{_bindir}/kill_mldonkey

%if %{with gui}
install mlgui $RPM_BUILD_ROOT%{_bindir}/mlgui
install mlnet+gui $RPM_BUILD_ROOT%{_bindir}/mlnet+gui
install mlguistarter $RPM_BUILD_ROOT%{_bindir}/mlguistarter
install mlchat $RPM_BUILD_ROOT%{_bindir}/mlchat
install distrib/mldonkey_previewer $RPM_BUILD_ROOT%{_bindir}/mldonkey_previewer
%endif

install distrib/ed2k_submit/mldonkey_submit $RPM_BUILD_ROOT%{_bindir}/mldonkey_submit
install distrib/ed2k_submit/mldonkey $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/mldonkey_submit
install distrib/ed2k_submit/ed2k.protocol $RPM_BUILD_ROOT%{_datadir}/services/ed2k.protocol

install %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/mldonkey
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/mldonkey
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/mlnet
%if %{with gui}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid mldonkey`" ]; then
	if [ "`getgid mldonkey`" != "33" ]; then
		echo "Error: group mldonkey doesn't have gid=33. Correct this before installing mldonkey." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 33 -r -f mldonkey
fi

if [ -n "`id -u mldonkey 2>/dev/null`" ]; then
	if [ "`id -u mldonkey`" != "47" ]; then
		echo "Error: user mldonkey doesn't have uid=47. Correct this before installing mldonkey." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -m -o -r -u 47 \
		-d /home/services/mldonkey -s /bin/sh -g mldonkey \
		-c "mldonkey" mldonkey 1>&2
fi

%post
/sbin/chkconfig --add mldonkey
if [ -f /var/lock/subsys/mldonkey ]; then
	/etc/rc.d/init.d/mldonkey restart >&2
else
	cd ~mldonkey
	mldonkeyd -exit > /dev/null 2>&1
	echo "Run \"/etc/rc.d/init.d/mldonkey start\" to start mldonkey." >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/mldonkey ]; then
		/etc/rc.d/init.d/mldonkey stop
	fi
	/sbin/chkconfig --del mldonkey
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel mldonkey
	/usr/sbin/groupdel mldonkey
fi

%files
%defattr(644,root,root,755)
%doc docs/* distrib/{Authors.txt,Bugs.txt,ChangeLog,directconnect.ini,ed2k_links.txt,FAQ.html,Todo.txt}
%config(noreplace) %{_sysconfdir}/sysconfig/mldonkey
%attr(754,root,root) %{_initrddir}/mldonkey
%attr(755,root,root) %{_bindir}/mlnetd
%attr(755,root,root) %{_bindir}/mlnet
%attr(755,root,root) %{_bindir}/mldonkey_command
%attr(755,root,root) %{_bindir}/kill_mldonkey

%if %{with gui}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mlchat
%attr(755,root,root) %{_bindir}/mlgui
%attr(755,root,root) %{_bindir}/mlnet+gui
%attr(755,root,root) %{_bindir}/mlguistarter
%attr(755,root,root) %{_bindir}/mldonkey_previewer
%{_pixmapsdir}/*
%{_desktopdir}/*
%endif

%files submit
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sysconfig/mldonkey_submit
%attr(755,root,root) %{_bindir}/mldonkey_submit
%{_datadir}/services/ed2k.protocol

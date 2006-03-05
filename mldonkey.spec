# TODO
#  - it creates file: .mldonkey/mlnet_strings.C
#  - mlnetd crashes on sparc (ca 15 minutes afrer start)
#
# Conditional build:
%bcond_without	audiogalaxy	# without Audio Galaxy support
%bcond_without	opennap		# without Open Napster support
%bcond_without	gnutella	# without Gnutella LimeWire support
%bcond_without	gnutella2	# without Gnutella2 support
%bcond_without	fasttrack	# without FastTrack support
%bcond_without	directconnect	# with Direct Connect support
%bcond_without	soulseek	# without Soulseek support
%bcond_with	openft		# without OpenFT support	(broken)
%bcond_without	cymes		# without Cymes support
%bcond_without	donkey		# without eDonkey support
%bcond_without	bittorrent	# without BitTorrent support
%bcond_without	filetp		# without fileTP support
%bcond_with	gui		# with mlgui

%ifarch alpha
%undefine with_gui
%endif

%define ocaml_ver	3.09.1
Summary:	eDonkey 2000 p2p network client
Summary(pl):	Klient sieci p2p eDonkey 2000
Name:		mldonkey
#%define patch_pack	c
%define real_ver	2.7.3
Version:	%{real_ver}
#Version:	%{real_ver}%{patch_pack}
Release:	1
License:	GPL
Group:		Applications/Networking
#Source0:	http://cvs.berlios.de/cgi-bin/viewcvs.cgi/mldonkey/mldonkey/mldonkey.tar.gz?tarball=1
#Source0:	http://savannah.nongnu.org/download/mldonkey/%{name}-%{version}.tar.gz
#Source0:	http://download.berlios.de/pub/mldonkey/spiralvoice/cvs/%{name}-%{real_ver}.tar.bz2
Source0:	http://savannah.nongnu.org/download/mldonkey/%{name}-%{version}.tar.bz2
# Source0-md5:	f6c7c183fda53a9e9c26a09f8cdefda7
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.sh
Source4:	%{name}.png
Source5:	%{name}-gui.desktop
Patch0:		%{name}-configwin.patch
Patch1:		%{name}-newgtk.patch
# PatchPack from http://download.berlios.de/pub/mldonkey/spiralvoice/patchpacks/
#PatchX:		%{name}-patch_pack30%{patch_pack}.gz
URL:		http://www.nongnu.org/mldonkey/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_gui:BuildRequires:	gtk+-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	ocaml-camlp4 >= 1:%{ocaml_ver}
%{?with_gui:BuildRequires:	ocaml-lablgtk-devel >= 1:1.2.6}
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	zlib-devel
Requires(post):	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(triggerpostun):	grep
Requires(triggerpostun):	sed >= 4.0
Requires:	nc
Requires:	procps
Requires:	rc-scripts >= 0.4.0.10
Requires:	wget
Provides:	group(mldonkey)
Provides:	user(mldonkey)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLDonkey is a door to the 'donkey' network, a decentralized network
used to exchange big files on the Internet. It is written in a
wonderful language, called Objective-Caml, and present most features
of the basic Windows donkey client, plus some more:
  - It should work on most UNIX-compatible platforms.
  - You can remotely command your client, either by telnet, on a WEB
    browser, or with the GTK+ interface.
  - You can connect to several servers, and each search will query all
    the connected servers.
  - You can select MP3s by bitrates in queries (useful ?).
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

%description -l pl
mldonkey jest nowym klientem do eDonkey 2000, zdecentralizowanej sieci
peer-to-peer bardzo wydajnej przy przesy³aniu du¿ych plików dziêki
protoko³owi pobierania danych z wielu ¼róde³. Klient ten zosta³
napisany w jêzyku Objective-Caml i ma wiêkszo¶æ cech podstawowego
klienta windowsowego, a ponadto:
 - dzia³a na wiêkszo¶ci platform uniksowych,
 - pozwala zdalnie sterowaæ klientem przez interfejs telnet, WWW lub
   GTK+,
 - mo¿na ³±czyæ siê z kilkoma serwerami, wtedy ka¿de przeszukiwanie
   odpyta po³±czone serwery,
 - mo¿na wybieraæ pliki MP3 po bitrate w zapytaniach,
 - mo¿na wybieraæ nazwê pliku do ¶ci±gniêcia przed przej¶ciem do
   katalogu incoming,
 - mo¿na jednocze¶nie wykonywaæ kilka zapytañ w graficznym interfejsie,
 - mo¿na zapamiêtaæ wyniki zapytañ w interfejsie z linii poleceñ,
 - mo¿na przeszukiwaæ historiê wszystkich plików widzianych w sieci.

Klient umo¿liwia tak¿e dostêp do innych sieci peer-to-peer:
 - Direct Connect,
 - Open Napster,
 - Gnutella LimeWire,
 - Soulseek,
 - Audio Galaxy,
 - OpenFT.

%package gui
Summary:	Graphical frontend for mldonkey based on GTK+
Summary(pl):	Graficzny interfejs u¿ytkownika GTK+ dla mldonkey
Group:		X11/Applications/Networking

%description gui
The GTK+ interface for mldonkey provides a convenient way of managing
all mldonkey operations. It gives details about connected servers,
downloaded files, friends and lets one search for files in a pleasing
way.

%description gui -l pl
Interfejs u¿ytkownika GTK+ dla mldonkey daje wygodny sposób
zarz±dzania wszystkimi operacjami mldonkey. Udostêpnia szczegó³y
dotycz±ce po³±czonych serwerów, ¶ci±ganych plików, znajomych oraz
pozwala wyszukiwaæ pliki w przyjemny sposób.

%package submit
Summary:	This tool gives you an easy way to add a ed2k-link
Summary(pl):	Narzêdzie pozwalaj±ce ³atwo dodaæ odno¶niki ed2k
Group:		X11/Applications
Requires:	kdelibs
Requires:	perl-libwww

%description submit
This tool gives you an easy way to add a ed2k-link (like
ed2k://|file|filename.exe|21352658|72b0b287cab7d875ccc1d89ebe910b9g|)
with a single click to your mldonkey download queue.

You need to edit /etc/sysconfig/mldonkey_submit.

%description submit -l pl
To narzêdzie pozwala ³atwo dodaæ odno¶nik ed2k (w rodzaju
ed2k://|file|filename.exe|21352658|72b0b287cab7d875ccc1d89ebe910b9g|)
pojedynczym klikniêciem na kolejkê ¶ci±gania mldonkey.

Trzeba zmodyfikowaæ plik /etc/sysconfig/mldonkey_submit.

%package utils
Summary:	Misc utils for mldonkey
Summary(pl):	Ró¿ne narzêdzia dla mldonkeya
Group:		Applications/Networking

%description utils
This package includes misc utils for mldonkey eg.: mld_hash,
make_torent, get_range, copysource, subconv, svg_converter.

%description utils -l pl
Ten pakiet zawiera nastêpuj±ce narzêdzia dla mldonkeya: mld_hash,
make_torent, get_range, copysource, subconv, svg_converter.

%prep
#%setup -q -n %{name}-%{real_ver}
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd config
%{__autoconf}
cd ..
cp -f /usr/share/automake/config.sub src/applets/kde/admin
cp -f /usr/share/automake/config.sub config

mkdir -p build
rm -f icons/big/*.ml_icon
rm -f icons/small/*.ml_icon
rm -f icons/*.ml_icon
rm -f *.cma *.cmxa *.a
rm -f mlgnut mlnap mlbt mldonkey mlslsk mldonkey_gui*
rm -f build/*.cma build/*.cmxa build/*.a
touch .depend
cd config
%configure \
	--enable-ocamlver=%{ocaml_ver} \
	--enable-pthread \
	%{?with_audiogalaxy:--en}%{!?with_audiogalaxy:--dis}able-audiogalaxy \
	%{?with_opennap:--en}%{!?with_opennap:--dis}able-opennap \
	%{?with_gnutella:--en}%{!?with_gnutella:--dis}able-gnutella \
	%{?with_gnutella2:--en}%{!?with_gnutella2:--dis}able-gnutella2 \
	%{?with_fasttrack:--en}%{!?with_fasttrack:--dis}able-fasttrack \
	%{?with_directconnect:--en}%{!?with_directconnect:--dis}able-directconnect \
	%{?with_soulseek:--en}%{!?with_soulseek:--dis}able-soulseek \
	%{?with_openft:--en}%{!?with_openft:--dis}able-openft \
	%{?with_cymes:--en}%{!?with_cymes:--dis}able-cymes \
	%{?with_donkey:--en}%{!?with_donkey:--dis}able-donkey \
	%{?with_bittorrent:--en}%{!?with_bittorrent:--dis}able-bittorrent \
	%{?with_filetp:--en}%{!?with_filetp:--dis}able-filetp \
	%{?with_gui:--en}%{!?with_gui:--dis}able-gui

cd ..
%{__make} opt utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/mldonkey,/etc/rc.d/init.d,/etc/sysconfig} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_datadir}/services,/var/log}

# core
install mlnet $RPM_BUILD_ROOT%{_sbindir}/mlnetd
install distrib/mldonkey_command $RPM_BUILD_ROOT%{_bindir}/mldonkey_command

%if %{with gui}
install mlgui $RPM_BUILD_ROOT%{_bindir}/mlgui
install mlnet+gui $RPM_BUILD_ROOT%{_bindir}/mlnet+gui
install mlguistarter $RPM_BUILD_ROOT%{_bindir}/mlguistarter
install mlchat $RPM_BUILD_ROOT%{_bindir}/mlchat
install mlim $RPM_BUILD_ROOT%{_bindir}/mlim
install mlprogress $RPM_BUILD_ROOT%{_bindir}/mlprogress
install distrib/mldonkey_previewer $RPM_BUILD_ROOT%{_bindir}/mldonkey_previewer
%endif

# util
install make_torrent $RPM_BUILD_ROOT%{_bindir}
install get_range $RPM_BUILD_ROOT%{_bindir}
install mld_hash $RPM_BUILD_ROOT%{_bindir}
install copysources $RPM_BUILD_ROOT%{_bindir}
install subconv $RPM_BUILD_ROOT%{_bindir}
install svg_converter $RPM_BUILD_ROOT%{_bindir}

install distrib/ed2k_submit/mldonkey_submit $RPM_BUILD_ROOT%{_bindir}/mldonkey_submit
install distrib/ed2k_submit/mldonkey $RPM_BUILD_ROOT/etc/sysconfig/mldonkey_submit
install distrib/ed2k_submit/ed2k.protocol $RPM_BUILD_ROOT%{_datadir}/services/ed2k.protocol

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/mldonkey
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/mldonkey
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/mlnet
%if %{with gui}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
%endif

> $RPM_BUILD_ROOT/var/log/mldonkey.log

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 33 mldonkey
%useradd -m -u 47 -d /home/services/mldonkey -s /bin/sh -g mldonkey -c "mldonkey" mldonkey

%post
if [ ! -f /var/log/mldonkey.log ]; then
	touch /var/log/mldonkey.log
	chmod 000 /var/log/mldonkey.log
	chown mldonkey:mldonkey /var/log/mldonkey.log
	chmod 640 /var/log/mldonkey.log
fi

/sbin/chkconfig --add mldonkey
%service mldonkey restart

%preun
if [ "$1" = "0" ]; then
	%service mldonkey stop
	/sbin/chkconfig --del mldonkey
fi

%postun
if [ "$1" = "0" ]; then
	%userremove mldonkey
	%groupremove mldonkey
fi

%triggerpostun -- mldonkey <= 2.5.22-2
if [ -f /etc/sysconfig/mldonkey ]; then
	sed -i -e 's@MLDONKEY_NICE@SERVICE_RUN_NICE_LEVEL@' /etc/sysconfig/mldonkey
fi

%triggerpostun -- mldonkey < 2.5.22-2.3
if [ -f /etc/sysconfig/mldonkey.rpmnew ]; then
	# new sysconfig, with lots of vars
	# we copy from old one just $SERVICE_RUN_NICE_LEVEL
	a=$(grep ^SERVICE_RUN_NICE_LEVEL /etc/sysconfig/mldonkey)
	if [ "$a" ]; then
		sed -i -e "s/^SERVICE_RUN_NICE_LEVEL.*/$a/" /etc/sysconfig/mldonkey.rpmnew
	fi
	cp -f /etc/sysconfig/mldonkey{,.rpmsave}
	mv -f /etc/sysconfig/mldonkey{.rpmnew,}
fi

%triggerpostun -- mldonkey < 2.5.28-0.4
chmod 640 /etc/sysconfig/mldonkey

%files
%defattr(644,root,root,755)
%doc docs/* distrib/{Authors.txt,Bugs.txt,ChangeLog,ed2k_links.txt,FAQ.html,Todo.txt}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/mldonkey
%attr(754,root,root) /etc/rc.d/init.d/mldonkey
%attr(755,root,root) %{_bindir}/mlnet
%attr(755,root,root) %{_bindir}/mldonkey_command
%attr(755,root,root) %{_sbindir}/mlnetd
%attr(640,mldonkey,mldonkey) %ghost /var/log/mldonkey.log

%if %{with gui}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mlchat
%attr(755,root,root) %{_bindir}/mlim
%attr(755,root,root) %{_bindir}/mlgui
%attr(755,root,root) %{_bindir}/mlprogress
%attr(755,root,root) %{_bindir}/mlnet+gui
%attr(755,root,root) %{_bindir}/mlguistarter
%attr(755,root,root) %{_bindir}/mldonkey_previewer
%{_pixmapsdir}/*
%{_desktopdir}/*
%endif

%files submit
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/mldonkey_submit
%attr(755,root,root) %{_bindir}/mldonkey_submit
%{_datadir}/services/ed2k.protocol

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/get_range
%attr(755,root,root) %{_bindir}/copysources
%attr(755,root,root) %{_bindir}/make_torrent
%attr(755,root,root) %{_bindir}/mld_hash
%attr(755,root,root) %{_bindir}/subconv
%attr(755,root,root) %{_bindir}/svg_converter

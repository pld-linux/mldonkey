#
# Conditional build:
# _without_audiogalaxy	- without Audio Galaxy support
# _without_opennap	- without Open Napster support
# _without_limewire	- without Gnutella LimeWire support
# _without_directconnect- without Direct Connect support
# _without_soulseek	- without Soulseek support
# _without_openft	- without OpenFT support
# _without_cymes	- without Cymes support
# _without_donkey	- without eDonkey support
#
Summary:	eDonkey 2000 p2p network client
Summary(pl):	Klient sieci p2p eDonkey 2000
Name:		mldonkey
Version:	2.02
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Networking
Source0:	http://savannah.nongnu.org/download/mldonkey/stable/%{name}-%{version}-0.sources.tar.gz
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.sh
Source4:	%{name}.png
Source5:	%{name}-gui.desktop
Source6:	%{name}-gui2.desktop
URL:		http://www.nongnu.org/mldonkey/
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel
BuildRequires:	lablgtk
BuildRequires:	perl
PreReq:		rc-scripts
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires:	ocaml
Requires:	ocaml-camlp4
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

%description -l pl
mldonkey jest nowym klientem do eDonkey 2000, zdecentralizowanej sieci
peer-to-peer bardzo wydajnej przy przesy³aniu du¿ych plików dzieki
protoko³owi pobierania danych z wielu ¼róde³. Klient ten zosta³
napisany w jêzyku Objective-Caml i ma wiêkszo¶æ cech podstawowego
klienta windowsowego, a ponadto:
 - dzia³a na wiêkszo¶ci platform uniksowych,
 - pozwala zdalnie sterowaæ klientem przez interfejs telnet, WWW lub
   GTK,
 - mo¿na ³±czyæ siê z kilkoma serwerami, wtedy ka¿de przeszukiwanie
   odpyta po³±czone serwery,
 - mo¿na wybieraæ pliki mp3 po bitrate w zapytaniach,
 - mo¿na wybieraæ nazwê pliku do ¶ci±gniêcia przed przej¶ciem do
   katalogu incoming,
 - mo¿na jednocze¶nie wykonywaæ kilka zapytañ w graficznym
   interfejsie,
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
Summary:	Graphical frontend for mldonkey based on GTK
Summary(pl):	Graficzny interfejs u¿ytkownika GTK dla mldonkey
Group:		X11/Applications/Networking
Requires:	gtk+
Requires:	lablgtk

%description gui
The GTK interface for mldonkey provides a convenient way of managing
all mldonkey operations. It gives details about connected servers,
downloaded files, friends and lets one search for files in a pleasing
way.

%description gui -l pl
Interfejs u¿ytkownika GTK dla mldonkey daje wygodny sposób zarz±dzania
wszystkimi operacjami mldonkey. Udostêpnia szczegó³y dotycz±ce
po³±czonych serwerów, ¶ci±ganych plików, znajomych oraz pozwala
wyszukiwaæ pliki w przyjemny sposób.

%package submit
Summary:	This tool gives you an easy way to add a ed2k-link
Summary(pl):	Narzêdzie pozwalaj±ce ³atwo dodaæ odno¶niki ed2k
Group:		X11/Applications
Requires:	kdebase
Requires:	perl-libwww-perl

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

%prep
%setup -q -n mldonkey

%build
perl -pi -e 's|/etc/sysconfig/mldonkey|/etc/sysconfig/mldonkey_submit|'  distrib/ed2k_submit/mldonkey_submit

%configure2_13 \
	%{?_without_audiogalaxy:--disable-audiogalaxy} \
	%{?_without_opennap:--disable-opennap} \
	%{?_without_limewire:--disable-limewire} \
	%{?_without_directconnect:--disable-directconnect} \
	%{?_without_soulseek:--disable-soulseek} \
	%{?_without_openft:--disable-openft} \
	%{?_without_cymes:--disable-cymes} \
	%{?_without_donkey:--disable-donkey}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/mldonkey
install -d $RPM_BUILD_ROOT%{_initrddir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/mldonkey
install mldonkey $RPM_BUILD_ROOT%{_bindir}/mldonkeyd
install use_tags $RPM_BUILD_ROOT%{_bindir}/use_tags
install distrib/mldonkey_command $RPM_BUILD_ROOT%{_bindir}/mldonkey_command
install distrib/kill_mldonkey $RPM_BUILD_ROOT%{_bindir}/kill_mldonkey
install %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/mldonkey
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/mldonkey

install mldonkey_gui $RPM_BUILD_ROOT%{_bindir}/mldonkey_gui
install mldonkey_gui2 $RPM_BUILD_ROOT%{_bindir}/mldonkey_gui2
install mldonkey_guistarter $RPM_BUILD_ROOT%{_bindir}/mldonkey_guistarter
install mlchat $RPM_BUILD_ROOT%{_bindir}/mlchat
install distrib/mldonkey_previewer $RPM_BUILD_ROOT%{_bindir}/mldonkey_previewer
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/
install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/
install %{SOURCE6} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/

install -d $RPM_BUILD_ROOT%{_datadir}/services
install distrib/ed2k_submit/mldonkey_submit $RPM_BUILD_ROOT%{_bindir}/mldonkey_submit
install distrib/ed2k_submit/mldonkey $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/mldonkey_submit
install distrib/ed2k_submit/ed2k.protocol  $RPM_BUILD_ROOT%{_datadir}/services/ed2k.protocol

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
        if [ "`id -u mysql`" != "47" ]; then
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/sysconfig/mldonkey
# isn't COPYING just GPL?
%doc COPYING docs/* distrib/AUTHORS distrib/BUGS distrib/ChangeLog distrib/Developers.txt distrib/directconnect.ini distrib/ed2k_links.txt distrib/FAQ.html distrib/Readme.txt distrib/TODO
%attr(754,root,root) %{_initrddir}/mldonkey
%attr(755,root,root) %{_bindir}/mldonkeyd
%attr(755,root,root) %{_bindir}/use_tags
%attr(755,root,root) %{_bindir}/mldonkey
%attr(755,root,root) %{_bindir}/mldonkey_command
%attr(755,root,root) %{_bindir}/kill_mldonkey

%files gui
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/mlchat
%attr(755,root,root) %{_bindir}/mldonkey_gui*
%attr(755,root,root) %{_bindir}/mldonkey_previewer
%attr(755,root,root) %{_pixmapsdir}/*
%attr(755,root,root) %{_applnkdir}/Network/Misc/*

%files submit
%defattr(644,root,root,755)
%doc COPYING
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sysconfig/mldonkey_submit
%attr(755,root,root) %{_bindir}/mldonkey_submit
%{_datadir}/services/ed2k.protocol

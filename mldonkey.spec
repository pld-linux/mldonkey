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
URL:		http://www.nongnu.org/mldonkey/
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel
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


It can also access other peer-to-peer networks :
- Direct Connect
- Open Napster
- Gnutella LimeWire
- Soulseek
- Audio Galaxy
- OpenFT

%description -l pl
mldonkey jest nowym klientem do eDonkey 2000, sieci peer-to-peer
bardzo wydajnej przy przesy�aniu du�ych plik�w dzieki protoko�owi
pobierania danych z wielu �r�de�. Klient ten zosta� napisany w j�zyku
Objective-Caml i jest dostarczany z interfejsami GTK, WWW i telnet.
Dzia�a na wi�kszo�ci plaform UNIXowych.

%package gui
Summary:	Graphical frontend for mldonkey based on GTK
Summary(pl):	Interfejs u�ytkownika GTK dla mldonkey
Group:		X11/Applications/Networking
Requires:	gtk+

%description gui
The GTK interface for mldonkey provides a convenient way of managing
all mldonkey operations. It gives details about conected servers,
downloaded files, friends and lets one search for files in a pleasing
way.

%description gui -l pl
Interfejs u�ytkownika GTK dla mldonkey.

%package submit
Summary:	This tool gives you an easy way to add a ed2k-link
Group:		X11/Applications
Requires:	kdebase
Requires:	perl-libwww-perl

%description submit
This tool gives you an easy way to add a ed2k-link (like
ed2k://|file|filename.exe|21352658|72b0b287cab7d875ccc1d89ebe910b9g|)
with a single click to your mldonkey download queue.

You need to edit /etc/sysconfig/mldonkey_submit

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

install -d $RPM_BUILD_ROOT%{_datadir}/services/
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

%files submit
%defattr(644,root,root,755)
%doc COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/mldonkey_submit
%attr(755,root,root) %{_bindir}/mldonkey_submit
%{_datadir}/services/ed2k.protocol

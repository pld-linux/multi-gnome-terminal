Summary:	The Enhanced GNOME Terminal
Summary(pl):	Ulepszony GNOME Terminal
Name:		multi-gnome-terminal
Version:	1.6.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/multignometerm/%{name}-%{version}.tar.bz2
# Source0-md5:	52b65d2326efc4273716383b0196e95f
Patch0:		%{name}-xterm-color.patch
Patch1:		%{name}-xterm-f1-f4.patch
Patch2:		%{name}-omf.patch
URL:		http://multignometerm.sf.net/
BuildRequires:	gdk-pixbuf-devel >= 0.18.0
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.18.0
BuildRequires:	gnome-libs-devel >= 1.4.1.4
BuildRequires:	libglade-gnome-devel >= 0.14
BuildRequires:	libxml-devel
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Multi Gnome Terminal is an enhanced version of gnome-terminal which
has the following features added:
- Many terminals in each window
- Switch between terminals using shortcuts
- Execution of user defined commands in new terminals (Customizable
  menus)
- Notification of terminals states using customizable colors for tabs
  text.

All these extensions are inspired by screen and konsole (the kde2
terminal) and are undoubtly very useful to each user.

%description -l pl
Multi Gnome Terminal jest wersj± standardowego GNOME Terminala
rozszerzon± o nowe mo¿liwo¶ci:
  - Kilka terminali w jednym oknie
  - Prze³±czanie pomiêdzy terminalami za pomoc± skrótów klawiszowych
  - Wykonywanie definiowanych przez u¿ytkownika komend w nowych
    terminalach
  - Powiadamianie o stanie terminali przy u¿yciu zmian kolorów zak³adek

Wszystkie te rozszerzenia s± inspirowane przez programy screen i
konsole (emulator terminala KDE2), i niew±tpliwie s± u¿yteczne dla
ka¿dego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="%{rpmcflags} -DREDHAT_TERM"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_applnkdir}/Terminals \
	omf_dest_dir=%{_omf_dest_dir}/mgt

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/mgt/multignometerm.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%{_sysconfdir}/CORBA/servers/multi-gnome-terminal.gnorba
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/mgt
%{_datadir}/gnome/help/*
%{_datadir}/idl/*
%{_omf_dest_dir}/mgt
%{_mandir}/man1/*
%{_applnkdir}/Terminals/*
%{_pixmapsdir}/*

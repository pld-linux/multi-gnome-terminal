Summary:	The Enhanced GNOME Terminal
Summary(pl):	Ulepszony GNOME Terminal
Name:		multi-gnome-terminal
Version:	1.3.13
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://multignometerm.sf.net/%{name}-%{version}.tar.bz2
Patch0:		%{name}-xterm-color.patch
URL:		http://multignometerm.sf.net/
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gnome-libs-devel >= 1.4.1.4
BuildRequires:	libglade-devel >= 0.14
BuildRequires:	libxml-devel
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
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
Multi Gnome Terminal jest wersj� standardowego GNOME Terminala
rozszerzon� o nowe mo�liwo�ci:
  - Kilka terminali w jednym oknie
  - Prze��czanie pomi�dzy terminalami za pomoc� skr�t�w klawiszowych
  - Wykonywanie definiowanych przez u�ytkownika komend w nowych
    terminalach
  - Powiadamianie o stanie terminali przy u�yciu zmian kolor�w zak�adek

Wszystkie te rozszerzenia s� inspirowane przez programy screen i
konsole (emulator terminala KDE2), i niew�tpliwie s� u�yteczne dla
ka�dego.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -DREDHAT_TERM"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_applnkdir}/Terminals \
	omf_dest_dir=%{_omf_dest_dir}/omf/mgt

gzip -9nf README NEWS AUTHORS

%find_lang %{name} --with-gnome

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/CORBA/servers/multi-gnome-terminal.gnorba
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/gnome-terminal
%{_datadir}/idl/*
%{_omf_dest_dir}/omf/mgt
%{_mandir}/man1/%{name}*
%{_applnkdir}/Terminals/*
%{_pixmapsdir}/*

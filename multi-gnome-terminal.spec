Summary:	The Enhanced GNOME Terminal
Summary(pl):	Ulepszony GNOME Terminal
Name:		multi-gnome-terminal
Version:	1.3.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://multignometerm.sf.net/%{name}-%{version}.tar.bz2
Patch0:		%{name}-xterm-color.patch
URL:		http://multignometerm.sf.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gnome-libs-devel >= 1.0.59
BuildRequires:	libxml-devel
BuildRequires:	scrollkeeper
BuildRequires:	libglade-devel >= 0.14

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/share/man

%description
Multi Gnome Terminal is an enhanced version of gnome-terminal which has
the following features added:
- Many terminals in each window
- Switch between terminals using shortcuts
- Execution of user defined commands in new terminals (Customizable menus)
- Notification of terminals states using customizable colors for tabs text.
 
All these extensions are inspired by screen and konsole (the kde2 terminal)
and are undoubtly very useful to each user.

%description -l pl
Multi Gnome Terminal jest wersj± standardowego GNOME Terminala
rozszerzon± o nowe mo¿liwo¶ci:
  - Kilka terminali w jednym oknie
  - Prze³±czanie pomiêdzy terminalami za pomoc± skrótów klawiszowych
  - Wykonywanie definiowanych przez u¿ytkownika komend w nowych terminalach
  - Powiadamianie o stanie terminali przy u¿yciu zmian kolorów zak³adek
 
Wszystkie te rozszerzenia s± inspirowane przez programy screen i konsole
(emulator terminala KDE2), i niew±tpliwie s± u¿yteczne dla ka¿dego.


%prep
%setup -q
%patch0 -p1

%build
%configure CFLAGS="%{rpmcflags} -DREDHAT_TERM"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT utildir=%{_applnkdir}/System

gzip -9nf README NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %{_sysconfdir}/CORBA/servers/multi-gnome-terminal.gnorba
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/gnome/help/multi-gnome-terminal
%{_datadir}/gnome/help/multi-gnome-terminal/*
%{_datadir}/gnome-terminal/glade/*glade
%{_datadir}/idl/*
%{_mandir}/man1/%{name}*
%{_datadir}/omf/mgt
%{_datadir}/pixmaps/mgt
%{_applnkdir}/System/*

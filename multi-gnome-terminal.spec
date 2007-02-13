Summary:	The Enhanced GNOME Terminal
Summary(pl.UTF-8):	Ulepszony GNOME Terminal
Name:		multi-gnome-terminal
Version:	1.6.2
Release:	5
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/multignometerm/%{name}-%{version}.tar.bz2
# Source0-md5:	52b65d2326efc4273716383b0196e95f
Patch0:		%{name}-xterm-f1-f4.patch
Patch1:		%{name}-omf.patch
Patch2:		%{name}-desktop.patch
URL:		http://multignometerm.sourceforge.net/
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

%description -l pl.UTF-8
Multi Gnome Terminal jest wersją standardowego GNOME Terminala
rozszerzoną o nowe możliwości:
  - Kilka terminali w jednym oknie
  - Przełączanie pomiędzy terminalami za pomocą skrótów klawiszowych
  - Wykonywanie definiowanych przez użytkownika komend w nowych
    terminalach
  - Powiadamianie o stanie terminali przy użyciu zmian kolorów zakładek

Wszystkie te rozszerzenia są inspirowane przez programy screen i
konsole (emulator terminala KDE2), i niewątpliwie są użyteczne dla
każdego.

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
	utildir=%{_desktopdir} \
	omf_dest_dir=%{_omf_dest_dir}/mgt

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/mgt/multignometerm.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%{_sysconfdir}/CORBA/servers
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/mgt
%{_datadir}/idl/*
%{_omf_dest_dir}/mgt
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

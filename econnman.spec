Summary:	EFL user interface for ConnMan
Name:		econnman
Version:	1.1
Release:	4
License:	LGPLv3+
Group:		Graphical desktop/Enlightenment
Url:		http://enlightenment.org/
Source:		http://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.gz
Patch:		econnman-1.1-desktop.patch
BuildRequires:	pkgconfig(edje)
Requires:	python-dbus
Requires:	python-efl
Requires:	connman
BuildArch:	noarch

%description
EFL user interface for ConnMan (Connection Manager).

%files
%doc README COPYING AUTHORS
%{_bindir}/*
%{_datadir}/econnman/
%{_datadir}/applications/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch -p1

%build
%configure
%make_build

%install
%make_install

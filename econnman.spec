Summary:	EFL user interface for ConnMan
Name:		econnman
Version:	1.1
Release:	5
License:	LGPLv3+
Group:		Graphical desktop/Enlightenment
Url:		https://enlightenment.org/
Source:		http://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
Patch:		econnman-1.1-desktop.patch
BuildRequires:	pkgconfig(edje)
BuildRequires:  efl
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
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

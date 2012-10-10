Name:		econnman
Version:	1
Release:	1
License:	GPLv2
Summary:	EFL user interface for ConnMan
Url:		http://enlightenment.org/
Group:		Graphical desktop/Enlightenment
# Actually, a repack - official release in tar.gz + few updates from SVN
Source:		http://packages.profusion.mobi/econnman/econnman-1.tar.bz2
Patch:		econnman-1-desktop.patch
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	evas
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(eweather)
BuildRequires:	pkgconfig(python-elementary)
BuildRequires:	pkgconfig(python-edbus)
BuildRequires:	pkgconfig(python-evas)
Requires:	python-ecore
Requires:	python-edje
Requires:	python-elementary
Requires:	python-evas
Requires:	python-e_dbus
Requires:	connman

%description
EFL user interface for ConnMan (Connection Manager).

%prep
%setup -q
%patch -p1

%build
autoreconf -ifv
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README COPYING AUTHORS
%{_bindir}/*
%{_datadir}/econnman
%{_datadir}/applications/*


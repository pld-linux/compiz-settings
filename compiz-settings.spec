Summary:	compiz configuration program
Name:		compiz-settings
Version:	0.07
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://compiz.biz/compiz-settings/%{name}_%{version}-2.tar.gz
# Source0-md5:	998b82327558fd1aef196601db9eec19
URL:		http://www.go-compiz.org/index.php?title=Compiz-Settings
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	compiz-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	compiz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
compiz configuration program with a SLAB style interface.

%prep
%setup -q -n compizsettings-trunk

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}

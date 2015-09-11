%define		kdeappsver	15.08.0
%define		qtver		5.3.2
%define		kaname		akonadi
Summary:	Akonadi - The PIM Storage Service
Name:		ka5-%{kaname}
Version:	15.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e6d025189fc54594c84ca52f2a478b62
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Akonadi is a personal information management (PIM) framework for KDE
Akonadi will function as an extensible data storage for all PIM
applications.

Besides data storage, Akonadi has several other components including
search, and a library (cache) for easy access and notification of data
changes.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_agent_launcher
%attr(755,root,root) %{_bindir}/akonadi_agent_server
%attr(755,root,root) %{_bindir}/akonadi_control
%attr(755,root,root) %{_bindir}/akonadi_rds
%attr(755,root,root) %{_bindir}/akonadictl
%attr(755,root,root) %{_bindir}/akonadiserver
%attr(755,root,root) %{_bindir}/asapcat
/etc/xdg/akonadi.categories
%dir /etc/xdg/akonadi
/etc/xdg/akonadi/mysql-global-mobile.conf
/etc/xdg/akonadi/mysql-global.conf
%attr(755,root,root) %ghost %{_libdir}/libKF5AkonadiPrivate.so.5
%attr(755,root,root) %{_libdir}/libKF5AkonadiPrivate.so.*.*.*
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite3.so
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/akonadi
%{_libdir}/cmake/KF5AkonadiServer
%attr(755,root,root) %{_libdir}/libKF5AkonadiPrivate.so

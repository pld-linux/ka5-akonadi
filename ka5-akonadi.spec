%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		akonadi
Summary:	Akonadi - The PIM Storage Service
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2c149449afbdb5315ed378055e2a0954
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
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

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
install -d $RPM_BUILD_ROOT%{_includedir}/KF5/Akonadi

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
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
/etc/xdg/akonadi.renamecategories
%attr(755,root,root) %{_bindir}/akonadi2xml
%attr(755,root,root) %{_bindir}/akonadi_knut_resource
%attr(755,root,root) %{_bindir}/akonadiselftest
%attr(755,root,root) %{_bindir}/akonaditest
%attr(755,root,root) %ghost %{_libdir}/libKF5AkonadiAgentBase.so.5
%attr(755,root,root) %{_libdir}/libKF5AkonadiAgentBase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5AkonadiCore.so.5
%attr(755,root,root) %{_libdir}/libKF5AkonadiCore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5AkonadiWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5AkonadiWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5AkonadiXml.so.5
%attr(755,root,root) %{_libdir}/libKF5AkonadiXml.so.*.*.*
%dir %{_libdir}/qt5/plugins/akonadi
%{_libdir}/qt5/plugins/akonadi/akonadi_test_searchplugin.so
%{_libdir}/qt5/plugins/designer/akonadi5widgets.so
%dir %{_datadir}/akonadi
%dir %{_datadir}/akonadi/agents
%{_datadir}/akonadi/agents/knutresource.desktop
%{_datadir}/config.kcfg/resourcebase.kcfg
%{_iconsdir}/hicolor/128x128/apps/akonadi.png
%{_iconsdir}/hicolor/16x16/apps/akonadi.png
%{_iconsdir}/hicolor/22x22/apps/akonadi.png
%{_iconsdir}/hicolor/256x256/apps/akonadi.png
%{_iconsdir}/hicolor/32x32/apps/akonadi.png
%{_iconsdir}/hicolor/48x48/apps/akonadi.png
%{_iconsdir}/hicolor/64x64/apps/akonadi.png
%{_iconsdir}/hicolor/scalable/apps/akonadi.svgz
%dir %{_datadir}/kf5/akonadi
%{_datadir}/kf5/akonadi/akonadi-xml.xsd
%{_datadir}/kf5/akonadi/kcfg2dbus.xsl
%dir %{_datadir}/kf5/akonadi_knut_resource
%{_datadir}/kf5/akonadi_knut_resource/knut-template.xml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/akonadi
%{_includedir}/KF5/Akonadi
%{_includedir}/KF5/AkonadiAgentBase
%{_includedir}/KF5/AkonadiCore
%{_includedir}/KF5/AkonadiWidgets
%{_includedir}/KF5/AkonadiXml
%{_includedir}/KF5/akonadi_version.h
%{_libdir}/cmake/KF5Akonadi
%attr(755,root,root) %{_libdir}/libKF5AkonadiPrivate.so
%{_libdir}/libKF5AkonadiAgentBase.so
%{_libdir}/libKF5AkonadiCore.so
%{_libdir}/libKF5AkonadiWidgets.so
%{_libdir}/libKF5AkonadiXml.so
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiAgentBase.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiCore.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiWidgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiXml.pri

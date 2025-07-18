#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kfver		5.53.0
%define		qtver		5.15.2
%define		kaname		akonadi
Summary:	Akonadi - The PIM Storage Service
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	884c64e59f226d4341b074e5069e994c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Designer-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5UiTools-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka5-kaccounts-integration-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kfver}
BuildRequires:	kf5-kcompletion-devel >= %{kfver}
BuildRequires:	kf5-kconfig-devel >= %{kfver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kfver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kfver}
BuildRequires:	kf5-kcrash-devel >= %{kfver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kfver}
BuildRequires:	kf5-kdesignerplugin-devel >= %{kfver}
BuildRequires:	kf5-ki18n-devel >= %{kfver}
BuildRequires:	kf5-kiconthemes-devel >= %{kfver}
BuildRequires:	kf5-kio-devel >= %{kfver}
BuildRequires:	kf5-kitemmodels-devel >= %{kfver}
BuildRequires:	kf5-kitemviews-devel >= %{kfver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kfver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kfver}
BuildRequires:	kf5-kxmlgui-devel >= %{kfver}
BuildRequires:	libaccounts-qt5-devel >= 1.16
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Conflicts:	akonadi-libs >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Akonadi is a personal information management (PIM) framework for KDE
Akonadi will function as an extensible data storage for all PIM
applications.

Besides data storage, Akonadi has several other components including
search, and a library (cache) for easy access and notification of data
changes.

%description -l pl.UTF-8
Akonadi jest szkieletem zarządzania informacjami osobistymi (PIM) dla
KDE. Będzie on funkcjonował jako rozszerzalny magazyn danych dla
wszystkich aplikacji PIM.

Oprócz magazynu danych, Akonadi ma wiele innych komponentów, między
innymi przeszukiwanie i bibliotekę (buforowanie) dla łatwego
dostępu i powiadomieniach o zmianach danych.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%package apparmor
Summary:	Files for apparmor
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description apparmor
Files for apparmor.


%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
install -d $RPM_BUILD_ROOT%{_includedir}/KF5/Akonadi
install -d $RPM_BUILD_ROOT%{_libdir}/qt5/plugins/pim5/kontact
install -d $RPM_BUILD_ROOT%{_libdir}/qt5/plugins/pim5/kcms
install -d $RPM_BUILD_ROOT%{_libdir}/qt5/qml/org/kde/akonadi

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
%dir /etc/xdg/akonadi
/etc/xdg/akonadi/mysql-global-mobile.conf
/etc/xdg/akonadi/mysql-global.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml
%attr(755,root,root) %{_bindir}/akonadi2xml
%attr(755,root,root) %{_bindir}/akonadi_knut_resource
%attr(755,root,root) %{_bindir}/akonadiselftest
%attr(755,root,root) %{_bindir}/akonaditest
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
%{_datadir}/qlogging-categories5/akonadi.categories
%{_datadir}/qlogging-categories5/akonadi.renamecategories
%dir %{_libdir}/qt5/plugins/pim5
%dir %{_libdir}/qt5/plugins/pim5/akonadi
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/akonadi_test_searchplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kontact
%ghost %{_libdir}/libKPim5AkonadiAgentBase.so.5
%attr(755,root,root) %{_libdir}/libKPim5AkonadiAgentBase.so.5.*.*
%ghost %{_libdir}/libKPim5AkonadiCore.so.5
%attr(755,root,root) %{_libdir}/libKPim5AkonadiCore.so.5.*.*
%ghost %{_libdir}/libKPim5AkonadiPrivate.so.5
%attr(755,root,root) %{_libdir}/libKPim5AkonadiPrivate.so.5.*.*
%ghost %{_libdir}/libKPim5AkonadiWidgets.so.5
%attr(755,root,root) %{_libdir}/libKPim5AkonadiWidgets.so.5.*.*
%ghost %{_libdir}/libKPim5AkonadiXml.so.5
%attr(755,root,root) %{_libdir}/libKPim5AkonadiXml.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/akonadi5widgets.so
%dir %{_libdir}/qt5/plugins/pim5/kcms
%dir %{_libdir}/qt5/qml/org/kde/akonadi

# TODO subpackage
%{_datadir}/kdevappwizard/templates/akonadiresource.tar.bz2
%{_datadir}/kdevappwizard/templates/akonadiserializer.tar.bz2

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Akonadi
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/Akonadi
%{_includedir}/KPim5/AkonadiAgentBase
%{_includedir}/KPim5/AkonadiCore
%{_includedir}/KPim5/AkonadiWidgets
%{_includedir}/KPim5/AkonadiXml
%{_libdir}/cmake/KF5Akonadi
%{_libdir}/cmake/KPim5Akonadi
%{_libdir}/libKPim5AkonadiAgentBase.so
%{_libdir}/libKPim5AkonadiCore.so
%{_libdir}/libKPim5AkonadiPrivate.so
%{_libdir}/libKPim5AkonadiWidgets.so
%{_libdir}/libKPim5AkonadiXml.so
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiAgentBase.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiCore.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiWidgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiXml.pri

%files apparmor
%defattr(644,root,root,755)
/etc/apparmor.d/mariadbd_akonadi
/etc/apparmor.d/mysqld_akonadi
/etc/apparmor.d/postgresql_akonadi
/etc/apparmor.d%{_prefix}.bin.akonadiserver


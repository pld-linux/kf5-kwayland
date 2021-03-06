%define		kdeframever	5.79
%define		qtver		5.9.0
%define		kfname		kwayland

Summary:	Framework for managing menu and toolbar actions
Name:		kf5-%{kfname}
Version:	5.79.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	9d221f6fc2f4d704fa115b59275218fd
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5WaylandClient-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	plasma-wayland-protocols-devel >= 1.1.1
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.7.0
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
kwayland

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/qlogging-categories5/kwayland.categories
%attr(755,root,root) %ghost %{_libdir}/libKF5WaylandClient.so.5
%attr(755,root,root) %{_libdir}/libKF5WaylandClient.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5WaylandServer.so.5
%attr(755,root,root) %{_libdir}/libKF5WaylandServer.so.5.*.*
%attr(755,root,root) %{_prefix}/libexec/org-kde-kf5-kwayland-testserver
%{_datadir}/qlogging-categories5/kwayland.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KWayland
%{_includedir}/KF5/kwayland_version.h
%{_libdir}/cmake/KF5Wayland
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandServer.pri
%attr(755,root,root) %{_libdir}/libKF5WaylandClient.so
%attr(755,root,root) %{_libdir}/libKF5WaylandServer.so

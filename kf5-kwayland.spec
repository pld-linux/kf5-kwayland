#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.97
%define		qtver		5.15.2
%define		kfname		kwayland

Summary:	Framework for managing menu and toolbar actions
Name:		kf5-%{kfname}
Version:	5.97.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	c0943e04bb7f514c58bcb9b891efb080
URL:		http://www.kde.org/
BuildRequires:	EGL-devel
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5WaylandClient-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-plasma-wayland-protocols-devel >= 1.4.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.15
BuildRequires:	wayland-protocols >= 1.15
BuildRequires:	xz
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	kf5-dirs
Requires:	wayland >= 1.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kwayland

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Gui-devel >= %{qtver}

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
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


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
%ghost %{_libdir}/libKF5WaylandClient.so.5
%attr(755,root,root) %{_libdir}/libKF5WaylandClient.so.5.*.*
%ghost %{_libdir}/libKF5WaylandServer.so.5
%attr(755,root,root) %{_libdir}/libKF5WaylandServer.so.5.*.*
%attr(755,root,root) %{_prefix}/libexec/org-kde-kf5-kwayland-testserver
%{_datadir}/qlogging-categories5/kwayland.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KWayland
%{_libdir}/cmake/KF5Wayland
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandServer.pri
%{_libdir}/libKF5WaylandClient.so
%{_libdir}/libKF5WaylandServer.so
%{_pkgconfigdir}/KF5WaylandClient.pc

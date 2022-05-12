#
# Conditional build:
%bcond_without	doc	# Rocumentation

%define		orgname		qtimageformats
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 Image Formats plugins
Summary(pl.UTF-8):	Wtyczki Qt5 Image Formats
Name:		qt5-%{orgname}
Version:	5.15.4
Release:	1
License:	LGPL v3 or GPL v2 or GPL v3 or commercial
Group:		X11/Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	feeb68abd2c997f8e08cae1908b44edb
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	jasper-devel >= 1.900.1
BuildRequires:	libmng-devel >= 1.0.9
BuildRequires:	libtiff-devel
BuildRequires:	libwebp-devel >= 0.4.3
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Image Formats plugins for Qt5Gui library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera wtyczki Qt5 Image Formats dla biblioteki Qt5Gui.

%package -n Qt5Gui-imageformats
Summary:	Qt5 Image Formats plugins for Qt5Gui library
Summary(pl.UTF-8):	Wtyczki Qt5 Image Formats dla biblioteki Qt5Gui
Group:		X11/Libraries
Requires:	jasper-libs >= 1.900.1
Requires:	libmng >= 1.0.9
Requires:	libwebp >= 0.4.3
Obsoletes:	qt5-qtimageformats < 5.3.0
Obsoletes:	qt5-qtimageformats-devel < 5.3.0

%description -n Qt5Gui-imageformats
This package contains Qt5Gui Image Formats plugins that support the
following formats:
%{?with_disabled:- DDS (Direct Draw Surface)}
- ICNS (Apple Icon Image)
- JP2 (JPEG2000; Joint Photographic Experts Group 2000)
- MNG (Multiple-image Network Graphics)
- TGA (Truevision Graphics Adapter)
- TIFF (Tagged Image File Format)
- WBMP (Wireless Bitmap)
- WEBP (WebP)

%description -n Qt5Gui-imageformats -l pl.UTF-8
Ten pakiet zawiera wtyczki Image Formats dla biblioteki Qt5Gui,
obsługujące następujące formaty:
%{?with_disabled:- DDS (Direct Draw Surface)}
- ICNS (Apple Icon Image)
- JP2 (JPEG2000; Joint Photographic Experts Group 2000)
- MNG (Multiple-image Network Graphics)
- TGA (Truevision Graphics Adapter)
- TIFF (Tagged Image File Format)
- WBMP (Wireless Bitmap)
- WEBP (WebP)

%package doc
Summary:	Qt5 Image Formats documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do wtyczek Qt5 Image Formats w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 Image Formats documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do wtyczek Qt5 Image Formats w formacie HTML.

%package doc-qch
Summary:	Qt5 Image Formats documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do wtyczek Qt5 Image Formats w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 Image Formats documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do wtyczek Qt5 Image Formats w formacie QCH.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
%{qmake_qt5}
%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n Qt5Gui-imageformats
%defattr(644,root,root,755)
%doc dist/changes-*
# module disabled in src/plugins/imageformats/imageformats.pro
#%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqdds.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqicns.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqjp2.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqmng.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqtga.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqtiff.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqwbmp.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/libqwebp.so
#%{_libdir}/cmake/Qt5Gui/Qt5Gui_QDDSPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QJp2Plugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QMngPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtimageformats

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtimageformats.qch
%endif

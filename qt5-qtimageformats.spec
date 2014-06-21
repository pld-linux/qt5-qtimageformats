# TODO:
# - cleanup
#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtimageformats
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 Image Formats plugins
Summary(pl.UTF-8):	Wtyczki Qt5 Image Formats
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	fe9898272b3952e3d97eacbaca484b55
URL:		http://qt-project.org/
BuildRequires:	libmng-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt5-qtbase-devel >= %{qtbase_ver}
BuildRequires:	qt5-qttools-devel >= %{qttools_ver}
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Image Formats plugins.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera wtyczki Qt5 Image Formats.

%package devel
Summary:	The Qt5 Image Formats - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Qt5 Image Formats - development files.

%package doc
Summary:	Qt5 Image Formats documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do wtyczek Qt5 Image Formats w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Image Formats documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do wtyczek Qt5 Image Formats w formacie HTML.

%package doc-qch
Summary:	Qt5 Image Formats documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do wtyczek Qt5 Image Formats w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Image Formats documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do wtyczek Qt5 Image Formats w formacie QCH.

%package examples
Summary:	Qt5 Image Formats examples
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Formats - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{qt5dir}/plugins/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/Qt5Gui/*.cmake

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtimageformats

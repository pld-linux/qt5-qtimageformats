# TODO:
# - cleanup

%define		orgname		qtimageformats
Summary:	The Qt5 Image Formats
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
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	qt5-qttools-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
Qt5 Image Formats libraries.

%package devel
Summary:	The Qt5 Image Formats - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Qt5 Image Formats - development files.

%package doc
Summary:	The Qt5 Image Formats - docs
Group:		Documentation

%description doc
Qt5 Image Formats - documentation.

%package examples
Summary:	Qt5 Image Formats examples
Group:		X11/Development/Libraries

%description examples
Qt5 Formats - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_qtdir}/plugins

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/Qt5Gui

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc

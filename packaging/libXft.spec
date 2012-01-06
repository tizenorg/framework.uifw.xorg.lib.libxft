
Name:       libXft
Summary:    X.Org X11 libXft runtime library
Version:    2.2.0
Release:    1.4
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Patch1:     100-libXft-2.1.10-lcd-filter-3.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xorg-macros)


%description
Xft is a library that connects X applications with the FreeType font rasterization
library. 



%package devel
Summary:    Development components for the libXft library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
xft Development Librariy files 



%prep
%setup -q -n %{name}-%{version}

# 100-libXft-2.1.10-lcd-filter-3.patch
%patch1 -p1

%build

%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXft.so.2
%{_libdir}/libXft.so.2.2.0


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%doc %{_mandir}/man3/Xft.3*


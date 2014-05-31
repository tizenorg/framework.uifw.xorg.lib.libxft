Summary: X.Org X11 libXft runtime library
Name: libXft
Version: 2.3.1
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires: pkgconfig(xrender)
BuildRequires: freetype-devel >= 2.1.9-2
BuildRequires: fontconfig-devel >= 2.2-1

Requires: fontconfig >= 2.2-1

%description
X.Org X11 libXft runtime library

%package devel
Summary: X.Org X11 libXft development package
Group: Development/Libraries
Provides: libxft-devel
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXft development package

%prep
%setup -q

%build

%reconfigure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: There's no real good reason to ship these anymore, as pkg-config
# is the official way to detect flags, etc. now.
rm -f $RPM_BUILD_ROOT%{_bindir}/xft-config
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/xft-config*

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXft.so.2*

%files devel
%defattr(-,root,root,-)
#%{_bindir}/xft-config
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
#%{_mandir}/man1/xft-config.1.gz
#%dir %{_mandir}/man3x
#%{_mandir}/man3/Xft.3*


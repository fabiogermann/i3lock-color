Name: i3lock-color
Version: 2.12.c
Release: 1%{?dist}
Summary: improved improved screen locker - "the ricing fork of i3lock"

License: BSD
URL: https://github.com/PandorasFox/i3lock-color

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

BuildRequires: git
BuildRequires: cairo-devel libev libev-devel libjpeg-turbo pam-devel xcb-util-devel xcb-util-image xcb-util-image-devel
BuildRequires: autoconf automake make gcc-c++

Provides:  i3lock-color
Obsoletes: i3lock

%description
i3lock is a simple screen locker like slock. After starting it, you will see a white screen (you can configure the color/an image). You can return to your screen by entering your password.

%prep
# none

%build
autoreconf --force --install
mkdir -p build
cd build
../configure --prefix %{_prefix} --sysconfdir=%{_sysconfdir} --disable-sanitizers
make -j

%install
cd build
%make_install

%check

%files
%{_bindir}/i3lock
%{_mandir}/man1/i3lock.1.*
%{_sysconfdir}/pam.d/i3lock

%doc README.md i3lock.1 CHANGELOG

%license LICENSE

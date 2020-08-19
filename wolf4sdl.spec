Name:           wolf4sdl
Version:        1.7
Release:        12%{?dist}
Summary:        SDL port of id Software's Wolfenstein 3D
Group:          Amusements/Games
License:        GPLv2+
# Upstream is dead, so lets just point to wikipedia ...
URL:            https://en.wikipedia.org/wiki/Wolfenstein_3D
Source0:        ftp://ftp.nluug.nl/pub/os/Linux/distr/debian/pool/contrib/w/wolf4sdl/wolf4sdl_1.7+svn262+dfsg1.orig.tar.gz
Source1:        ftp://ftp.nluug.nl/pub/os/Linux/distr/debian/pool/contrib/w/wolf4sdl/wolf4sdl_1.7+svn262+dfsg1-3.debian.tar.xz
Source2:        %{name}.desktop
# debian/wolf4sdl.svg rendered at 64x64
Source3:        %{name}.png
# appstream files
Source4:        %{name}-shrwr.appdata.xml
Source5:        %{name}-spear-dem.appdata.xml
Source6:        %{name}-registered-id.metainfo.xml
Source7:        %{name}-registered-apogee.metainfo.xml
Source8:        %{name}-spear.metainfo.xml
# Patches to create different configurations to build
Patch1:         Wolf4SDL-1.6-registered-apogee.patch
Patch2:         Wolf4SDL-1.6-shareware.patch
Patch3:         Wolf4SDL-1.6-spear.patch
Patch4:         Wolf4SDL-1.6-speardemo.patch
BuildRequires:  SDL-devel SDL_mixer-devel desktop-file-utils libappstream-glib
BuildRequires:  gcc-c++

%global desc \
Maybe it was the fact that people got to blow away Nazis. Maybe it was the \
sheer challenge of it all. For whatever reason, Wolfenstein 3D and Spear of \
Destiny, pioneered the first-person shooter genre and brought its legendary \
creators, id Software, worldwide notoriety and numerous awards. In fact, The \
Computer Gaming World Hall of Fame recognized Wolfenstein 3D as helping to \
shape the overall direction of the computer gaming industry. \
\
Wolf4SDL is an open-source port of id Software's classic first-person shooter \
Wolfenstein 3D to the cross-platform multimedia library "Simple DirectMedia \
Layer (SDL)" (http://www.libsdl.org). It is meant to keep the original feel \
while taking advantage of some improvements.

%description
%{desc}


%package        common
Summary:        Common files for %{name}
Requires:       hicolor-icon-theme

%description common
Common files for %{name}.


%package        registered-id
Summary:        SDL port of Wolfenstein 3D - id Software registered version
URL:            http://www.idsoftware.com/games/wolfenstein/wolf3d/
Requires:       %{name}-common = %{version}-%{release}

%description registered-id
This package contains %{name} compiled for playing the registered version of
Wolfenstein 3D as sold by id Software:
http://www.idsoftware.com/games/wolfenstein/wolf3d/

You will need the original registered version's data files to play the
registered version. Place the data files under /usr/share/wolf3d/registered-id
before starting %{name}-registered-id. Note all file-names must be lowercase!
%{desc}


%package        registered-apogee
Summary:        SDL port of Wolfenstein 3D - Apogee registered version
URL:            http://www.3drealms.com/wolf3d/index.html
Requires:       %{name}-common = %{version}-%{release}

%description registered-apogee
This package contains %{name} compiled for playing the registered version of
Wolfenstein 3D as sold by Apogee / 3Drealms here:
http://www.3drealms.com/wolf3d/index.html

You will need the original registered version's data files to play the
registered version. Place the data files under
/usr/share/wolf3d/registered-apogee before starting
%{name}-registered-apogee. Note all file-names must be lowercase!
%{desc}


%package        shareware
Summary:        SDL port of id Software's Wolfenstein 3D - shareware version
URL:            http://www.3drealms.com/wolf3d/index.html
Requires:       %{name}-common = %{version}-%{release}
Requires:       wolf3d-shareware

%description shareware
This package contains %{name} compiled for playing the shareware version of
Wolfenstein 3D.
%{desc}


%package        spear
Summary:        SDL port of Wolfenstein 3D - Spear of Destiny version
URL:            http://www.idsoftware.com/games/wolfenstein/spear/
Requires:       %{name}-common = %{version}-%{release}

%description spear
This package contains %{name} compiled for playing the Spear of Destiny
prequel to Wolfenstein 3D, sold by id Software:
http://www.idsoftware.com/games/wolfenstein/spear/

You will need the original Spear of Destiny data files to play.
Place the data files under /usr/share/spear/full before starting
%{name}-spear. Note all file-names must be lowercase!
%{desc}


%package        spear-demo
Summary:        SDL port of Wolfenstein 3D - Spear of Destiny demo version
URL:            http://www.idsoftware.com/games/wolfenstein/spear/
Requires:       %{name}-common = %{version}-%{release}
Requires:       spear-demo

%description spear-demo
This package contains %{name} compiled for playing the demo of the Spear of
Destiny prequel to Wolfenstein 3D.
%{desc}


%prep
%setup -n wolf4sdl-1.7+svn262 -a 1
for i in debian/patches/*.patch; do
    patch -p1 < $i
done


%build
# Build GPL opl emulator
export GPL=1

CFLAGS="$RPM_OPT_FLAGS -Wno-sign-compare -Wno-switch -Wno-unused-result"
CFLAGS="$CFLAGS -fno-toplevel-reorder $(sdl-config --cflags) -DUSE_GPL"

make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-id/\\\""
mv wolf3d %{name}-registered-id
cp %{SOURCE2} %{name}-registered-id.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (id)|g' \
    %{name}-registered-id.desktop
sed -i 's|@VARIANT@|registered-id|g' %{name}-registered-id.desktop
make clean

patch -p1 < %{PATCH1}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-apogee/\\\""
mv wolf3d %{name}-registered-apogee
cp %{SOURCE2} %{name}-registered-apogee.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (Apogee)|g' \
    %{name}-registered-apogee.desktop
sed -i 's|@VARIANT@|registered-apogee|g' %{name}-registered-apogee.desktop
make clean

patch -p1 < %{PATCH2}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/shareware/\\\""
mv wolf3d %{name}-shareware
cp %{SOURCE2} %{name}-shrwr.desktop
sed -i 's|@NAME@|Wolfenstein 3D Shareware (Apogee)|g' %{name}-shrwr.desktop
sed -i 's|@VARIANT@|shareware|g' %{name}-shrwr.desktop
make clean

patch -p1 < %{PATCH3}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/full/\\\""
mv wolf3d %{name}-spear
cp %{SOURCE2} %{name}-spear.desktop
sed -i 's|@NAME@|Spear of Destiny|g' %{name}-spear.desktop
sed -i 's|@VARIANT@|spear|g' %{name}-spear.desktop
make clean

patch -p1 < %{PATCH4}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/demo/\\\""
mv wolf3d %{name}-spear-demo
cp %{SOURCE2} %{name}-spear-dem.desktop
sed -i 's|@NAME@|Spear of Destiny Demo|g' %{name}-spear-dem.desktop
sed -i 's|@VARIANT@|spear-demo|g' %{name}-spear-dem.desktop


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 debian/%{name}.svg \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

install -p -m 644 debian/man/wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6

install -m 755 %{name}-registered-id $RPM_BUILD_ROOT%{_bindir}
ln -s wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6/wolf4sdl-registered-id.6
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}-registered-id.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wolf3d/registered-id

install -m 755 %{name}-registered-apogee $RPM_BUILD_ROOT%{_bindir}
ln -s wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6/wolf4sdl-registered-apogee.6
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}-registered-apogee.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wolf3d/registered-apogee

install -m 755 %{name}-shareware $RPM_BUILD_ROOT%{_bindir}
ln -s wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6/wolf4sdl-shareware.6
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}-shrwr.desktop

install -m 755 %{name}-spear $RPM_BUILD_ROOT%{_bindir}
ln -s wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6/wolf4sdl-spear.6
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}-spear.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/spear/full

install -m 755 %{name}-spear-demo $RPM_BUILD_ROOT%{_bindir}
ln -s wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6/wolf4sdl-spear-demo.6
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}-spear-dem.desktop

install -p -m 644 %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
    $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}*.xml


%post common
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun common
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans common
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files common
%doc Changes.txt README.txt
%license debian/copyright license-gpl.txt
%{_mandir}/man6/%{name}.6*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files registered-id
%{_bindir}/%{name}-registered-id
%{_mandir}/man6/%{name}-registered-id.6*
%{_datadir}/appdata/%{name}-registered-id.metainfo.xml
%{_datadir}/applications/%{name}-registered-id.desktop
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-id

%files registered-apogee
%{_bindir}/%{name}-registered-apogee
%{_mandir}/man6/%{name}-registered-apogee.6*
%{_datadir}/appdata/%{name}-registered-apogee.metainfo.xml
%{_datadir}/applications/%{name}-registered-apogee.desktop
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-apogee

%files shareware
%{_bindir}/%{name}-shareware
%{_mandir}/man6/%{name}-shareware.6*
%{_datadir}/appdata/%{name}-shrwr.appdata.xml
%{_datadir}/applications/%{name}-shrwr.desktop

%files spear
%{_bindir}/%{name}-spear
%{_mandir}/man6/%{name}-spear.6*
%{_datadir}/appdata/%{name}-spear.metainfo.xml
%{_datadir}/applications/%{name}-spear.desktop
%dir %{_datadir}/spear
%dir %{_datadir}/spear/full

%files spear-demo
%{_bindir}/%{name}-spear-demo
%{_mandir}/man6/%{name}-spear-demo.6*
%{_datadir}/appdata/%{name}-spear-dem.appdata.xml
%{_datadir}/applications/%{name}-spear-dem.desktop


%changelog
* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Sat Jul 28 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 16 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.7-3
- Add keywords to .desktop file

* Tue Jan  5 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.7-2
- Add a -common subpackage containing the shared icon, manpage and doc files
- Fix missing icon-cache scriptlets / Fix icon not showing

* Thu Dec 31 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.7-1
- Upstream is dead, start using Debian sources as upstream
- Update to 1.7+svn262+dfsg1-3 sources
- This version is completely GPLv2+, change License tag to match
  (note still lives in nonfree due to nonfree deps)
- Add various mouse control improvements
- Add new high res icon
- Add appdata files

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6-5
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6-4
- Rebuilt for c++ ABI breakage

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 27 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6-2
- Original upstream is back
- Rebase to new (original) 1.6 src zip
- Add a number of patches from upstream svn (bring version up to svn255 commit)
- Rebase patches borrowed from Debian to the latest Debian package

* Mon Dec 27 2010 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6-1
- Initial rpmfusion package

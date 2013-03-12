Name:           wolf4sdl
Version:        1.6
Release:        5%{?dist}
Summary:        SDL port of id Software's Wolfenstein 3D
Group:          Amusements/Games
License:        Distributable
URL:            http://www.alice-dsl.net/mkroll/
Source0:        http://www.alice-dsl.net/mkroll/bins/Wolf4SDL-1.6-src.zip
Source1:        %{name}.desktop
# Update to 1.7 svn snapshot
Patch0:         wolf4sdl-1.7-svn255.patch
# The below patch and the package description are taken from the Debian
# package by Fabian Greffrath <fabian+debian@greffrath.com>
# License:
#  Copying and distribution of the Debian packaging, with or without
#  modification are permitted in any medium without royalty provided the
#  copyright notice and this notice are preserved. The Debian packaging is
#  offered as-is, without any warranty.
Patch1:         wolf4sdl-1.7-svn255-debian.patch
# Patches to create different configurations to build
Patch2:         Wolf4SDL-1.6-registered-apogee.patch
Patch3:         Wolf4SDL-1.6-shareware.patch
Patch4:         Wolf4SDL-1.6-spear.patch
Patch5:         Wolf4SDL-1.6-speardemo.patch
BuildRequires:  SDL-devel SDL_mixer-devel desktop-file-utils

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


%package        registered-id
Summary:        SDL port of Wolfenstein 3D - id Software registered version
URL:            http://www.idsoftware.com/games/wolfenstein/wolf3d/

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
Requires:       wolf3d-shareware

%description shareware
This package contains %{name} compiled for playing the shareware version of
Wolfenstein 3D.
%{desc}


%package        spear
Summary:        SDL port of Wolfenstein 3D - Spear of Destiny version
URL:            http://www.idsoftware.com/games/wolfenstein/spear/

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
Requires:       spear-demo

%description spear-demo
This package contains %{name} compiled for playing the demo of the Spear of
Destiny prequel to Wolfenstein 3D.
%{desc}


%prep
%setup -c -T -n Wolf4SDL-1.6-src
# Must unpack ourselves to make zip do dos2unix conversion
pushd .. && unzip -a -q %{SOURCE0} && popd
%patch0 -p1
%patch1 -p1
for i in debian/patches/*.patch; do
    patch -p1 < $i
done


%build
CFLAGS="$RPM_OPT_FLAGS -Wno-sign-compare -Wno-switch -Wno-unused-result"
CFLAGS="$CFLAGS -fno-toplevel-reorder $(sdl-config --cflags)"

make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-id/\\\""
mv wolf3d %{name}-registered-id
cp %{SOURCE1} %{name}-registered-id.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (id)|g' \
    %{name}-registered-id.desktop
sed -i 's|@VARIANT@|registered-id|g' %{name}-registered-id.desktop
make clean

patch -p1 < %{PATCH2}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-apogee/\\\""
mv wolf3d %{name}-registered-apogee
cp %{SOURCE1} %{name}-registered-apogee.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (Apogee)|g' \
    %{name}-registered-apogee.desktop
sed -i 's|@VARIANT@|registered-apogee|g' %{name}-registered-apogee.desktop
make clean

patch -p1 < %{PATCH3}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/shareware/\\\""
mv wolf3d %{name}-shareware
cp %{SOURCE1} %{name}-shareware.desktop
sed -i 's|@NAME@|Wolfenstein 3D Shareware (Apogee)|g' %{name}-shareware.desktop
sed -i 's|@VARIANT@|shareware|g' %{name}-shareware.desktop
make clean

patch -p1 < %{PATCH4}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/full/\\\""
mv wolf3d %{name}-spear
cp %{SOURCE1} %{name}-spear.desktop
sed -i 's|@NAME@|Spear of Destiny|g' %{name}-spear.desktop
sed -i 's|@VARIANT@|spear|g' %{name}-spear.desktop
make clean

patch -p1 < %{PATCH5}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/demo/\\\""
mv wolf3d %{name}-spear-demo
cp %{SOURCE1} %{name}-spear-demo.desktop
sed -i 's|@NAME@|Spear of Destiny Demo|g' %{name}-spear-demo.desktop
sed -i 's|@VARIANT@|spear-demo|g' %{name}-spear-demo.desktop


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 debian/man/wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 debian/pixmaps/wolf4sdl.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps

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
    %{name}-shareware.desktop

install -m 755 %{name}-spear $RPM_BUILD_ROOT%{_bindir}
ln -s wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6/wolf4sdl-spear.6
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}-spear.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/spear/full

install -m 755 %{name}-spear-demo $RPM_BUILD_ROOT%{_bindir}
ln -s wolf4sdl.6 $RPM_BUILD_ROOT%{_mandir}/man6/wolf4sdl-spear-demo.6
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}-spear-demo.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%files registered-id
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-registered-id
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-registered-id.6*
%{_datadir}/applications/%{name}-registered-id.desktop
%{_datadir}/pixmaps/%{name}.xpm
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-id

%files registered-apogee
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-registered-apogee
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-registered-apogee.6*
%{_datadir}/applications/%{name}-registered-apogee.desktop
%{_datadir}/pixmaps/%{name}.xpm
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-apogee

%files shareware
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-shareware
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-shareware.6*
%{_datadir}/applications/%{name}-shareware.desktop
%{_datadir}/pixmaps/%{name}.xpm

%files spear
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-spear
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-spear.6*
%{_datadir}/applications/%{name}-spear.desktop
%{_datadir}/pixmaps/%{name}.xpm
%dir %{_datadir}/spear
%dir %{_datadir}/spear/full

%files spear-demo
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-spear-demo
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-spear-demo.6*
%{_datadir}/applications/%{name}-spear-demo.desktop
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6-5
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6-4
- Rebuilt for c++ ABI breakage

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 27 2011 Hans de Goede <hdegoede@redhat.com> 1.6-2
- Original upstream is back
- Rebase to new (original) 1.6 src zip
- Add a number of patches from upstream svn (bring version up to svn255 commit)
- Rebase patches borrowed from Debian to the latest Debian package

* Mon Dec 27 2010 Hans de Goede <hdegoede@redhat.com> 1.6-1
- Initial rpmfusion package

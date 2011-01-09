Name:           wolf4sdl
Version:        1.6
Release:        1%{?dist}
Summary:        SDL port of id Software's Wolfenstein 3D
Group:          Amusements/Games
License:        Distributable
# These url's are for a version targeted mainly at Mac OS X
# The original wolf4sdl site was:
# http://www.stud.uni-karlsruhe.de/~uvaue/chaos
# But this gives 403 errors now a days.
URL:            http://chrisballinger.info/wolf4sdl/
Source0:        http://chrisballinger.info/wolf4sdl/Wolf4SDL-1.6-src.zip
# All the below files and the package description are taken from the Debian
# package by Fabian Greffrath <fabian+debian@greffrath.com>
# License:
#  Copying and distribution of the Debian packaging, with or without
#  modification are permitted in any medium without royalty provided the
#  copyright notice and this notice are preserved. The Debian packaging is
#  offered as-is, without any warranty.
Source1:        %{name}.6
Source2:        %{name}.desktop
Source3:        %{name}.xpm
Patch0:         01-shareware-version.patch
Patch1:         02-enable-shading.patch
Patch2:         10-datadir.patch
Patch3:         11-configdir.patch
Patch4:         21-compiler-warnings.patch
# end Debian files
Patch5:         Wolf4SDL-1.6-compile-fixes.patch
Patch6:         Wolf4SDL-1.6-registered-apogee.patch
Patch7:         Wolf4SDL-1.6-spear.patch
Patch8:         Wolf4SDL-1.6-speardemo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
%setup -q -c
pushd Wolf4SDL-1.6-src
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

chmod -x *.cpp *.h *.inc

mkdir ../doc
for i in Changes.txt README.txt license-*.txt; do
    cat $i | sed 's|\r||g' > ../doc/$i
    touch -r $i ../doc/$i
done

popd


%build
pushd Wolf4SDL-1.6-src
CFLAGS="$RPM_OPT_FLAGS -Wno-sign-compare -Wno-switch -Wno-unused-result"
CFLAGS="$CFLAGS $(sdl-config --cflags)"

make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-id/\\\""
mv wolf3d %{name}-registered-id
cp %{SOURCE2} %{name}-registered-id.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (id)|g' \
    %{name}-registered-id.desktop
sed -i 's|@VARIANT@|registered-id|g' %{name}-registered-id.desktop
make clean

patch -p1 < %{PATCH6}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-apogee/\\\""
mv wolf3d %{name}-registered-apogee
cp %{SOURCE2} %{name}-registered-apogee.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (Apogee)|g' \
    %{name}-registered-apogee.desktop
sed -i 's|@VARIANT@|registered-apogee|g' %{name}-registered-apogee.desktop
make clean

patch -p1 < %{PATCH0}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/shareware/\\\""
mv wolf3d %{name}-shareware
cp %{SOURCE2} %{name}-shareware.desktop
sed -i 's|@NAME@|Wolfenstein 3D Shareware (Apogee)|g' %{name}-shareware.desktop
sed -i 's|@VARIANT@|shareware|g' %{name}-shareware.desktop
make clean

patch -p1 < %{PATCH7}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/full/\\\""
mv wolf3d %{name}-spear
cp %{SOURCE2} %{name}-spear.desktop
sed -i 's|@NAME@|Spear of Destiny|g' %{name}-spear.desktop
sed -i 's|@VARIANT@|spear|g' %{name}-spear.desktop
make clean

patch -p1 < %{PATCH8}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/demo/\\\""
mv wolf3d %{name}-spear-demo
cp %{SOURCE2} %{name}-spear-demo.desktop
sed -i 's|@NAME@|Spear of Destiny Demo|g' %{name}-spear-demo.desktop
sed -i 's|@VARIANT@|spear-demo|g' %{name}-spear-demo.desktop

popd


%install
pushd Wolf4SDL-1.6-src
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps

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

popd


%clean
rm -rf $RPM_BUILD_ROOT


%files registered-id
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}-registered-id
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-registered-id.6*
%{_datadir}/applications/%{name}-registered-id.desktop
%{_datadir}/pixmaps/%{name}.xpm
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-id

%files registered-apogee
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}-registered-apogee
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-registered-apogee.6*
%{_datadir}/applications/%{name}-registered-apogee.desktop
%{_datadir}/pixmaps/%{name}.xpm
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-apogee

%files shareware
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}-shareware
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-shareware.6*
%{_datadir}/applications/%{name}-shareware.desktop
%{_datadir}/pixmaps/%{name}.xpm

%files spear
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}-spear
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-spear.6*
%{_datadir}/applications/%{name}-spear.desktop
%{_datadir}/pixmaps/%{name}.xpm
%dir %{_datadir}/spear
%dir %{_datadir}/spear/full

%files spear-demo
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}-spear-demo
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-spear-demo.6*
%{_datadir}/applications/%{name}-spear-demo.desktop
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Mon Dec 27 2010 Hans de Goede <hdegoede@redhat.com> 1.6-1
- Initial rpmfusion package

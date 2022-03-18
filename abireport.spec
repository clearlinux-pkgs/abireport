#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : abireport
Version  : 1.0.11
Release  : 37
URL      : https://github.com/clearlinux/abireport/releases/download/v1.0.11/abireport-1.0.11.tar.xz
Source0  : https://github.com/clearlinux/abireport/releases/download/v1.0.11/abireport-1.0.11.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: abireport-bin = %{version}-%{release}
Requires: abireport-license = %{version}-%{release}
Requires: abireport-man = %{version}-%{release}
BuildRequires : buildreq-golang

%description
abireport
----------
[![Report](https://goreportcard.com/badge/github.com/clearlinux/abireport)](https://goreportcard.com/report/github.com/clearlinux/abireport) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

%package bin
Summary: bin components for the abireport package.
Group: Binaries
Requires: abireport-license = %{version}-%{release}

%description bin
bin components for the abireport package.


%package license
Summary: license components for the abireport package.
Group: Default

%description license
license components for the abireport package.


%package man
Summary: man components for the abireport package.
Group: Default

%description man
man components for the abireport package.


%prep
%setup -q -n abireport-1.0.11
cd %{_builddir}/abireport-1.0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624577898
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1624577898
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/abireport
cp %{_builddir}/abireport-1.0.11/LICENSE %{buildroot}/usr/share/package-licenses/abireport/598f87f072f66e2269dd6919292b2934dbb20492
cp %{_builddir}/abireport-1.0.11/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/abireport/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/abireport-1.0.11/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/abireport/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/abireport-1.0.11/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/abireport/b3c86ae465b21f7323059db335158b48187731c7
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/abireport

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/abireport/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/abireport/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/abireport/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/abireport/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/abireport.1

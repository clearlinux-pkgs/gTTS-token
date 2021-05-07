#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gTTS-token
Version  : 1.1.4
Release  : 19
URL      : https://files.pythonhosted.org/packages/78/b4/e2306352c5b5d777c9d39cbf17f21b10be40cbe7271329473d424700aa41/gTTS-token-1.1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/78/b4/e2306352c5b5d777c9d39cbf17f21b10be40cbe7271329473d424700aa41/gTTS-token-1.1.4.tar.gz
Summary  : Calculates a token to run the Google Translate text to speech
Group    : Development/Tools
License  : MIT
Requires: gTTS-token-license = %{version}-%{release}
Requires: gTTS-token-python = %{version}-%{release}
Requires: gTTS-token-python3 = %{version}-%{release}
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : requests

%description
====

%package license
Summary: license components for the gTTS-token package.
Group: Default

%description license
license components for the gTTS-token package.


%package python
Summary: python components for the gTTS-token package.
Group: Default
Requires: gTTS-token-python3 = %{version}-%{release}
Provides: gtts-token-python

%description python
python components for the gTTS-token package.


%package python3
Summary: python3 components for the gTTS-token package.
Group: Default
Requires: python3-core
Provides: pypi(gtts_token)
Requires: pypi(requests)

%description python3
python3 components for the gTTS-token package.


%prep
%setup -q -n gTTS-token-1.1.4
cd %{_builddir}/gTTS-token-1.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604971730
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gTTS-token
cp %{_builddir}/gTTS-token-1.1.4/LICENSE %{buildroot}/usr/share/package-licenses/gTTS-token/748ee85e743c7323d44803cdba103206fdb58874
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gTTS-token/748ee85e743c7323d44803cdba103206fdb58874

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gTTS-token
Version  : 1.1.3
Release  : 5
URL      : https://files.pythonhosted.org/packages/e7/25/ca6e9cd3275bfc3097fe6b06cc31db6d3dfaf32e032e0f73fead9c9a03ce/gTTS-token-1.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/25/ca6e9cd3275bfc3097fe6b06cc31db6d3dfaf32e032e0f73fead9c9a03ce/gTTS-token-1.1.3.tar.gz
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

%description python3
python3 components for the gTTS-token package.


%prep
%setup -q -n gTTS-token-1.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543514874
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gTTS-token
cp LICENSE %{buildroot}/usr/share/package-licenses/gTTS-token/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gTTS-token/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

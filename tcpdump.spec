#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE089DEF1D9C15D0D (release@tcpdump.org)
#
Name     : tcpdump
Version  : 4.9.2
Release  : 24
URL      : http://www.tcpdump.org/release/tcpdump-4.9.2.tar.gz
Source0  : http://www.tcpdump.org/release/tcpdump-4.9.2.tar.gz
Source99 : http://www.tcpdump.org/release/tcpdump-4.9.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: tcpdump-bin
Requires: tcpdump-doc
BuildRequires : libcap-ng-dev
BuildRequires : libpcap-dev

%description
# tcpdump
[![Build
Status](https://travis-ci.org/the-tcpdump-group/tcpdump.png)](https://travis-ci.org/the-tcpdump-group/tcpdump)

%package bin
Summary: bin components for the tcpdump package.
Group: Binaries

%description bin
bin components for the tcpdump package.


%package doc
Summary: doc components for the tcpdump package.
Group: Documentation

%description doc
doc components for the tcpdump package.


%prep
%setup -q -n tcpdump-4.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504570151
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1504570151
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tcpdump
/usr/bin/tcpdump.4.9.2

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

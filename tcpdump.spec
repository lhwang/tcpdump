#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tcpdump
Version  : 4.7.4
Release  : 16
URL      : http://www.tcpdump.org/release/tcpdump-4.7.4.tar.gz
Source0  : http://www.tcpdump.org/release/tcpdump-4.7.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: tcpdump-bin
Requires: tcpdump-doc
BuildRequires : libcap-ng-dev
BuildRequires : libpcap-dev
BuildRequires : openssl-dev
Patch1: nogeneve.patch

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
%setup -q -n tcpdump-4.7.4
%patch1 -p1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tcpdump
/usr/bin/tcpdump.4.7.4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

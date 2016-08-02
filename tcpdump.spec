#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tcpdump
Version  : 4.8.0
Release  : 18
URL      : http://www.tcpdump.org/release/tcpdump-4.8.0.tar.gz
Source0  : http://www.tcpdump.org/release/tcpdump-4.8.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: tcpdump-bin
Requires: tcpdump-doc
BuildRequires : libcap-ng-dev
BuildRequires : libpcap-dev
Patch1: nogeneve.patch

%description
To build tcpdump under Windows, you need:
- version 6 (or higher) of Microsoft Visual Studio or the Cygnus gnu
C compiler.
- The November 2001 (or later) edition of Microsoft Platform
Software Development Kit (SDK), that contains some necessary includes
for IPv6 support. You can download it from http://www.microsoft.com/sdk
- the WinPcap source code, that includes libpcap for win32. Download it
from http://winpcap.polito.it or download libpcap sources from
file.

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
%setup -q -n tcpdump-4.8.0
%patch1 -p1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tcpdump
/usr/bin/tcpdump.4.8.0

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

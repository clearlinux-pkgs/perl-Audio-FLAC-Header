#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Audio-FLAC-Header
Version  : 2.4
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANIEL/Audio-FLAC-Header-2.4.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANIEL/Audio-FLAC-Header-2.4.tar.gz
Summary  : interface to FLAC header metadata.
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
Audio::FLAC version 2.4
=======================
how to install the module, any machine dependencies it may have (for
example C compilers and installed libraries) and any other information
that should be provided before the module is installed.

%package dev
Summary: dev components for the perl-Audio-FLAC-Header package.
Group: Development
Provides: perl-Audio-FLAC-Header-devel = %{version}-%{release}

%description dev
dev components for the perl-Audio-FLAC-Header package.


%prep
%setup -q -n Audio-FLAC-Header-2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Audio/FLAC/Header.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Audio::FLAC::Header.3

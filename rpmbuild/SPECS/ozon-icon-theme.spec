Name:		ozon-icon-theme
Version:	0.1.0
Release:	1%{?dist}
Summary:	Default icon theme for OzonOS.
Group:		User Interface/Desktops
License:	GPL-3.0+
URL:		https://github.com/ozonos/ozon-icon-theme
Source0:	%{name}-%{version}.tar.gz
BuildArch:  noarch

%description
 This is the default icon theme for OzonOS. It's licensed under the GNU GPLv3+.

%prep
%setup -q

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
/usr/share/icons/Ozon/

%changelog
* Sat Jan 10 06:27:21 UTC 2015 Markus S. <kamikazow@web.de>
- BuildArch: noarch
- SPDX License Identifier
- Use variables for source file name

* Sat Dec 20 2014 Paolo Rotolo <paolorotolo@ubuntu.com> - 0.1.0-1
- Initial package for Fedora

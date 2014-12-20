Name:		ozon-icon-theme
Version:	0.1.0
Release:	1%{?dist}
Summary:	Default icon theme for OzonOS.
Group:		User Interface/Desktops
License:	GPLv3+
URL:		https://github.com/ozonos/ozon-icon-theme
Source0:	ozon-icon-theme-0.1.0.tar.gz

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
* Sat Dec 20 2014 Paolo Rotolo <paolorotolo@ubuntu.com> - 0.1.0-1
- Initial package for Fedora

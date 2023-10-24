%define _unpackaged_files_terminate_build 1

Name: alterator-module-application
Version: 0.1.0
Release: alt1

Summary: Local applications interface for alterator browser.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/alterator-module-application

BuildArch: noarch

Source0: %name-%version.tar

%description
Local applications interface for alterator browser with rules, scripts and xml.

%prep
%setup

%install
mkdir -p %buildroot%{_datadir}/dbus-1/interfaces
mkdir -p %buildroot%{_sysconfdir}/polkit-1/rules.d
mkdir -p %buildroot%{_datadir}/alterator/backends
mkdir -p %buildroot%{_datadir}/alterator/scripts

install -v -p -m 644 -D ru.basealt.alterator.applications.xml %buildroot%{_datadir}/dbus-1/interfaces
install -v -p -m 644 -D 46-alterator-module-application.rules %buildroot%{_sysconfdir}/polkit-1/rules.d
install -v -p -m 644 -D applications.backend %buildroot%{_datadir}/alterator/backends
install -v -p -m 755 -D *.sh %buildroot%{_datadir}/alterator/scripts

%files
%{_datadir}/alterator/backends/*.backend
%{_datadir}/alterator/scripts/*.sh
%{_datadir}/dbus-1/interfaces/ru.basealt.alterator.applications.xml
%{_sysconfdir}/polkit-1/rules.d/46-alterator-module-application.rules

%changelog
* Tue Oct 24 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
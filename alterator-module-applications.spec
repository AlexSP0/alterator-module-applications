%define _unpackaged_files_terminate_build 1

Name: alterator-module-applications
Version: 0.1.0
Release: alt1

Summary: Local applications interface for alterator browser.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/alterator-module-applications

BuildArch: noarch

Source0: %name-%version.tar

%description
Local applications interface for alterator browser with rules, scripts and xml.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dbus-1/interfaces
#mkdir -p %buildroot%_sysconfdir/polkit-1/rules.d
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_sysconfdir/alterator/backends
mkdir -p %buildroot%_libexecdir/%name

install -v -p -m 644 -D ru.basealt.alterator.applications.xml %buildroot%_datadir/dbus-1/interfaces
#install -v -p -m 644 -D 49-alterator-module-applications.rules %buildroot%_sysconfdir/polkit-1/rules.d
install -v -p -m 644 -D ru.basealt.alterator.applications.policy %buildroot%_datadir/polkit-1/actions
install -v -p -m 644 -D applications.backend %buildroot%_sysconfdir/alterator/backends
install -v -p -m 755 -D app-info %buildroot%_libexecdir/%name
install -v -p -m 755 -D list-apps %buildroot%_libexecdir/%name

%files
%_sysconfdir/alterator/backends/*.backend
%dir %_libexecdir/%name
%_datadir/polkit-1/actions/ru.basealt.alterator.applications.policy
%_libexecdir/%name/app-info
%_libexecdir/%name/list-apps
%_datadir/dbus-1/interfaces/ru.basealt.alterator.applications.xml
#%_sysconfdir/polkit-1/rules.d/49-alterator-module-applications.rules

%changelog
* Tue Oct 24 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build

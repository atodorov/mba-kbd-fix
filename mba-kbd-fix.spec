Summary:   Keyboard fixes for MacBook Air
Name:      mba-kbd-fix
Version:   1
Release:   1%{?dist}
URL:       http://github.com/atodorov/mba-kbd-fix
License:   MIT
Group:     System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   mba-kbd-fix.service
Source1:   README.md

BuildArch: noarch

%description
This package provides a modprobe configuration file for hid_apple which
reverses the behavior of media and function keys and fixes tilde mapping.

%prep
echo > /dev/null

%build
echo > /dev/null

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/systemd/system
install -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/systemd/system

mkdir -p %{buildroot}/%{_docdir}/%{name}
install -m 0644 %{SOURCE1}  %{buildroot}/%{_docdir}/%{name}

%post
systemctl daemon-reload
systemctl enable mapping_fix
systemctl start mapping_fix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/systemd/system/mba-kbd-fix.service
%doc %{_docdir}/%{name}/README.md

%changelog

* Thu Apr 30 2015 Alexander Todorov <atodorov@redhat.com> - 1-1
- initial build

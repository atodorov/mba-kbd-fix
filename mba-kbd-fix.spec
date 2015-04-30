Summary:   Keyboard fixes for MacBook Air
Name:      mba-kbd-fix
Version:   1
Release:   1%{?dist}
URL:       http://github.com/atodorov/mba-kbd-fix
License:   MIT
Group:     System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   mba-kbd-fix.conf
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

mkdir -p %{buildroot}/%{_sysconfdir}/modprobe.d/
install -m 0644 %{source0} %{buildroot}/%{_sysconfdir}/modprobe.d/

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 %{source1}  %{buildroot}/%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/modprobe.d/%{source0}
%doc %{_docdir}/%{name}-%{version}/%{source1}

%changelog

* Thu Apr 30 2015 Alexander Todorov <atodorov@redhat.com> - 1-1
- initial build

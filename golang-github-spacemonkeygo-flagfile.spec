# https://github.com/spacemonkeygo/flagfile
%global provider_prefix github.com/spacemonkeygo/flagfile
%global gobaseipath     %{provider_prefix}
%global commit          871ce569c29360f95d7596f90aa54d5ecef75738
%global commitdate      20150204

%gocraftmeta -i

Name:           %{goname}
Version:        0
Release:        0.10.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Simple api for flag serialization and parsing
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20150204git871ce56
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git871ce56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git871ce56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git871ce56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git871ce56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git871ce56
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git871ce56
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git871ce56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git871ce56
- Update spec file to spec-2.0
  resolves: #1250512

* Mon Jun 15 2015 Marek Skalicky <mskalick@redhat.com> - 0-0.1.git871ce56
- First package for Fedora
  resolves: #1211312


Summary:	Common dirs for Zope libraries
Name:		Zope-dirs
Version:	1.0
Release:	1
License:	Public Domain
Group:		Libraries/Python
BuildRequires:	python
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for Zope libraries.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/zope
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/zope

touch $RPM_BUILD_ROOT%{py_sitedir}/zope/__init__.py
touch $RPM_BUILD_ROOT%{py_sitescriptdir}/zope/__init__.py

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/zope
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/zope
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope
%{py_sitescriptdir}/zope

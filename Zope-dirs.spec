Summary:	Common dirs for Zope libraries
Summary(pl.UTF-8):	Katalogi wspólne dla bibliotek Zope
Name:		Zope-dirs
Version:	1.0
Release:	4
License:	Public Domain
Group:		Libraries/Python
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
Common dirs for Zope libraries.

%description -l pl.UTF-8
Katalogi wspólne dla bibliotek Zope.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/zope
touch $RPM_BUILD_ROOT%{py_sitedir}/zope/__init__.py
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope

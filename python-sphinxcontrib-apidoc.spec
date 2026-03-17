%define module sphinxcontrib-apidoc
%define oname sphinxcontrib_apidoc

Name:		python-sphinxcontrib-apidoc
Version:	0.6.0
Release:	1
Summary:	A Sphinx extension for running sphinx-apidoc on each build
License:	BSD License
Group:		Development/Python
URL:		https://pypi.org/project/sphinxcontrib-apidoc/
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A Sphinx extension for running 'sphinx-apidoc' on each build.

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/sphinxcontrib
%{py_sitedir}/%{oname}-%{version}-py%{pyver}-nspkg.pth
%{py_sitedir}/%{oname}-%{version}.dist-info

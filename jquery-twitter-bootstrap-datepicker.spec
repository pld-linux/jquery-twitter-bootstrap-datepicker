%define		plugin	datepicker
Summary:	Bootstrap - front-end framework for faster and easier web development
Name:		jquery-twitter-bootstrap-%{plugin}
Version:	2.3.1
Release:	2
License:	Apache License v2.0
Group:		Applications/WWW
Source0:	http://www.eyecon.ro/bootstrap-datepicker/datepicker.zip
# Source0-md5:	8f2fdaf53a1022d60002752289d8f7f4
URL:		http://www.eyecon.ro/bootstrap-datepicker/
BuildRequires:	unzip
Requires:	jquery >= 1.7
Requires:	jquery-twitter-bootstrap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/twitter-bootstrap/%{plugin}

%description
Sleek, intuitive, and powerful front-end framework for faster and
easier web development.

%prep
%setup -qc
mv %{plugin}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -p js/bootstrap-%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p css/%{plugin}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.css
ln -s %{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

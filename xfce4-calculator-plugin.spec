Summary:	A calculator plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka kalkulatora przeznaczenia dla panelu Xfce4
Name:		xfce4-calculator-plugin
Version:	0.8.0
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-calculator-plugin/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	6c5988322d05fa40ff74916a08072c84
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-calculator-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce4-calculator-plugin is a calculator plugin for the Xfce4 panel.

%description -l pl.UTF-8
Xfce4-calculator-plugin jest wtyczką kalkulatora dla panelu Xfce4.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hy_AM,hye,ie}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libcalculator.so
%{_datadir}/xfce4/panel/plugins/calculator.desktop
%{_iconsdir}/hicolor/*x*/apps/xfce4-calculator-plugin.png

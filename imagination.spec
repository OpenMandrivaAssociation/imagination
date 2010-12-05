%define		name	imagination
%define		version	2.1
%define		release %mkrel 2

Summary:	Simple DVD slide show maker
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Video
License:	GPLv2+
URL:		http://imagination.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
# patch to add support of plugin, asked by developer in README
Patch:          imagination-plugin_support.patch
BuildRequires:	gtk2-devel
BuildRequires:	sox-devel >= 14.3.0
BuildRequires:	desktop-file-utils
BuildRequires:	cairo-devel 
BuildRequires:  glib-devel
BuildRequires:  gettext intltool
BuildRequires:	docbook-xsl xsltproc
Requires: 	sox >= 14.3.0
Requires: 	ffmpeg


%description
Imagination is a lightweight and simple DVD slide show maker written 
in C language and built with the GTK+2 toolkit.

%prep
%setup -q 
%patch -p1

%build
%configure2_5x --disable-static 

%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 
desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-Multimedia-Video" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop


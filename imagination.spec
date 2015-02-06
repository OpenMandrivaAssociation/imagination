Summary:	Simple DVD slide show maker
Name:		imagination
Version:	3.0
Release:	3
Group:		Video
License:	GPLv2+
URL:		http://imagination.sourceforge.net/
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		imagination-3.0-link.patch
BuildRequires:	pkgconfig(cairo) >= 1.6
BuildRequires:	pkgconfig(glib-2.0) > 2.18.0
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.14.0
BuildRequires:	pkgconfig(sox) >= 14.2.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	docbook-xsl
BuildRequires:	docbook-style-xsl
Requires:	sox >= 14.3.0
Requires:	ffmpeg

%description
Imagination is a lightweight and simple DVD slide show maker written 
in C language and built with the GTK+2 toolkit.

%prep
%setup -q
%patch0 -p0
# Otherwise plugins won't be loading from %{_libdir}/%{name}
sed -i -e "/#define PLUGINS_INSTALLED/s:0:1:" src/support.h

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-Multimedia-Video" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop


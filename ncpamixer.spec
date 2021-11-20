Summary:	ncurses PulseAudio Mixer
Name:		ncpamixer
Version:	1.3.3.1
Release:	2
License:	MIT
Group:		Applications/Sound
Source0:	https://github.com/fulhax/ncpamixer/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	351d35b9652f75f1f61fb7842db1763c
URL:		https://github.com/fulhax/ncpamixer
BuildRequires:	cmake >= 3.1
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An ncurses mixer for PulseAudio inspired by pavucontrol.

%prep
%setup -q

%build
install -d build
cd build
%cmake ../src \
	-DUSE_WIDE=TRUE
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/ncpamixer

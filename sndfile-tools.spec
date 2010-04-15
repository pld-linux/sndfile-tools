Summary:	Small collection of programs that use libsndfile and other libraries
Summary(pl.UTF-8):	Mały zestaw programów wykorzystujących libsndfile i inne biblioteki
Name:		sndfile-tools
Version:	1.03
Release:	1
License:	GPL v2 or GPL v3
Group:		Applications/Sound
Source0:	http://www.mega-nerd.com/libsndfile/files/%{name}-%{version}.tar.gz
# Source0-md5:	5b74bb6bb4b2627158f861ae9c45e433
URL:		http://www.mega-nerd.com/libsndfile/tools/
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	fftw3-devel >= 0.15.0
BuildRequires:	gcc-fortran
BuildRequires:	jack-audio-connection-kit-devel >= 0.100
BuildRequires:	libsndfile-devel >= 1.0.19
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small collection of programs that use libsndfile and other libraries.

%description -l pl.UTF-8
Mały zestaw programów wykorzystujących libsndfile i inne biblioteki.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sndfile-generate-chirp
%attr(755,root,root) %{_bindir}/sndfile-spectrogram
%attr(755,root,root) %{_bindir}/sndfile-mix-to-mono
%attr(755,root,root) %{_bindir}/sndfile-jackplay
%{_mandir}/man1/sndfile-generate-chirp.1*
%{_mandir}/man1/sndfile-spectrogram.1*
%{_mandir}/man1/sndfile-mix-to-mono.1*
%{_mandir}/man1/sndfile-jackplay.1*

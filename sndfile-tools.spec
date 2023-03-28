Summary:	Small collection of programs that use libsndfile and other libraries
Summary(pl.UTF-8):	Mały zestaw programów wykorzystujących libsndfile i inne biblioteki
Name:		sndfile-tools
Version:	1.5
Release:	1
License:	GPL v2 or GPL v3
Group:		Applications/Sound
#Source0Download: https://github.com/libsndfile/sndfile-tools/releases
Source0:	https://github.com/libsndfile/sndfile-tools/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	26dc615302b65aee3ace917be192d30a
URL:		http://www.mega-nerd.com/libsndfile/tools/
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	fftw3-devel >= 0.15.0
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gcc-fortran
BuildRequires:	jack-audio-connection-kit-devel >= 0.100
BuildRequires:	libsamplerate-devel >= 0.1.5
BuildRequires:	libsndfile-devel >= 1.0.19
BuildRequires:	pkgconfig
Requires:	cairo >= 1.4.0
Requires:	fftw3 >= 0.15.0
Requires:	jack-audio-connection-kit-libs >= 0.100
Requires:	libsamplerate >= 0.1.5
Requires:	libsndfile >= 1.0.19
Provides:	libsamplerate-tools
Obsoletes:	libsamplerate-tools < 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small collection of programs that use libsndfile and other libraries.

%description -l pl.UTF-8
Mały zestaw programów wykorzystujących libsndfile i inne biblioteki.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/sndfile-tools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*
%attr(755,root,root) %{_bindir}/sndfile-generate-chirp
%attr(755,root,root) %{_bindir}/sndfile-jackplay
%attr(755,root,root) %{_bindir}/sndfile-mix-to-mono
%attr(755,root,root) %{_bindir}/sndfile-resample
%attr(755,root,root) %{_bindir}/sndfile-spectrogram
%attr(755,root,root) %{_bindir}/sndfile-waveform
%{_mandir}/man1/sndfile-generate-chirp.1*
%{_mandir}/man1/sndfile-jackplay.1*
%{_mandir}/man1/sndfile-mix-to-mono.1*
%{_mandir}/man1/sndfile-resample.1*
%{_mandir}/man1/sndfile-spectrogram.1*

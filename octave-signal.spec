%global octpkg signal

Summary:	Signal processing tools for Octave
Name:		octave-signal
Version:	1.4.3
Release:	1
License:	GPLv3+ and Public Domain
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/signal/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.8.0
BuildRequires:  octave-control >= 2.4.0

Requires:	octave(api) = %{octave_api}
Requires:  	octave-control >= 2.4.0

Requires(post): octave
Requires(postun): octave

%description
Signal processing tools, including filtering, windowing and display
functions.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild


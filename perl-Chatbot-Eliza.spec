%include	/usr/lib/rpm/macros.perl
%define		pdir	Chatbot
%define		pnam	Eliza
Summary:	Eliza perl module
Summary(pl):	Modu³ perla Eliza
Name:		perl-Chatbot-Eliza
Version:	1.04
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	754199bbe591eaa11301aee108586fcd
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chatbot::Eliza module - classic Eliza algorithm.

%description -l pl
Modu³ Chatbot::Eliza - klasyczny algorytm Eliza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *txt twobots
%dir %{perl_vendorlib}/Chatbot
%{perl_vendorlib}/Chatbot/Eliza.pm
%{_mandir}/man3/*

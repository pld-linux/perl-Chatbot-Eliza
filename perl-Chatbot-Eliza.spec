%include	/usr/lib/rpm/macros.perl
Summary:	Eliza perl module
Summary(pl):	Modu³ perla Eliza
Name:		perl-Chatbot-Eliza
Version:	0.97
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Chatbot/Chatbot-Eliza-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chatbot-Eliza module - classic Eliza algorithm.

%description -l pl
Modu³ Chatbot-Eliza - klasyczny algorytm Eliza.

%prep
%setup -q -n Chatbot-Eliza-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz twobots
%dir %{perl_sitelib}/Chatbot
%{perl_sitelib}/Chatbot/Eliza.pm
%{_mandir}/man3/*

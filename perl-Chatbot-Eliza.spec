%include	/usr/lib/rpm/macros.perl
Summary:	Eliza perl module
Summary(pl):	Modu³ perla Eliza
Name:		perl-Chatbot-Eliza
Version:	0.91
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Chatbot/Chatbot-Eliza-%{version}.tar.gz
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-13
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Chatbot-Eliza module - classic Eliza algorithm.

%description -l pl
Modu³ Chatbot-Eliza - klasyczny algorytm Eliza.

%prep
%setup -q -n Chatbot-Eliza-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Chatbot
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz deutsch* doctor* debug* simple* twobots

%dir %{perl_sitelib}/Chatbot
%{perl_sitelib}/Chatbot/Eliza.pm
%{perl_sitearch}/auto/Chatbot

%{_mandir}/man3/*

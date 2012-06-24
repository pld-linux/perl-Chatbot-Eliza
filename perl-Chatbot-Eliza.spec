%include	/usr/lib/rpm/macros.perl
Summary:	Eliza perl module
Summary(pl):	Modu� perla Eliza
Name:		perl-Chatbot-Eliza
Version:	0.97
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Chatbot/Chatbot-Eliza-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chatbot-Eliza module - classic Eliza algorithm.

%description -l pl
Modu� Chatbot-Eliza - klasyczny algorytm Eliza.

%prep
%setup -q -n Chatbot-Eliza-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Chatbot
%define	pnam	Eliza
Summary:	Chatbot::Eliza Perl module - a clone of the classic Eliza program
Summary(pl):	Modu³ Perla Chatbot::Eliza - klon klasycznego programu Eliza
Name:		perl-Chatbot-Eliza
Version:	1.04
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	754199bbe591eaa11301aee108586fcd
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chatbot::Eliza Perl module implements classic Eliza algorithm.  The
original Eliza program was written by Joseph Weizenbaum and described
in the Communications of the ACM in 1966.  Eliza is a mock Rogerian
psychotherapist.  It prompts for user input, and uses a simple
transformation algorithm to change user input into a follow-up
question.  The program is designed to give the appearance of
understanding.

%description -l pl
Modu³ Perla Chatbot::Eliza stanowi implementacjê klasycznego algorytmu
Eliza. Oryginalny program Eliza zosta³ napisany przez Josepha
Weizenbauma i opisany w Communications of the ACM w 1966. Eliza jest
imitacj± zabawnego psychoterapeuty. Prosi u¿ytkownika o informacje i,
u¿ywaj±c prostego algorytmu transformacyjnego, zmienia informacje
u¿ytkownika w nastêpne pytanie. Program zaprojektowano aby
zaprezentowaæ rozumienie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *txt twobots
%dir %{perl_vendorlib}/Chatbot
%{perl_vendorlib}/Chatbot/Eliza.pm
%{_mandir}/man3/*

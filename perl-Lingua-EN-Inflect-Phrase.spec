%define upstream_name    Lingua-EN-Inflect-Phrase
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Inflect short English Phrases
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(Lingua::EN::Inflect::Number)
BuildRequires:	perl(Lingua::EN::Tagger)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Attempts to pluralize or singularize short English phrases.

If it doesn't work, please email or submit to RT the example you tried, and
I'll try to fix it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 655041
- rebuild for updated spec-helper

* Thu Apr 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 533029
- import perl-Lingua-EN-Inflect-Phrase


* Thu Apr 08 2010 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

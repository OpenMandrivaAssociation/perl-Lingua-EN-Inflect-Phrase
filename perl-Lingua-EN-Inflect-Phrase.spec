%define upstream_name    Lingua-EN-Inflect-Phrase
%define upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Inflect short English Phrases
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Lingua::EN::FindNumber)
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

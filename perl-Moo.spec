%define upstream_name    Moo
%define upstream_version 0.009008

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Efficient generation of subroutines via string eval
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Method::Modifiers)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(strictures)
BuildArch:	noarch

%description
This module is an extremely light-weight, high-performance the Moose
manpage replacement. It also avoids depending on any XS modules to allow
simple deployments. The name 'Moo' is based on the idea that it provides
almost -but not quite- two thirds of the Moose manpage.

Unlike 'Mouse' this module does not aim at full the Moose manpage
compatibility. See the /INCOMPATIBILITIES manpage for more details.

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
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.8-1mdv2011.0
+ Revision: 687049
- import perl-Moo


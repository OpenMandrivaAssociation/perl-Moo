%define upstream_name    Moo

Name:		perl-%{upstream_name}
Version:	2.005005
Release:	1

Summary:	Efficient generation of subroutines via string eval
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Moo
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl(Sub::Quote)
BuildRequires:	perl(Role::Tiny)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Devel::GlobalDestruction)
BuildRequires:	perl-devel
BuildRequires:	perl(Class::Method::Modifiers)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(strictures)
BuildArch:	noarch

%description
This module is an extremely light-weight, high-performance perl-Moose
replacement. It also avoids depending on any XS modules to allow
simple deployments. The name 'Moo' is based on the idea that it provides
almost -but not quite- two thirds of the Moose functionality.

Unlike 'Mouse' this module does not aim at full Moose compatibility.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

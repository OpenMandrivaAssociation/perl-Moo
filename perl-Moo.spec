%define upstream_name    Moo
%define upstream_version 0.009008

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Efficient generation of subroutines via string eval
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Method::Modifiers)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires: perl(strictures)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*



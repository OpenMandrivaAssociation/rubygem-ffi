%define oname ffi

Name:       rubygem-%{oname}
Version:    0.6.3
Release:    %mkrel 1
Summary:    A ruby extension for programmatically loading dynamic libraries
Group:      Development/Ruby
License:    LGPLv3
URL:        http://wiki.github.com/ffi/ffi
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(rake) >= 0.8.7
BuildRequires: rubygems
BuildRequires: ruby-devel
Provides:   rubygem(%{oname}) = %{version}

%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here[http://wiki.github.com/ffi/ffi/why-use-ffi].


%prep

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
cp -r .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

#install arch dependant files in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/*.so %{buildroot}%{ruby_sitearchdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.require_paths
%{ruby_gemdir}/gems/%{oname}-%{version}/gen/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/tasks/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/ffi_c.so
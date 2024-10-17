%define oname ffi

Name:       rubygem-%{oname}
Version:    1.0.11
Release:	6
Summary:    A ruby extension for programmatically loading dynamic libraries
Group:      Development/Ruby
License:    LGPLv3
URL:        https://wiki.github.com/ffi/ffi
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
Requires:   rubygems
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
mkdir -p .%{gem_dir}
gem install -V --local --install-dir .%{gem_dir} \
               --force --rdoc %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -r .%{gem_dir}/* %{buildroot}%{gem_dir}

rm -rf %{buildroot}%{gem_dir}/gems/%{oname}-%{version}/ext/

#install arch dependant files in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{gem_dir}/gems/%{oname}-%{version}/lib/*.so %{buildroot}%{ruby_sitearchdir}

%files
%dir %{gem_dir}/gems/%{oname}-%{version}/
%{gem_dir}/gems/%{oname}-%{version}/gen/
%{gem_dir}/gems/%{oname}-%{version}/lib/
%{gem_dir}/gems/%{oname}-%{version}/spec/
%{gem_dir}/gems/%{oname}-%{version}/tasks/
%doc %{gem_dir}/gems/%{oname}-%{version}/History.txt
%doc %{gem_dir}/gems/%{oname}-%{version}/LICENSE
%doc %{gem_dir}/gems/%{oname}-%{version}/Rakefile
%doc %{gem_dir}/gems/%{oname}-%{version}/README.rdoc
%doc %{gem_dir}/doc/%{oname}-%{version}
%{gem_dir}/cache/%{oname}-%{version}.gem
%{gem_dir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/ffi_c.so
%{gem_dir}/extensions/*/*/%{oname}-%{version}


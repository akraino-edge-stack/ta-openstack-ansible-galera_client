Name:           openstack-ansible-galera_client
Version:        17.0.2
Release:        1%{?dist}.1
License:        %{_platform_licence} and ASL 2.0
Source0:        https://github.com/openstack/%{name}/archive/%{version}.tar.gz
Patch0:         0001-initial.patch
Vendor:         %{_platform_vendor} and OpenStack modified
URL:            https://github.com/openstack/openstack-ansible-galera_client
BuildArch:      noarch
Summary:        openstack-ansible-galera_client
Requires:       openstack-ansible

%description
openstack-ansible-galera_client

%prep
%autosetup -n %{name}-%{version} -p 1

%build

%install
mkdir -p %{buildroot}/etc/ansible/roles/galera_client
rsync -av --exclude rpmbuild.spec --exclude .git/ --exclude .gitreview --exclude .eggs/ . %{buildroot}/etc/ansible/roles/galera_client/

%files
/etc/ansible/roles/galera_client


Name:           dmemcg-booster
Version:        0.1.2
Release:        1%{?dist}
Summary:        Dynamic memory cgroup booster for KDE Plasma

License:        GPLv3+
URL:            https://gitlab.steamos.cloud/holo/dmemcg-booster
Source0:        %{url}/-/archive/v%{version}/dmemcg-booster-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
# List the Qt and KDE Frameworks devel packages here:
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-kcoreaddons-devel

%description
A background service that dynamically manages memory cgroups to boost foreground gaming performance by evicting background application VRAM.

%prep
%autosetup -p1

%build
# The %cmake macro handles build directory creation and configuration
%cmake 
%cmake_build

%install
%cmake_install

# These macros safely handle enabling and starting the services during installation
%post
%systemd_post dmemcg-booster-system.service
%systemd_user_post dmemcg-booster-user.service

%preun
%systemd_preun dmemcg-booster-system.service
%systemd_user_preun dmemcg-booster-user.service

%postun
%systemd_postun_with_restart dmemcg-booster-system.service
%systemd_user_postun_with_restart dmemcg-booster-user.service

%files
%license LICENSE
%doc README.md
%{_bindir}/dmemcg-booster
%{_unitdir}/dmemcg-booster-system.service
%{_userunitdir}/dmemcg-booster-user.service

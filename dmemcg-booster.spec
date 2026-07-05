Name:           dmemcg-booster
Version:        0.1.2
Release:        1%{?dist}
Summary:        Service for enabling and controlling VRAM protection limits via dmem cgroups

License:        MIT
URL:            https://gitlab.steamos.cloud/holo/dmemcg-booster
Source0:        %{url}/-/archive/${version}/dmemcg-booster-${version}.tar.gz

BuildRequires:  cargo
BuildRequires:  libdrm-devel
BuildRequires:  systemd-rpm-macros

%description
A systemd service used for enabling and controlling DMEM cgroup limits for 
boosting foreground games. This activates the kernel's VRAM protection logic, 
ensuring that foreground applications (games) have first priority on VRAM and 
that background processes are evicted first during VRAM pressure.

%prep
# GitLab packs the root folder as 'dmemcg-booster-main' because it targets the main branch
%autosetup -n dmemcg-booster-main -p1

%build
cargo build --release

%install
# Create target system paths inside the clean buildroot environment
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_userunitdir}

# Copy the compiled Rust binary into the system binary path
install -m 0755 target/release/dmemcg-booster %{buildroot}%{_bindir}/dmemcg-booster

# Copy the systemd configuration files included in the source code
install -m 0644 dmemcg-booster-system.service %{buildroot}%{_unitdir}/dmemcg-booster-system.service
install -m 0644 dmemcg-booster-user.service %{buildroot}%{_userunitdir}/dmemcg-booster-user.service

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
%{_bindir}/dmemcg-booster
%{_unitdir}/dmemcg-booster-system.service
%{_userunitdir}/dmemcg-booster-user.service

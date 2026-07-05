Name:           plasma-foreground-booster
Version:        0.1.0
Release:        1%{?dist}
Summary:        KDE component to manipulate cgroups and boost foreground gaming apps

License:        LGPL-2.1-or-later
URL:            https://github.com/pixelcluster/kcgroups
# Referencing the tag directly because there's no semantic versioning.
Source0:        %{url}/archive/refs/tags/booster-dmemcg-experimental.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  plasma-workspace-devel

Provides:       kcgroups-dmemcg = %{version}-%{release}
Requires:       dmemcg-booster

%description
A KDE Plasma user-space companion utility that tracks the active window 
and dynamically moves foreground games into the dmemcg control group.

%prep
%autosetup -n kcgroups-booster-dmemcg-experimental

%build
# KDE/Qt projects usually require these build flags
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/plasma-foreground-booster
%{_userunitdir}/plasma-foreground-booster.service
%{_sysconfdir}/xdg/autostart/org.kde.foreground-booster.desktop

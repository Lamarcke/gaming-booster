Name:           kcgroups-dmemcg
Version:        0.1
Release:        1%{?dist}
Summary:        KDE cgroup library with DMEM cgroup support

License:        LGPL-2.1-or-later
URL:            https://github.com/pixelcluster/kcgroups
Source0:        %{url}/archive/refs/tags/kcgroups-dmemcg-experimental.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-devel
BuildRequires:  plasma-workspace-devel

%prep
%autosetup -n kcgroups-kcgroups-dmemcg-experimental

%build
%cmake -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%doc README.md
/usr/*

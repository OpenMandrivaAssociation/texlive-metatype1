Name:		texlive-metatype1
Version:	37105
Release:	2
Summary:	Generate Type 1 fonts from MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/metatype1
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metatype1.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metatype1.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The system employs scripts, common utility programs, and a set
of MetaPost macros to provide a means of expressing the details
outline fonts directly in the MetaPost language. The system was
employed to generate the Latin Modern fonts, and the
distribution includes an example development of Knuth's logo
fonts.

%prep
%autosetup -p1 -c -a2

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/metapost/metatype1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

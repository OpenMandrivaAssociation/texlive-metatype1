%global tl_name metatype1
%global tl_revision 37105

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.56
Release:	%{tl_revision}.1
Summary:	Generate Type 1 fonts from MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/metatype1
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metatype1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metatype1.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The system employs scripts, common utility programs, and a set of
MetaPost macros to provide a means of expressing the details outline
fonts directly in the MetaPost language. The system was employed to
generate the Latin Modern fonts, and the distribution includes an
example development of Knuth's logo fonts.


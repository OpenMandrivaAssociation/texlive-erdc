%global tl_name erdc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Style for Reports by US Army Corps of Engineers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/erdc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/erdc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/erdc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/erdc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A class for typesetting Technical Information Reports of the Engineer
Research and Development Center, US Army Corps of Engineers. The class
was commissioned and paid for by US Army Corps of Engineers, Engineer
Research and Development Center, 3909 Halls Ferry Road, Vicksburg, MS
39180-6199.


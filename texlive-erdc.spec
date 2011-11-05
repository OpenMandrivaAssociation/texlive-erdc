# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/erdc
# catalog-date 2009-11-09 22:14:03 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-erdc
Version:	1.1
Release:	1
Summary:	Style for Reports by US Army Corps of Engineers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/erdc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erdc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erdc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erdc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A class for typesetting Technical Information Reports of the
Engineer Research and Development Center, US Army Corps of
Engineers. The class was commissioned and paid for by US Army
Corps of Engineers, Engineer Research and Development Center,
3909 Halls Ferry Road, Vicksburg, MS 39180-6199.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/erdc/erdc.cls
%doc %{_texmfdistdir}/doc/latex/erdc/README
%doc %{_texmfdistdir}/doc/latex/erdc/erdc.bib
%doc %{_texmfdistdir}/doc/latex/erdc/erdc.pdf
%doc %{_texmfdistdir}/doc/latex/erdc/nola.eps
%doc %{_texmfdistdir}/doc/latex/erdc/nola.pdf
%doc %{_texmfdistdir}/doc/latex/erdc/red_corps_castle2.eps
%doc %{_texmfdistdir}/doc/latex/erdc/red_corps_castle2.pdf
%doc %{_texmfdistdir}/doc/latex/erdc/sample.pdf
%doc %{_texmfdistdir}/doc/latex/erdc/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/erdc/Makefile
%doc %{_texmfdistdir}/source/latex/erdc/erdc.dtx
%doc %{_texmfdistdir}/source/latex/erdc/erdc.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

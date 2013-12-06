# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/erdc
# catalog-date 2009-11-09 22:14:03 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-erdc
Version:	1.1
Release:	5
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

%description
A class for typesetting Technical Information Reports of the
Engineer Research and Development Center, US Army Corps of
Engineers. The class was commissioned and paid for by US Army
Corps of Engineers, Engineer Research and Development Center,
3909 Halls Ferry Road, Vicksburg, MS 39180-6199.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751541
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718360
- texlive-erdc
- texlive-erdc
- texlive-erdc
- texlive-erdc


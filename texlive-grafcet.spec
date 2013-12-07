# revision 22509
# category Package
# catalog-ctan /graphics/pgf/contrib/grafcet
# catalog-date 2011-05-17 01:53:44 +0200
# catalog-license lppl1
# catalog-version 1.3.5
Name:		texlive-grafcet
Version:	1.3.5
Release:	4
Summary:	Draw Grafcet/SFC with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/grafcet
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grafcet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grafcet.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a library (GRAFCET) that can draw
Grafcet/SFC diagrams, in accordance with EN 60848, using
Pgf/TikZ. L'objectif de la librairie GRAFCET est de permettre
le trace de grafcet selon la norme EN~60848 a partir de
Pgf/TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/grafcet/grafcet.sty
%doc %{_texmfdistdir}/doc/latex/grafcet/README
%doc %{_texmfdistdir}/doc/latex/grafcet/grafcet.pdf
%doc %{_texmfdistdir}/doc/latex/grafcet/grafcet.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3.5-2
+ Revision: 752372
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3.5-1
+ Revision: 718576
- texlive-grafcet
- texlive-grafcet
- texlive-grafcet
- texlive-grafcet


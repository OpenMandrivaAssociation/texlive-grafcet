# revision 22509
# category Package
# catalog-ctan /graphics/pgf/contrib/grafcet
# catalog-date 2011-05-17 01:53:44 +0200
# catalog-license lppl1
# catalog-version 1.3.5
Name:		texlive-grafcet
Version:	1.3.5
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a library (GRAFCET) that can draw
Grafcet/SFC diagrams, in accordance with EN 60848, using
Pgf/TikZ. L'objectif de la librairie GRAFCET est de permettre
le trace de grafcet selon la norme EN~60848 a partir de
Pgf/TikZ.

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
%{_texmfdistdir}/tex/latex/grafcet/grafcet.sty
%doc %{_texmfdistdir}/doc/latex/grafcet/README
%doc %{_texmfdistdir}/doc/latex/grafcet/grafcet.pdf
%doc %{_texmfdistdir}/doc/latex/grafcet/grafcet.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

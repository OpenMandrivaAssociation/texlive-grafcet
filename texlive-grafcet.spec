Name:		texlive-grafcet
Version:	22509
Release:	1
Summary:	Draw Grafcet/SFC with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/grafcet
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grafcet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grafcet.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

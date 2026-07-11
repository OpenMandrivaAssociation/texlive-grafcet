%global tl_name grafcet
%global tl_revision 22509

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.5
Release:	%{tl_revision}.1
Summary:	Draw Grafcet/SFC with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/grafcet
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grafcet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grafcet.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a library (GRAFCET) that can draw Grafcet
Sequential Function Chart (SFC) diagrams, in accordance with EN 60848,
using Pgf/TikZ. L'objectif de la librairie GRAFCET est de permettre le
trace de grafcet selon la norme EN 60848 a partir de Pgf/TikZ.


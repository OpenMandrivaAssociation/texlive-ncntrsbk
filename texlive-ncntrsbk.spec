# revision 31835
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2012-06-06 22:57:48 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-ncntrsbk
Version:	20120606
Release:	3
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ncntrsbk.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/ncntrsbk/config.unc
%{_texmfdistdir}/fonts/afm/adobe/ncntrsbk/pncb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/ncntrsbk/pncbi8a.afm
%{_texmfdistdir}/fonts/afm/adobe/ncntrsbk/pncr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/ncntrsbk/pncri8a.afm
%{_texmfdistdir}/fonts/afm/urw/ncntrsbk/uncb8a.afm
%{_texmfdistdir}/fonts/afm/urw/ncntrsbk/uncbi8a.afm
%{_texmfdistdir}/fonts/afm/urw/ncntrsbk/uncr8a.afm
%{_texmfdistdir}/fonts/afm/urw/ncntrsbk/uncri8a.afm
%{_texmfdistdir}/fonts/map/dvips/ncntrsbk/unc.map
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbi.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbi8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncri.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncri7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncri8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncri8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncri8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ncntrsbk/pncro8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk/uncro8t.tfm
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncb8a.pfm
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncbi8a.pfb
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncbi8a.pfm
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncr8a.pfm
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncri8a.pfb
%{_texmfdistdir}/fonts/type1/urw/ncntrsbk/uncri8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncb.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbc.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbi.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbi8t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbo.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncr.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncrc.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncri.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncri7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncri8c.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncri8t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncro.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/ncntrsbk/pncro8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/ncntrsbk/uncro8t.vf
%{_texmfdistdir}/tex/latex/ncntrsbk/8runc.fd
%{_texmfdistdir}/tex/latex/ncntrsbk/omlunc.fd
%{_texmfdistdir}/tex/latex/ncntrsbk/omsunc.fd
%{_texmfdistdir}/tex/latex/ncntrsbk/ot1unc.fd
%{_texmfdistdir}/tex/latex/ncntrsbk/t1unc.fd
%{_texmfdistdir}/tex/latex/ncntrsbk/ts1unc.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}

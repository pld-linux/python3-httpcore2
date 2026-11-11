Summary:	A minimal low-level HTTP client
Summary(pl.UTF-8):	Minimalny, niskopoziomowy klient HTTP
Name:		python3-httpcore2
Version:	2.16.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/httpcore2/
Source0:	https://files.pythonhosted.org/packages/source/h/httpcore2/httpcore2-%{version}.tar.gz
# Source0-md5:	118785ac17d5a4d0b9122f998ee2f705
URL:		https://github.com/pydantic/httpx2
BuildRequires:	python3-build
BuildRequires:	python3-hatch-fancy-pypi-readme
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-uv-dynamic-versioning >= 0.14.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTPCore 2 is a maintained fork of HTTP Core. It provides a minimal
low-level HTTP client, which does one thing only: sending HTTP
requests.

It does not provide any high level model abstractions over the API,
does not handle redirects, multipart uploads, building authentication
headers, transparent HTTP caching, URL parsing, session cookie
handling, content or charset decoding, handling JSON, environment
based configuration defaults, or any of that Jazz.

Some things HTTPCore 2 does do:
- Sending HTTP requests.
- Thread-safe / task-safe connection pooling.
- HTTP(S) proxy & SOCKS proxy support.
- Supports HTTP/1.1 and HTTP/2.
- Provides both sync and async interfaces.
- Async backend support for asyncio and trio.

%description -l pl.UTF-8
HTTPCore 2 to utrzymywane odgałęzienie pakietu HTTP Core. Udostępnia
minimalnego, niskopoziomowego klienta HTTP, wykonującego tylko jedną
rzecz: wysyłanie żądań HTTP.

Nie dostarcza żadnych wysokopoziomowych abstrakcji modelu na API, nie
obsługuje przekierowań, przesyłania wieloczęściowego, tworzenia
nagłówków uwierzytelniających, przezroczystego buforowania HTTP,
analizy URL-i, obsługi ciasteczek sesyjnych, dekodowania treści czy
zestawów znaków, obsługi JSON-a, ustawień domyślnych konfiguracji itd.

Niektóre zadania, które HTTPCore 2 wykonuje:
- wysyłanie żądań HTTP
- pula połączeń bezpieczna pod kątem wątków
- obsługa proxy HTTP(S) i SOCKS
- obsługa HTTP/1.1 i HTTP/2
- interfejs synchroniczny i asynchroniczny
- obsługa backendu asynchronicznego dla asyncio i trio

%prep
%setup -q -n httpcore2-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.md README.md
%{py3_sitescriptdir}/httpcore2
%{py3_sitescriptdir}/httpcore2-%{version}.dist-info

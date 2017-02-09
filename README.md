Przeznaczenie repozytorium
==========================

Ze względu na pomysł budowy Platformy aplikacje.gov.pl w architekturze
mikroserwisów, planujemy zbudować testową aplikację wraz z zaślepkami
emulującymi potrzebne jej mikroserwisy które powstaną w przyszłości.

Dzięki temu, w przyszłości aplikacje będą mogły powstawać niezależnie od
potrzebnych im usług takich jak dziennik zdarzeń, powiadomienia, mechanizm
rejestrów - jedynym warunkiem będzie to, żeby nowopowstająca, produkcyjna usługa
zapewniająca wymagane funkcje, posiadała identyczne API co zaślepka.

Pierwsze aplikacje będą napisane w Pythonie i mikroframeworku Flask, ze względu
na ich łatwość użycia do szybkich eksperymentów. Nie stanowi to jednak oceny
przydatności innych technologii - równouprawnione będą eksperymenty w Pythonie,
w Javie, w Perlu, w Haskellu i w Erlangu.

# Słowniczek
* Aplikacja (app): mikroserwis udostępniający funkcje dla użytkownika. Aplikacja
  może również udostępniać funkcje pozostałym aplikacjom.
* Usługa (service): mikroserwis udostępniający funkcje dla pozostałych aplikacji

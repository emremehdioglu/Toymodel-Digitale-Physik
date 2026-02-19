# Toy Model: Ressourcenbasierter zellulärer Automat

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18698818.svg)](https://doi.org/10.5281/zenodo.18698818)

Dieses Repository enthält die formale Spezifikation sowie die **prototypische Python-Implementierung** eines hochkomplexen, deterministischen zellulären Automaten. Das Modell untersucht, wie aus streng limitierten lokalen Rechenbudgets und Erhaltungsregeln physikähnliche Eigenschaften emergieren.

## 🔹 Über das Projekt

Im Gegensatz zu klassischen zellulären Automaten folgt dieses Universum den Prinzipien einer Ressourcen-Ökonomie:

* **Zeit als lokale Ressource:** Jede Zelle besitzt ein festes Rechenbudget. Hohe lokale Dichte führt zur Verlangsamung der Eigenzeit (delta_tau) – ein Effekt analog zur relativistischen Zeitdilatation.
* **Eiserne Buchhaltung:** Eine konservierte Größe („Bilanz“) bleibt global invariant. Keine Substanz geht verloren, sie wird nur lokal umverteilt.
**Logikbasierte Physik:** Lokale Informationszustände steuern direkt physikalische Wirkungen.

Dieses Modell steht in der Tradition der digitalen Physik (Konrad Zuse, Edward Fredkin) und zellulärer Automaten (Stephen Wolfram).

**🛠️ Die Simulation** (simulation.py)

Der beigefügte Code dient als Machbarkeitsnachweis für die mathematische Konsistenz:

* **Invarianz-Check:** Bestätigt mathematisch, dass die globale Bilanz über alle Zeit-Ticks exakt erhalten bleibt.
* **Visualisierung:** Erzeugt eine Gegenüberstellung von Ressourcendichte (rho) und der daraus resultierenden Eigenzeit-Struktur.

## Mathematische Grundlage

Die Eigenzeit wird im Code wie folgt berechnet:
`delta_tau = max(0, 1 - rho / rho_max)`

## Installation & Nutzung

1. Benötigte Bibliotheken installieren:
   `pip install numpy matplotlib`

2. Simulation starten:
   `python simulation.py`

## Zitation

Falls Sie dieses Modell oder den Code in Ihrer Forschung verwenden, zitieren Sie bitte die offizielle DOI:
**10.5281/zenodo.18698818**

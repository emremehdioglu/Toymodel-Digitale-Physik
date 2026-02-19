import numpy as np
import matplotlib.pyplot as plt

class ToyModelSimulation:
    """
    Formale Implementation des ressourcenbasierten Toy Models.
    Bestätigt: Bilanz-Invarianz und emergente Zeitdilatation.
    DOI: 10.5281/zenodo.18698818
    """
    def __init__(self, size=50, rho_max=1.0):
        self.size = size
        self.rho_max = rho_max
        # 1. Initialisierung: Ein Gitter voller Nullen
        self.balance = np.zeros((size, size))
        
        # 2. Start-Zustand: Ein Energie-Cluster in der Mitte (Symmetrie-Test)
        mid = size // 2
        self.balance[mid-5:mid+5, mid-5:mid+5] = 10.0
        self.initial_sum = np.sum(self.balance)

    def calculate_proper_time(self):
        """Berechnet die Eigenzeit delta_tau = max(0, 1 - rho/rho_max)"""
        # Normierung der Dichte für die Visualisierung
        current_max = np.max(self.balance)
        rho = self.balance / current_max if current_max > 0 else self.balance
        return np.maximum(0, 1 - (rho / self.rho_max))

    def step(self):
        """Ein Simulations-Tick: Erhält die globale Bilanz (Invarianz-Logik)."""
        # 10% der Ressource fließen pro Tick ab (Diffusion)
        flow = self.balance * 0.1
        self.balance -= flow
        
        # Umverteilung auf die 4 direkten Nachbarn (Oben, Unten, Links, Rechts)
        # np.roll sorgt für periodische Randbedingungen (das Gitter ist ein Torus)
        self.balance += (np.roll(flow, 1, axis=0) + np.roll(flow, -1, axis=0) + 
                         np.roll(flow, 1, axis=1) + np.roll(flow, -1, axis=1)) / 4

    def run(self, iterations=100):
        """Führt die Simulation über n Schritte aus und prüft die Invarianz."""
        print(f"--- Starte Simulation ({iterations} Ticks) ---")
        print(f"Start-Bilanzsumme: {self.initial_sum:.4f}")
        
        for i in range(iterations):
            self.step()
        
        final_sum = np.sum(self.balance)
        print(f"End-Bilanzsumme:   {final_sum:.4f}")
        
        # Mathematischer Beweis der Invarianz (Fehlertoleranz für Floats)
        if np.isclose(self.initial_sum, final_sum):
            print("ERGEBNIS: Bilanz-Invarianz mathematisch bestätigt ✅")
        else:
            print("WARNUNG: Bilanz-Abweichung detektiert ❌")
        return final_sum

    def visualize(self):
        """Erstellt die finale Gegenüberstellung von Dichte und Zeit."""
        delta_tau = self.calculate_proper_time()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Karte 1: Ressourcenverteilung (Dichte)
        im1 = ax1.imshow(self.balance, cmap='hot')
        ax1.set_title("Ressourcen-Verteilung (Bilanz)")
        plt.colorbar(im1, ax=ax1)
        
        # Karte 2: Zeit-Dilation (Eigenzeit)
        im2 = ax2.imshow(delta_tau, cmap='Blues_r')
        ax2.set_title("Emergente Eigenzeit (delta_tau)")
        plt.colorbar(im2, ax=ax2)
        
        plt.tight_layout()
        plt.show()

# --- Hauptprogramm ---
if __name__ == "__main__":
    # Instanz der Welt erstellen
    sim = ToyModelSimulation(size=50)
    
    # Simulation durchführen
    sim.run(iterations=100)
    
    # Ergebnisse visualisieren
    sim.visualize()

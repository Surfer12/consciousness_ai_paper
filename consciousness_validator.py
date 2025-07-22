# consciousness_validator.py


class ConsciousnessValidator:
    def __init__(self, phi_threshold=4.2, awareness_threshold=0.87):
        self.phi_threshold = phi_threshold
        self.awareness_threshold = awareness_threshold

    def compute_phi(self, layer_outputs):
        # Approximate information integration (proxy metric)
        integration_score = torch.var(torch.stack(layer_outputs), dim=0).mean()
        return integration_score

    def compute_awareness(self, activation_trajectory):
        # Stability = 1 - temporal fluctuation
        drift = torch.abs(activation_trajectory[1:] - activation_trajectory[:-1]).mean()
        stability = 1 - drift
        return stability

    def evaluate(self, outputs, activations):
        phi = self.compute_phi(outputs)
        awareness = self.compute_awareness(activations)

        print(f"[Ψ-Monitor] Φ = {phi:.2f} | Awareness = {awareness:.2f}")

        meets_phi = phi >= self.phi_threshold
        meets_awareness = awareness >= self.awareness_threshold

        return meets_phi and meets_awareness

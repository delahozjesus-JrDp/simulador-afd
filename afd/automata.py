class AutomataFinitoDeterminista:
    """Modelo de un AFD M = (Q, Sigma, delta, q0, F)."""

    def __init__(self, estados, alfabeto, transiciones,
                 estado_inicial, estados_finales):
        self.estados = list(estados)
        self.alfabeto = list(alfabeto)
        self.transiciones = dict(transiciones)
        self.estado_inicial = estado_inicial
        # Se conserva como conjunto para comprobar aceptación eficientemente.
        self.estados_finales = set(estados_finales)

    def obtener_estado_siguiente(self, estado, simbolo):
        """Aplica delta(estado, simbolo)."""
        return self.transiciones[(estado, simbolo)]

    def reconocer_palabra(self, palabra):
        """Procesa una palabra y devuelve aceptación, motivo y recorrido."""
        estado_actual = self.estado_inicial
        recorrido = [estado_actual]

        for posicion, simbolo in enumerate(palabra, start=1):
            if simbolo not in self.alfabeto:
                return {
                    "aceptada": False,
                    "motivo": "simbolo_invalido",
                    "simbolo_invalido": simbolo,
                    "posicion": posicion,
                    "recorrido": recorrido,
                    "estado_final": estado_actual,
                }

            estado_actual = self.obtener_estado_siguiente(estado_actual, simbolo)
            recorrido.append(estado_actual)

        aceptada = estado_actual in self.estados_finales
        return {
            "aceptada": aceptada,
            "motivo": "aceptada" if aceptada else "no_aceptada",
            "simbolo_invalido": None,
            "posicion": None,
            "recorrido": recorrido,
            "estado_final": estado_actual,
        }

    def obtener_5_tupla(self):
        return {
            "Q": self.estados,
            "Sigma": self.alfabeto,
            "delta": self.transiciones,
            "q0": self.estado_inicial,
            "F": [e for e in self.estados if e in self.estados_finales],
        }

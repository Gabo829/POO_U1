from dataclasses import dataclass

@dataclass
class Temperatura:
    valor_celsius: float
    tecnico_nombre: str
    
    def es_congelacion(self) -> bool:
        return self.valor_celsius <= 0
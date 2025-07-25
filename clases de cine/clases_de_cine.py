class SalaCine:
    def _init_(self, capacidad_total, precio_asiento):
        self.capacidad_total = capacidad_total
        self.precio_asiento = precio_asiento
        self.asientos_reservados = 0

    def reservar_asientos(self, cantidad):
        if cantidad <= self.asientos_disponibles():
            self.asientos_reservados += cantidad
            total_bs = cantidad * self.precio_asiento
            print(f" {cantidad} asiento(s) reservado(s). Total: Bs. {total_bs}")
        else:
            print(" No hay suficientes asientos disponibles.")

    def asientos_disponibles(self):
        return self.capacidad_total - self.asientos_reservados

    def mostrar_estado(self):
        print(f" Asientos disponibles: {self.asientos_disponibles()}")
        print(f" Total recaudado: Bs. {self.asientos_reservados * self.precio_asiento}")

# Ejemplo de uso
sala = SalaCine(capacidad_total=50, precio_asiento=30)

sala.mostrar_estado()
sala.reservar_asientos(5)
sala.mostrar_estado()
sala.reservar_asientos(48)  # Esto debería mostrar un error por falta de asientos
#daniel alanes caceres13

class Empleado:
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, supervisor=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("DNI:", self.dni)
        print("Dirección:", self.direccion)
        print("Teléfono:", self.telefono)
        print("Salario:", self.salario)
        if self.supervisor:
            print("Supervisor:", self.supervisor.nombre)

    def cambiar_supervisor(self, nuevo_supervisor):
        self.supervisor = nuevo_supervisor

    def incrementar_salario(self):
        pass


class Secretario(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, numero_fax):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.despacho = despacho
        self.numero_fax = numero_fax

    def imprimir(self):
        super().imprimir()
        print("Puesto: Secretario")
        print("Despacho:", self.despacho)
        print("Número de Fax:", self.numero_fax)

    def incrementar_salario(self):
        self.salario *= 1.05


class Vendedor(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, coche, telefono_movil, area_venta, porcentaje_comision):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.coche = coche
        self.telefono_movil = telefono_movil
        self.area_venta = area_venta
        self.clientes = []
        self.porcentaje_comision = porcentaje_comision

    def imprimir(self):
        super().imprimir()
        print("Puesto: Vendedor")
        print("Coche:", self.coche)
        print("Teléfono Móvil:", self.telefono_movil)
        print("Área de Venta:", self.area_venta)

    def dar_alta_cliente(self, cliente):
        self.clientes.append(cliente)

    def dar_baja_cliente(self, cliente):
        self.clientes.remove(cliente)

    def cambiar_coche(self, nuevo_coche):
        self.coche = nuevo_coche

    def incrementar_salario(self):
        self.salario *= 1.10


class JefeZona(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, secretario, coche):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.despacho = despacho
        self.secretario = secretario
        self.vendedores = []
        self.coche = coche

    def imprimir(self):
        super().imprimir()
        print("Puesto: Jefe de Zona")
        print("Despacho:", self.despacho)
        print("Secretario a Cargo:", self.secretario.nombre)
        print("Vendedores a Cargo:")
        for vendedor in self.vendedores:
            print("-", vendedor.nombre)

    def cambiar_secretario(self, nuevo_secretario):
        self.secretario = nuevo_secretario

    def dar_alta_vendedor(self, vendedor):
        self.vendedores.append(vendedor)

    def dar_baja_vendedor(self, vendedor):
        self.vendedores.remove(vendedor)

    def cambiar_coche(self, nuevo_coche):
        self.coche = nuevo_coche

    def incrementar_salario(self):
        self.salario *= 1.20


# Programa de prueba
if __name__ == "__main__":
    secretario1 = Secretario("Juan", "Perez", "12345678A", "Calle Mayor 1", "123456789", 1500, "Despacho 1", "123456")
    vendedor1 = Vendedor("Pedro", "Gomez", "87654321B", "Calle Menor 2", "987654321", 2000, "ABC123", "654321987", "Zona Norte", 0.05)
    vendedor2 = Vendedor("María", "López", "56789012C", "Calle Pequeña 3", "456789012", 2200, "DEF456", "987654321", "Zona Sur", 0.07)
    jefe_zona1 = JefeZona("Luis", "Martinez", "34567890D", "Calle Grande 4", "789012345", 3000, "Despacho 2", secretario1, "GHI789")

    secretario1.incrementar_salario()
    vendedor1.incrementar_salario()
    vendedor2.incrementar_salario()
    jefe_zona1.incrementar_salario()

    print("Datos del Secretario:")
    secretario1.imprimir()
    print("\nDatos del Vendedor 1:")
    vendedor1.imprimir()
    print("\nDatos del Vendedor 2:")
    vendedor2.imprimir()
    print("\nDatos del Jefe de Zona:")
    jefe_zona1.imprimir()
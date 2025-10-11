import pandapower as pp

# Crear la red
net = pp.create_empty_network()

# Nodos de la red
bus_grid = pp.create_bus(net, vn_kv=110, name="Red Principal")
bus_park = pp.create_bus(net, vn_kv=20, name="Parque Solar")
bus_load = pp.create_bus(net, vn_kv=20, name="Carga Rural")

# Elementos de la red
pp.create_ext_grid(net, bus_grid, vm_pu=1.02)  # Conexión a la red principal
pp.create_line(net, from_bus=bus_grid, to_bus=bus_park, length_km=15,
               std_type="NAYY 4x150 SE")
pp.create_line(net, from_bus=bus_park, to_bus=bus_load, length_km=5,
               std_type="NAYY 4x70 SE")

# Generación solar y carga
pp.create_sgen(net, bus_park, p_mw=10, q_mvar=0, name="Parque Solar")
pp.create_load(net, bus_load, p_mw=8, q_mvar=2, name="Carga Rural")

# Simulación de flujo de potencia
pp.runpp(net)
print(net.res_bus)
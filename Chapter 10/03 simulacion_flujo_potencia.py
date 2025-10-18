import pandapower as pp

# Crear la red
net = pp.create_empty_network()

# Nodos
bus1 = pp.create_bus(net, vn_kv=20, name="Nodo 1")
bus2 = pp.create_bus(net, vn_kv=0.4, name="Nodo 2")

# Elementos de la red
pp.create_ext_grid(net, bus1, vm_pu=1.02, name="Red Externa")  # Conexión externa
pp.create_transformer(net, bus1, bus2, std_type="0.4 MVA 20/0.4 kV")

# Carga y generación distribuida
pp.create_load(net, bus2, p_mw=0.1, q_mvar=0.05, name="Carga")
pp.create_sgen(net, bus2, p_mw=0.05, q_mvar=0, name="Generación Solar")

# Simulación
pp.runpp(net)

# Resultados
print(net.res_bus)
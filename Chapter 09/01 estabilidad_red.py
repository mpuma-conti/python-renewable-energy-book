import pandapower as pp

# Crear un sistema eléctrico simple
net = pp.create_empty_network()

# Agregar nodos
bus1 = pp.create_bus(net, vn_kv=20)
bus2 = pp.create_bus(net, vn_kv=0.4)

# Agregar generador renovable
pp.create_gen(net, bus1, p_mw=5, vm_pu=1.02)

# Agregar una carga
pp.create_load(net, bus2, p_mw=3, q_mvar=0.5)

# Crear línea entre nodos
pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=1,
               std_type="NAYY 4x50 SE")

# Simular flujo de carga
pp.runpp(net)
print(net.res_bus)
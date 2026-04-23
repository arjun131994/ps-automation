from simulation import SimulatedPowerSupply

def test_voltage_set():
    ps = SimulatedPowerSupply()
    ps.set_voltage(5)
    assert ps.read_voltage() == 5

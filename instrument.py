import pyvisa

class PowerSupply:
    def __init__(self, address):
        rm = pyvisa.ResourceManager()
        self.ps = rm.open_resource(address)

    def set_voltage(self, v):
        self.ps.write(f"VOLT {v}")

    def output_on(self):
        self.ps.write("OUTP ON")
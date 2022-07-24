# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### L1-D1: Test for MUX2 ########')

    for i in range(31):
        
        in_data = i % 4

        for ii in dut:
            if (str(ii._name) == str('inp'+str(i))):
                test_input = ii._name
        
        dut._sub_handles[test_input].value = in_data
        dut.sel.value = i

        await Timer(10, units='ns')

        dut._log.info(f'inp{i:05}={in_data:05} sel={i:05} Model={in_data:05} DUT={int(dut.out.value):05}')
        assert int(dut.out.value) == int(in_data), "Mux select circuit failed with:\
        Sel: {A} -> Expected {B} - Current {C}".format(A=int(i),
        B=int(in_data), C=int(dut.out.value))


import pytest


class Test_Ts1_001:
    @pytest.mark.skip
    def test_add(self,setup1, setup3, setup4):
        print("add")

    @pytest.mark.skipif(5>3, reason="condition becomes true so skippingthe TC")
    def test_sub(self):
        print("sub")

    @pytest.mark.sanity
    def test_mul(self, setup2):
        print(setup2)
        var1, var2=setup2
        print(var1)
        print(var2)
        print("multiplication")


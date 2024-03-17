import pytest
class Test_Ts2_002:
    @pytest.mark.functionality
    @pytest.mark.parametrize("var",[1,2,3,4,5,6,7,8])
    # @pytest.mark.parametrize("var1,var2",[(1,2),(2,3),(3,4)])
    def test_greater(self, var, setup2, setup3, setup4):
        print(f"variables from paramenterize", var)
        print("Greater")


    @pytest.mark.parametrize("var1,var2,var3",[(1,2,3),(2,3,4),(3,4,5)])
    def test_greater1(self, var1, var2, var3, setup2, setup3, setup4):
        print(f"variables from paramenterize", var1,var2, var3)
        print("Greater")

    @pytest.mark.functionality
    @pytest.mark.sanity
    def test_lesser(self, setup2):
        print("Lesser")

    @pytest.mark.sanity
    @pytest.mark.xfail
    def test_equal(self, setup1):
        print("Equal")
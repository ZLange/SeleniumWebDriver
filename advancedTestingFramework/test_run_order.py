# run pytests in specific order
# installed -> pip3 install pytest-ordering

import pytest


# B, A, C, E, D, F
@pytest.mark.run(order=2)
def test_run_order_methoda(onetimesetup, setup):
    print("Running method A")


@pytest.mark.run(order=1)
def test_run_order_methodb(onetimesetup, setup):
    print("Running method B")


@pytest.mark.run(order=3)
def test_run_order_methodc(onetimesetup, setup):
    print("Running method C")


@pytest.mark.run(order=5)
def test_run_order_methodd(onetimesetup, setup):
    print("Running method D")


@pytest.mark.run(order=4)
def test_run_order_methode(onetimesetup, setup):
    print("Running method E")


@pytest.mark.run(order=6)
def test_run_order_methodf(onetimesetup, setup):
    print("Running method F")

# does not work for now
# @pytest.mark.run(after="test_second")
# def test_third(onetimesetup, setup):
#     print("Running third")
# def test_second(onetimesetup, setup):
#     print("Running second")
#
# @pytest.mark.run(before="test_second")
# def test_first(onetimesetup, setup):
#     print("Running first")

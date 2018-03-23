#from regression_tests import *
import os
from utils import multicall, constants

def test_max():
    pathName = os.path.join(constants.seeds_dir, 'max.js')
    res = multicall.callAll(pathName)
    assert 67 == int(res.jsc_outerr)
    assert 67 == int(res.chakra_outerr)
    assert 67 == int(res.spiderm_outerr)
    assert 67 == int(res.v8_outerr)

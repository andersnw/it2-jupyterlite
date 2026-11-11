import priser

def test_billettpris_barn_ungdom():
    assert priser.billettpris(6) == 63
    assert priser.billettpris(10) == 63
    assert priser.billettpris(17) == 63

def test_billettpris_voksen():
    assert priser.billettpris(18) == 157
    assert priser.billettpris(50) == 157
    assert priser.billettpris(66) == 157

def test_billettpris_honnør():
    assert priser.billettpris(67) == 79
    assert priser.billettpris(80) == 79
    assert priser.billettpris(130) == 79
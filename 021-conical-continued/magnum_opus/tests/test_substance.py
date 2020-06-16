from magnumopus.models.substance import Substance

def test_can_cook_substance():
    substance = Substance()

    result = substance.cook()

    assert substance.state == ['cooked']

def test_can_wash_substance():
    substance = Substance()

    result = substance.wash()

    assert result.state == ['washed']

def test_can_pickle_substance():
    substance = Substance()

    result = substance.pickle()

    assert result.state == ['pickled']

def test_can_ferment_substance():
    substance = Substance()

    result = substance.ferment()

    assert substance.state == ['fermented']

def test_can_cook_and_ferment_substance():
    substance = Substance()

    result = substance.cook()
    result = result.ferment()

    assert substance.state == ['cooked', 'fermented']

def test_the_order_of_processes_applied_to_a_substance_matters():
    substance1 = Substance()
    result1 = substance1.cook()
    result1 = result1.ferment()

    substance2 = Substance()
    result2 = substance2.ferment()
    result2 = result2.cook()

    assert result1.state != result2.state
    assert result1.state == result2.state[::-1]

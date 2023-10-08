import pytest


@pytest.mark.usefixtures('test_fixture1')
def test_google():
        pass

@pytest.mark.p
def test_facebook():
        pass
@pytest.mark.usefixtures('test_fixture1')
def test_apple():
        pass

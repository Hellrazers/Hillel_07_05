import logging

import pytest
logger = logging.getLogger("test")


@pytest.mark.smoke
def test_1():
	logger.info("test")

@pytest.mark.smoke

def test_2():
	logger.info("test")

@pytest.mark.smoke

def test_3():
	logger.info("test")

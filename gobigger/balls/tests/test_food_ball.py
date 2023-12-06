import logging
import pytest
import uuid
from pygame.math import Vector2
from easydict import EasyDict

from gobigger.balls import FoodBall
from gobigger.utils import Border

logging.basicConfig(level=logging.DEBUG)

@pytest.mark.unittest
class TestFoodBall:

    def test_naive(self):
        ball_id = uuid.uuid1()
        border = Border(0, 0, 100, 100)
        position = Vector2(10, 10)
        food_ball = FoodBall(ball_id, position, border=border, score=1)
        assert True

    def test_default_config(self):
        assert isinstance(FoodBall.default_config(), EasyDict)

    def test_move(self):
        ball_id = uuid.uuid1()
        border = Border(0, 0, 100, 100)
        position = Vector2(10, 10)
        food_ball = FoodBall(ball_id, position, border=border, score=1)
        food_ball.move(direction=None, duration=None)

    def test_eat(self):
        ball_id = uuid.uuid1()
        border = Border(0, 0, 100, 100)
        position = Vector2(10, 10)
        food_ball = FoodBall(ball_id, position, border=border, score=1)
        food_ball.eat(ball=None)
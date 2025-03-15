# Imports:
import pygame, random

from src.player.player import *
from src.sprites.backgroundSprite import BackgroundSprite
from src.sprites.textSprite import TextSprite
from src.scripts.background import drawBackground
from src.scripts.ground import drawGround
from src.scripts.events import *
import src.settings.defaultSettings as ds

from src.scripts.updateLoop import updateWindow

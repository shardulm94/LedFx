from ledfx.effects.temporal import TemporalEffect
from ledfx.effects.gradient import GradientEffect
#from ledfx.color import COLORS, GRADIENTS
#from ledfx.effects import Effect
import voluptuous as vol
import numpy as np
import logging

class FadeEffect(TemporalEffect, GradientEffect):
    """
    Fades through the colours of a gradient
    """

    NAME = "Fade"

    CONFIG_SCHEMA = vol.Schema({
        vol.Optional('speed', default = 0.5, description="Speed of the effect"): vol.Coerce(float),
    })

    def config_updated(self, config):
        self.idx = 0
        self.forward = True

    def effect_loop(self):
        self.idx += 0.0015
        if self.idx > 1:
            self.idx = 1
            self.forward = not self.forward
        self.idx = self.idx % 1

        if self.forward:
            i = self.idx
        else:
            i = 1-self.idx        

        color = self.get_gradient_color(i)
        self.pixels = np.tile(color, (self.pixel_count, 1))
from classes.config import config as Config
from generator.settings import Settings

DEFAULT_DENSITY = float(Config.get('placeObjectSettings', 'default_density'))
DEFAULT_CLUMPING = float(Config.get('placeObjectSettings', 'default_clumping'))
DEFAULT_RANDOM_NUDGE_ENABLED = bool(Config.getboolean('placeObjectSettings', 'random_nudge_enabled'))
DEFAULT_RANDOM_ROTATION_ENABLED = bool(Config.getboolean('placeObjectSettings', 'random_rotation_enabled'))
DEFAULT_HEIGHT_BASED_ENABLED = bool(Config.getboolean('placeObjectSettings', 'height_based_enabled'))
DEFAULT_HEIGHT_BASED_MULTIPLIER = float(Config.get('placeObjectSettings', 'height_based_multiplier'))
DEFAULT_HEIGHT_BASED_OFFSET = float(Config.get('placeObjectSettings', 'height_based_offset'))
DEFAULT_RANDOM_NOISE_WEIGHT = float(Config.get('placeObjectSettings', 'random_noise_weight'))

class PlaceObjectSettings(Settings):

    def __init__(self, passedSettings):
        Settings.__init__(self, passedSettings)
        keys = passedSettings.keys()
        self.params.update({
            "density" : passedSettings['density']  if 'density' in keys else DEFAULT_DENSITY,
            "clumping" : passedSettings['clumping'] if 'clumping' in keys else DEFAULT_CLUMPING,
            "randomNoiseWeight" : passedSettings['randomNoiseWeight'] if 'randomNoiseWeight' in keys else DEFAULT_RANDOM_NOISE_WEIGHT,

            "randomNudgeEnabled" : passedSettings['randomNudge'] if 'randomNudge' in keys else DEFAULT_RANDOM_NUDGE_ENABLED,
            "randomRotationEnabled" : passedSettings['randomRotation'] if 'randomRotation' in keys else DEFAULT_RANDOM_ROTATION_ENABLED,

            "heightBasedEnabled" : passedSettings['heightBased'] if 'heightBased' in keys else DEFAULT_HEIGHT_BASED_ENABLED,
            "heightBasedMultiplier" : passedSettings['heightBasedMultiplier'] if 'heightBasedMultiplier' in keys else DEFAULT_HEIGHT_BASED_MULTIPLIER,
            "heightBasedOffset" : passedSettings['heightBasedOffset'] if 'heightBasedOffset' in keys else DEFAULT_HEIGHT_BASED_OFFSET
        })

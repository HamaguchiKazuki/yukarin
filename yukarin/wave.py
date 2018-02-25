from pathlib import Path

import librosa
import numpy


class Wave(object):
    def __init__(
            self,
            wave: numpy.ndarray,
            sampling_rate: int,
    ) -> None:
        self.wave = wave
        self.sampling_rate = sampling_rate

    @staticmethod
    def load(path: Path, sampling_rate: int, dtype=numpy.float32):
        wave = librosa.core.load(str(path), sr=sampling_rate, dtype=dtype)[0]
        return Wave(wave=wave, sampling_rate=sampling_rate)

    def pad(self, pre_second: int, post_second: int):
        pre, post = int(self.sampling_rate * pre_second), int(self.sampling_rate * post_second)
        return Wave(
            wave=numpy.pad(self.wave, pad_width=(pre, post), mode='constant'),
            sampling_rate=self.sampling_rate,
        )

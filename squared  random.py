!easy_install mne --upgrade
import mne

import numpy as np
mne.set_log_level('WARNING')
from mne.datasets import sample
data_path = sample.data_path()

raw_fname = data_path + '/MEG/sample/sample_audvis_filt-0-40_raw.fif'
raw = mne.io.Raw(raw_fname, preload=False)
print(raw)
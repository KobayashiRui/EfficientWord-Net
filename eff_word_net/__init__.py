"""
.. include:: ../README.md
"""

import os
RATE=16000
samples_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)),"sample_refs")

import sys
if sys.platform.startswith('linux'):
    from eff_word_net.package_installation_scripts import check_install_tflite
    check_install_tflite()
else:
    from eff_word_net.package_installation_scripts import check_install_tf
    check_install_tf()

#!/usr/bin/env python
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
"""Custom options for PulseAudio."""
from __future__ import print_function
import os

import package


class Package(package.Package):  # pylint: disable=too-few-public-methods
  """PulseAudio package."""

  def __init__(self, apt_version):
    super(Package, self).__init__('pulseaudio', apt_version)

  def post_download(self, source_directory):  # pylint: disable=no-self-use
    """Remove blacklisted patches."""
    # Fix *droid* patches.
    bad_patch_path = os.path.join(
        source_directory, 'debian', 'patches',
        '0600-droid-sync-with-upstream-for-Android-5-support-and-b.patch')
    if not os.path.exists(bad_patch_path):
      return

    print('Applying custom patches.')
    package.apply_patch(source_directory, 'pulseaudio_fix_android.patch')

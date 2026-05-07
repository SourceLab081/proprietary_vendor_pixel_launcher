#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The PixelOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = []


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
}  # fmt: skip

module = ExtractUtilsModule(
    'common',
    'pixel/launcher',
    device_rel_path='vendor/pixel/launcher',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    skip_main_proprietary_file=True,
)

module.add_proprietary_file('proprietary-files.txt')

module.add_proprietary_file('proprietary-files_tablet.txt').add_copy_files_guard(
    'TARGET_IS_TABLET', 'true'
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

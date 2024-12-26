#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

ifeq ($(WITH_GMS),true)

# Inherit from the proprietary version
$(call inherit-product, vendor/pixel_launcher/common/common-vendor.mk)

# Overlay
PRODUCT_PACKAGES += \
	FrameworkPixellauncher \
	PixelLauncherOverlay

PRODUCT_COPY_FILES += \
    vendor/pixel_launcher/prebuilt/etc/pixel_launcher.xml:$(TARGET_COPY_OUT_PRODUCT)/etc/sysconfig/pixel_launcher.xml \
    vendor/pixel_launcher/prebuilt/etc/preinstalled-packages-product-pixel_launcher.xml:$(TARGET_COPY_OUT_PRODUCT)/etc/sysconfig/preinstalled-packages-product-pixel_launcher.xml \
	vendor/pixel_launcher/prebuilt/etc/privapp-permissions-pixel_launcher-se.xml:$(TARGET_COPY_OUT_SYSTEM_EXT)/etc/permissions/privapp-permissions-pixel_launcher-se.xml

endif

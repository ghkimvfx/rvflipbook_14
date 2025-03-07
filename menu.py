import nuke
import nukescripts
import os

try:
    import rv_flipbook
    nuke.tprint("RV Flipbook Loaded Successfully!")
except Exception as e:
    nuke.tprint(f"Error loading RV Flipbook: {e}")

import nuke
import nukescripts
import nukescripts.flipbooking as flipbooking
import os
import subprocess

class RVFlipbook(flipbooking.FlipbookApplication):
    def __init__(self):
        if nuke.env['WIN32']:
            self._rvPath = "C:/Program Files/Shotgun/RV-7.1.1/bin/RV.exe"
            #if your RV path not here please change correct path
        else:
            self._rvPath = "/Applications/RV64.app/Contents/MacOS/RV64"
            #if your RV path not here please change correct path

    def name(self):
        return "RV"

    def path(self):
        return self._rvPath

    def cacheDir(self):
        return os.environ.get("NUKE_TEMP_DIR", os.path.expanduser("~"))

    def run(self, filename, frameRanges, views, options):
        sequence_interval = f"{frameRanges.minFrame()}-{frameRanges.maxFrame()}"

        for frame in range(frameRanges.minFrame(), frameRanges.maxFrame()):
            if frame not in frameRanges.toFrameList():
                print("This example only supports complete frame ranges.")
                return

        filename = os.path.normpath(filename)

        args = []
        if nuke.env['WIN32']:
            args.append(f'"{self.path()}"')
            filename = f'"{filename}"'
        else:
            args.append(self.path())

        args.append(filename)
        args.append(sequence_interval)

        if nuke.env['WIN32']:
            subprocess.Popen(" ".join(args), shell=True)
        else:
            os.spawnv(os.P_NOWAITO, self.path(), args)

    def capabilities(self):
        return {
            'proxyScale': False,
            'crop': True,
            'canPreLaunch': False,
            'supportsArbitraryChannels': True,
            'maximumViews': 2,
            'fileTypes': [
                "j2k", "jpt", "jp2", "dpx", "cin", "cineon", "jpeg", "jpg", "rla", "rpf",
                "yuv", "exr", "openexr", "sxr", "tif", "tiff", "sm", "tex", "tx", "tdl",
                "shd", "targa", "tga", "tpic", "rgbe", "hdr", "iff", "png", "z", "zfile",
                "sgi", "bw", "rgb", "rgba", "*mraysubfile*", "movieproc", "stdinfb",
                "aiff", "aif", "aifc", "wav", "snd", "au", "mov", "avi", "mp4", "m4v", "dv"
            ]
        }

flipbooking.register(RVFlipbook())
nukescripts.setFlipbookDefaultOption("flipbook", "RV")

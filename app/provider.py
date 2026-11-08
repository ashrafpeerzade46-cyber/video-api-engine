class ProviderNotConfigured(Exception):
    pass


class VideoProvider:

    def generate_video(self, payload):
        raise ProviderNotConfigured(
            "No video-generation provider is connected yet. "
            "Configure a real provider before generating videos."
        )


video_provider = VideoProvider()￼Enter

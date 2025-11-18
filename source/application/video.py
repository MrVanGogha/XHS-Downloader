from source.expansion import Namespace
from .request import Html

__all__ = ["Video"]


class Video:
    VIDEO_LINK = (
        "video",
        "consumer",
        "originVideoKey",
    )

    @classmethod
    def get_video_link(cls, data: Namespace) -> list:
        return (
            [Html.format_url(f"https://sns-video-bd.xhscdn.com/{t}")]
            if (t := data.safe_extract(".".join(cls.VIDEO_LINK)))
            else []
        )
    
    VIDEO_DIRECT_LINK = (
        "video",
        "media",
        "stream",
        "h264[0]",
        "masterUrl",
    )
    @classmethod
    def get_video_direct_link(cls, data: Namespace) -> list:
        return (
            [Html.format_url(f"{t}")]
            if (t := data.safe_extract(".".join(cls.VIDEO_DIRECT_LINK)))
            else []
        )



    VIDEO_DURATION = (
        "video",
        "media",
        "video",
        "duration",
    )
    @classmethod
    def get_video_duration(cls, data: Namespace) -> int:
        if (t := data.safe_extract(".".join(cls.VIDEO_DURATION))):
            return int(t)
        return 0


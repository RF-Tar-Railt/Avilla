from typing import Literal, Optional

from avilla.core.builtins.elements import Image
from avilla.core.message.chain import MessageChain
from avilla.core.message.element import Element

__all__ = (
    "FlashImage",
    "Face",
    "Rps",
    "Dice",
    "Shake",
    "Poke",
    "Anonymous",
    "Share",
    "FriendRecommend",
    "GroupRecommend",
    "Location",
    "MusicShare",
    "CustomMusicShare",
    "Reply",
    "MergedForward",
    "MergedForwardNode",
    "MergedForwardCustomNode",
    "XmlMessage",
    "JsonMessage",
)


class FlashImage(Image):
    def asDisplay(self) -> str:
        return "[$onebot::FlashImage]"


class Face(Element):
    id: int

    def __init__(self, id: int) -> None:
        self.id = id

    def asDisplay(self) -> str:
        return f"[$onebot::Face:id={self.id}]"


class Rps(Element):
    def asDisplay(self) -> str:
        return "[$onebot::Rps]"


class Dice(Element):
    def asDisplay(self) -> str:
        return "[$onebot::Dice]"


class Shake(Element):
    def asDisplay(self) -> str:
        return "[$onebot::Shake]"


class Poke(Element):
    type: str
    id: str
    name: Optional[str] = None

    def __init__(self, type: str, id: str, name: Optional[str] = None) -> None:
        self.type = type
        self.id = id
        self.name = name

    def asDisplay(self) -> str:
        return f"[$onebot::Poke:type={self.type},id={self.id},name={self.name or 'null'}]"


class Anonymous(Element):
    ignore: bool = True

    def __init__(self, ignore: bool = True) -> None:
        self.ignore = ignore

    def asDisplay(self) -> str:
        return "[$onebot::#Anonymous#]"


class Share(Element):
    url: str
    title: str
    content: Optional[str] = None
    image: Optional[str] = None

    def __init__(
        self, url: str, title: str, content: Optional[str] = None, image: Optional[str] = None
    ) -> None:
        self.url = url
        self.title = title
        self.content = content
        self.image = image

    def asDisplay(self) -> str:
        return f"[$onebot::Share:\
            url={self.url},\
            title={self.title},\
            content={self.content or 'null'},\
            image={self.image or 'null'}]"


class FriendRecommend(Element):
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def asDisplay(self) -> str:
        return f"[$onebot::FriendRecommend:id={self.id}]"


class GroupRecommend(Element):
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def asDisplay(self) -> str:
        return f"[$onebot::GroupRecommend:id={self.id}]"


class Location(Element):
    lat: float
    lon: float
    title: Optional[str] = None
    content: Optional[str] = None

    def __init__(
        self, lat: float, lon: float, title: Optional[str] = None, content: Optional[str] = None
    ) -> None:
        self.lat = lat
        self.lon = lon
        self.title = title
        self.content = content

    def asDisplay(self) -> str:
        return f"[$onebot::Location:\
            lat={self.lat},\
            lon={self.lon},\
            title={self.title or 'null'},\
            content={self.content or 'null'}]"


class MusicShare(Element):
    type: Literal["qq", "163", "xm"]
    id: str

    def __init__(self, type: Literal["qq", "163", "xm"], id: str) -> None:
        self.type = type
        self.id = id

    def asDisplay(self) -> str:
        return f"[$onebot::MusicShare:type={self.type},id={self.id}]"


class CustomMusicShare(Element):
    url: str
    audio: str
    title: str
    content: Optional[str] = None
    image: Optional[str] = None

    def __init__(
        self,
        url: str,
        audio: str,
        title: str,
        content: Optional[str] = None,
        image: Optional[str] = None,
    ) -> None:
        self.url = url
        self.audio = audio
        self.title = title
        self.content = content
        self.image = image

    def asDisplay(self) -> str:
        return f"[$onebot::CustomMusicShare:\
            url={self.url},\
            audio={self.audio},\
            title={self.title},\
            content={self.content or 'null'},\
            image={self.image or 'null'}]"


class Reply(Element):
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def asDisplay(self) -> str:
        return f"[$onebot::Reply:id={self.id}]"


class MergedForward(Element):
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def asDisplay(self) -> str:
        return f"[$onebot::MergedForward:id={self.id}]"


class MergedForwardNode(Element):
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def asDisplay(self) -> str:
        return f"[$onebot::MergedForwardNode:id={self.id}]"


class MergedForwardCustomNode(Element):
    user_id: str
    nickname: str
    content: MessageChain

    def __init__(self, user_id: str, nickname: str, content: MessageChain) -> None:
        self.user_id = user_id
        self.nickname = nickname
        self.content = content

    def asDisplay(self) -> str:
        return f"[$onebot::MergedForwardCustomNode:\
            user_id={self.user_id},\
            nickname={self.nickname},\
            content={self.content}]"


class XmlMessage(Element):
    xml: str

    def __init__(self, xml: str) -> None:
        self.xml = xml

    def asDisplay(self) -> str:
        return f"[$onebot::XmlMessage:xml={self.xml}]"


class JsonMessage(Element):
    json: str

    def __init__(self, _json: str) -> None:
        self.json = _json

    def asDisplay(self) -> str:
        return f"[$onebot::JsonMessage:json={self.json}]"
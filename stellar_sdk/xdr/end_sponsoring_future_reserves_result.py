# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from xdrlib import Packer, Unpacker

from .end_sponsoring_future_reserves_result_code import (
    EndSponsoringFutureReservesResultCode,
)

__all__ = ["EndSponsoringFutureReservesResult"]


class EndSponsoringFutureReservesResult:
    """
    XDR Source Code
    ----------------------------------------------------------------
    union EndSponsoringFutureReservesResult switch (
        EndSponsoringFutureReservesResultCode code)
    {
    case END_SPONSORING_FUTURE_RESERVES_SUCCESS:
        void;
    default:
        void;
    };
    ----------------------------------------------------------------
    """

    def __init__(
        self,
        code: EndSponsoringFutureReservesResultCode,
    ) -> None:
        self.code = code

    def pack(self, packer: Packer) -> None:
        self.code.pack(packer)
        if (
            self.code
            == EndSponsoringFutureReservesResultCode.END_SPONSORING_FUTURE_RESERVES_SUCCESS
        ):
            return

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "EndSponsoringFutureReservesResult":
        code = EndSponsoringFutureReservesResultCode.unpack(unpacker)
        if (
            code
            == EndSponsoringFutureReservesResultCode.END_SPONSORING_FUTURE_RESERVES_SUCCESS
        ):
            return cls(code)
        return cls(code)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "EndSponsoringFutureReservesResult":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "EndSponsoringFutureReservesResult":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.code == other.code

    def __str__(self):
        out = []
        out.append(f"code={self.code}")
        return f"<EndSponsoringFutureReservesResult {[', '.join(out)]}>"

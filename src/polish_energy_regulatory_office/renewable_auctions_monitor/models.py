"""Models for renewable auctions monitor."""

from dataclasses import dataclass


@dataclass
class AuctionResult:
    auction_id: str


@dataclass
class BidData:
    bid_id: str


@dataclass
class AuctionAnalysis:
    analysis_id: str

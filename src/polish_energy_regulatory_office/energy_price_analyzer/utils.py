"""Utility functions for energy price analyzer."""

from decimal import Decimal
from typing import List, Union

import pandas as pd


def calculate_average_price(prices: List[float]) -> float:
    """Calculate average price from list of prices."""
    if not prices:
        return 0.0
    return sum(prices) / len(prices)


def format_currency(amount: Union[float, Decimal], currency: str = "PLN") -> str:
    """Format amount as currency string."""
    return f"{float(amount):.2f} {currency}"


def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """Convert between energy units."""
    conversions = {
        ("kWh", "MWh"): 0.001,
        ("MWh", "kWh"): 1000.0,
        ("kWh", "GWh"): 0.000001,
        ("GWh", "kWh"): 1000000.0,
    }

    key = (from_unit, to_unit)
    if key in conversions:
        return value * conversions[key]
    return value


def filter_by_date_range(data: pd.DataFrame, start_date: str, end_date: str, date_column: str = "date") -> pd.DataFrame:
    """Filter dataframe by date range."""
    mask = (pd.to_datetime(data[date_column]) >= pd.to_datetime(start_date)) & (
        pd.to_datetime(data[date_column]) <= pd.to_datetime(end_date)
    )
    data_filtered: pd.DataFrame = data[mask]
    return data_filtered


def group_by_period(data: pd.DataFrame, period: str, date_column: str = "date") -> pd.DataFrame:
    """Group data by time period."""
    data_copy = data.copy()
    data_copy[date_column] = pd.to_datetime(data_copy[date_column])

    if period == "month":
        return data_copy.groupby(data_copy[date_column].dt.to_period("M")).sum()
    elif period == "quarter":
        return data_copy.groupby(data_copy[date_column].dt.to_period("Q")).sum()
    elif period == "year":
        return data_copy.groupby(data_copy[date_column].dt.to_period("Y")).sum()
    else:
        return data_copy

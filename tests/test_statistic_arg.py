"""Tests for --statistic argument validation (PomodoroTimer.arg)."""

import sys

import pytest

from pomodorotimer.pomodorotimer import PomodoroTimer


def test_statistic_accepts_valid_values(monkeypatch):
    monkeypatch.setattr(
        sys, "argv", ["pomodorotimer", "--statistic", "today"]
    )
    assert PomodoroTimer.arg() == "today"


@pytest.mark.parametrize("bad", ["bogus", "TODAY", "all ", "123"])
def test_statistic_rejects_invalid_values(monkeypatch, bad):
    """A typo'd --statistic value must error, not drop into the timer."""
    monkeypatch.setattr(sys, "argv", ["pomodorotimer", "--statistic", bad])
    with pytest.raises(SystemExit):
        PomodoroTimer.arg()

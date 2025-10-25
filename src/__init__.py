"""
Memory Engineering - A framework for AI agent memory systems.

Teaching AI agents to learn like professional chefs, not recipe followers.
"""

__version__ = "0.1.0"
__author__ = "CognioLab"

from .memory import MemorySystem
from .consolidation import ConsolidationEngine

__all__ = ["MemorySystem", "ConsolidationEngine"]

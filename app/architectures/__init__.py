"""Coordination Topologies for MultiAgentBench"""
from .base_architecture import BaseArchitecture, ArchitectureResult
from .single_agent import SingleAgentArchitecture
from .star import StarArchitecture
from .chain import ChainArchitecture
from .tree import TreeArchitecture
from .graph import GraphArchitecture

__all__ = [
    "BaseArchitecture",
    "ArchitectureResult",
    "SingleAgentArchitecture",
    "StarArchitecture",
    "ChainArchitecture",
    "TreeArchitecture",
    "GraphArchitecture"
]

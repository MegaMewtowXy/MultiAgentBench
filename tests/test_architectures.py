"""
Integration tests for 5 Coordination Topologies (Single, Star, Chain, Tree, Graph).
Runs 100% offline using MockProvider.
"""

import pytest
from app.llm import MockProvider
from app.architectures import (
    SingleAgentArchitecture,
    StarArchitecture,
    ChainArchitecture,
    TreeArchitecture,
    GraphArchitecture,
    ArchitectureResult
)

SAMPLE_TASK = {
    "task_id": "test_task_001",
    "category": "Planning",
    "prompt": "Design a scalable university management system architecture.",
    "constraints": ["Must use modular microservices", "Max budget $10,000"],
    "expected_properties": ["microservices", "modular"]
}

def test_single_agent_architecture():
    provider = MockProvider()
    arch = SingleAgentArchitecture(provider=provider)
    res = arch.solve_task(SAMPLE_TASK)

    assert isinstance(res, ArchitectureResult)
    assert res.architecture_name == "single"
    assert res.task_id == "test_task_001"
    assert res.success is True
    assert res.total_calls == 1
    assert "DEMO / MOCK DATA" in res.final_answer

def test_star_architecture():
    provider = MockProvider()
    arch = StarArchitecture(provider=provider)
    res = arch.solve_task(SAMPLE_TASK)

    assert res.architecture_name == "star"
    assert res.success is True
    assert res.total_calls == 5
    assert len(res.communication_edges) == 6
    assert len(res.agent_states) == 5

def test_chain_architecture():
    provider = MockProvider()
    arch = ChainArchitecture(provider=provider)
    res = arch.solve_task(SAMPLE_TASK)

    assert res.architecture_name == "chain"
    assert res.success is True
    assert res.total_calls == 5
    assert len(res.communication_edges) == 4

def test_tree_architecture():
    provider = MockProvider()
    arch = TreeArchitecture(provider=provider)
    res = arch.solve_task(SAMPLE_TASK)

    assert res.architecture_name == "tree"
    assert res.success is True
    assert res.total_calls == 6
    assert len(res.agent_states) == 6

def test_graph_architecture():
    provider = MockProvider()
    arch = GraphArchitecture(provider=provider)
    res = arch.solve_task(SAMPLE_TASK)

    assert res.architecture_name == "graph"
    assert res.success is True
    assert res.total_calls >= 4
    assert ("planner", "researcher") in res.communication_edges
    assert ("critic", "finalizer") in res.communication_edges

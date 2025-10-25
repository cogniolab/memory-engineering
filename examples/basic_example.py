"""
Basic example of Memory Engineering in action.

This example demonstrates how an AI agent learns user preferences
across multiple sessions through memory consolidation.
"""

import sys
sys.path.append('../src')

from memory import MemorySystem
from consolidation import ConsolidationEngine


def main():
    """Run basic memory engineering example."""

    print("=" * 60)
    print("MEMORY ENGINEERING - BASIC EXAMPLE")
    print("=" * 60)

    # Initialize components
    memory = MemorySystem(user_id="user_123")
    consolidation = ConsolidationEngine()

    # Session 1: User gives feedback
    print("\n📅 SESSION 1")
    print("-" * 60)

    session_1 = {
        'user': "I prefer brief, technical answers",
        'agent_response': "[Long detailed explanation...]",
        'feedback': "Too long! Keep it concise.",
        'outcome': 'negative'
    }

    print(f"User: {session_1['user']}")
    print(f"Agent: {session_1['agent_response']}")
    print(f"User: {session_1['feedback']}")

    # Consolidate
    print("\n⚙️  Consolidating experience...")
    insights = consolidation.consolidate(session_1)

    print(f"💡 Extracted: {insights['patterns'][0]['principle']}")
    print(f"   Confidence: {insights['patterns'][0]['confidence']}")

    # Store in memory
    memory.store_session(session_1)
    memory.update_long_term('patterns', insights['patterns'][0])

    # Session 2: Memory retrieval
    print("\n\n📅 SESSION 2")
    print("-" * 60)

    context = memory.retrieve(query="How should I respond?")

    print(f"🧠 Retrieved from memory:")
    print(f"   Pattern: {context['patterns'][0]['principle']}")

    print("\nUser: What is Docker?")
    print("Agent: Containerization platform for packaging apps.")
    print("       Want more detail?")
    print("User: Perfect!")

    print("\n" + "=" * 60)
    print("✅ Agent learned and applied user preference!")
    print("=" * 60)


if __name__ == "__main__":
    main()

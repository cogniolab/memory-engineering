```python
import anthropic
from datetime import datetime


def memory_engineering_system():
    """
    Memory Engineering framework for AI agents.
    Demonstrates how AI learns from experience like professional chefs,
    building intuition through pattern recognition and adaptation.
    """
    client = anthropic.Anthropic()
    
    # Initialize memory structure for learning progression
    memory_state = {
        "experiences": [],
        "patterns": [],
        "intuitions": [],
        "adaptations": [],
    }
    
    # System prompt that enables memory-based learning
    system_prompt = """You are a Memory Engineering system for AI agents. Your role is to:
1. Learn from experiences and build intuition like professional chefs
2. Recognize patterns across different contexts
3. Develop and refine heuristics through practice
4. Share insights about what works and why

When given experiences, extract:
- Core patterns (what consistently works)
- Context factors (when and where it applies)
- Exceptions (when patterns break)
- Intuitive rules (professional shortcuts)

Format responses as learning insights, not just answers."""

    def add_experience(domain: str, scenario: str, outcome: str, context: dict = None):
        """Record an experience for the system to learn from."""
        experience = {
            "domain": domain,
            "scenario": scenario,
            "outcome": outcome,
            "context": context or {},
            "timestamp": datetime.now().isoformat()
        }
        memory_state["experiences"].append(experience)
        return experience

    def extract_patterns():
        """Have Claude analyze experiences to extract patterns."""
        if not memory_state["experiences"]:
            return "No experiences recorded yet."
        
        experiences_text = "\n".join([
            f"- Domain: {e['domain']}, Scenario: {e['scenario']}, Outcome: {e['outcome']}"
            for e in memory_state["experiences"][-5:]  # Last 5 experiences
        ])
        
        pattern_prompt = f"""Analyze these recent experiences and extract:
1. Core patterns (what consistently works)
2. Context factors that influence success
3. Intuitive rules professional would use
4. Exceptions to watch for

Recent experiences:
{experiences_text}

Provide insights like a master chef teaching an apprentice."""
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=system_prompt,
            messages=[{"role": "user", "content": pattern_prompt}]
        )
        
        patterns = response.content[0].text
        memory_state["patterns"].append(patterns)
        return patterns

    def apply_intuition(new_scenario: str, domain: str):
        """Use learned patterns to handle new scenarios."""
        patterns_context = "\n".join(memory_state["patterns"][-3:]) if memory_state["patterns"] else "No patterns learned yet"
        
        intuition_prompt = f"""Based on patterns learned from past experiences:

{patterns_context}

Now handle this new scenario in {domain}:
{new_scenario}

Apply your learned intuition. What would a master do? Explain your reasoning."""
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=system_prompt,
            messages=[{"role": "user", "content": intuition_prompt}]
        )
        
        intuition = response.content[0].text
        memory_state["intuitions"].append({
            "scenario": new_scenario,
            "domain": domain,
            "intuition": intuition
        })
        return intuition

    def demonstrate_learning():
        """Demonstrate the memory engineering framework in action."""
        print("=== Memory Engineering: AI Learning Like Master Chefs ===\n")
        
        # Phase 1: Add experiences
        print("Phase 1: Recording Experiences")
        print("-" * 50)
        
        experiences = [
            ("cooking", "Searing steak at high heat", "Perfect crust, juicy inside",
             {"temperature": 500, "duration": 3, "oil_type": "avocado"}),
            ("cooking", "Searing steak at medium heat", "Pale crust, dry inside",
             {"temperature": 350, "duration": 5, "oil_type": "olive"}),
            ("cooking", "Slow roasting chicken at 325F", "Tender, moist",
             {"temperature": 325, "duration": 45, "marinade": True}),
            ("cooking", "Quick roasting chicken at 450F", "Dry outside, undercooked inside",
             {"temperature": 450, "duration": 25, "marinade": False}),
        ]
        
        for domain, scenario, outcome, context in experiences:
            exp = add_experience(domain, scenario, outcome, context)
            print(f"✓ Recorded: {scenario}")
        
        print(f"\nTotal experiences recorded: {len(memory_state['experiences'])}\n")
        
        # Phase 2: Extract patterns
        print("Phase 2: Extracting Patterns from Experience")
        print("-" * 50)
        patterns = extract_patterns()
        print("Patterns discovered:")
        print(patterns)
        print()
        
        # Phase 3: Apply learned intuition
        print("Phase 3: Applying Learned Intuition to New Scenario")
        print("-" * 50)
        new_scenario = """You need to cook a salmon fillet. 
        It's a delicate protein that can easily overcook. 
        You want a crispy skin but moist flesh inside."""
        
        intuition = apply_intuition(new_scenario, "cooking")
        print("Intuitive solution based on learned patterns:")
        print(intuition)
        print()
        
        # Phase 4: Summary
        print("Phase 4: Learning Summary")
        print("-" * 50)
        print(f"Total patterns learned: {len(memory_state['patterns'])}")
        print(f"Total intuitions applied: {len(memory_state['intuitions'])}")
        print("\nThe system has evolved from following recipes to understanding")
        print("the principles behind cooking - learning like a real chef!")

    # Run the demonstration
    demonstrate_learning()


if __name__ == "__main__":
    memory_engineering_system()
```
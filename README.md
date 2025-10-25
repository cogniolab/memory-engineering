# Memory Engineering™

> Teaching AI agents to learn like professional chefs, not recipe followers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## The Problem

Current AI agents suffer from amnesia. Tell ChatGPT your preferences in one session, start a new chat, and it's forgotten. This isn't a limitation of language models—it's an unsolved engineering problem.

As Andrej Karpathy (former Tesla AI director, OpenAI founding member) identified in his recent interview with Dwarkesh Patel:

> "We don't have an equivalent of continual learning. You can't just tell them something and they'll remember it. They're cognitively lacking and it's just not working."

**Memory Engineering** is the systematic approach to solving this problem.

---

## What is Memory Engineering?

Memory Engineering is a framework for designing AI agent memory systems that:

1. **Selectively consolidate** experiences into generalizable knowledge (not just store everything)
2. **Track confidence** with evidence-based learning
3. **Learn continuously** without catastrophic forgetting
4. **Maintain diversity** to avoid collapse into narrow patterns
5. **Generalize knowledge** to apply learning across contexts

### The Core Insight

Memory isn't just storage—it's the ability to selectively consolidate experiences into generalizable knowledge while maintaining appropriate flexibility.

**Think of it like cooking:**
- **Bad approach:** Memorize 1,000 recipes perfectly, but can't make anything new
- **Good approach:** Learn fundamental cooking principles from 10 dishes, then create infinite variations

**Current AI = Recipe follower**
**Memory Engineering = Professional chef**

---

## Why This Matters

### For Users
- AI assistants that remember your preferences across sessions
- Personalized experiences that improve over time
- No more repeating yourself to the same AI

### For Developers
- Framework for building agents with continual learning
- Practical patterns for memory consolidation
- Open-source alternative to proprietary memory systems

### For Businesses
- Customer service bots that build context over time
- AI that learns your team's processes and preferences
- Compounding value—gets better with use, not just more data

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                 MEMORY ENGINEERING SYSTEM            │
└─────────────────────────────────────────────────────┘

    👤 USER INTERACTION
         │
         ▼
┌─────────────────────────┐
│  WORKING MEMORY         │ ◄──────────┐
│  (Short-Term)           │            │
├─────────────────────────┤            │
│ • Context Window        │         Retrieval
│ • Active Reasoning      │            │
└───────────┬─────────────┘            │
            │                          │
    End of Session                     │
            │                          │
            ▼                          │
┌─────────────────────────┐            │
│  CONSOLIDATION ENGINE   │            │
├─────────────────────────┤            │
│ 1. Reflection           │            │
│ 2. Pattern Extraction   │            │
│ 3. Integration          │            │
│ 4. Pruning              │            │
└────┬──────────────┬─────┘            │
     │              │                  │
     ▼              ▼                  │
┌─────────────┐  ┌──────────────────┐ │
│  EPISODIC   │  │  LONG-TERM       │─┘
│  MEMORY     │  │  MEMORY          │
├─────────────┤  ├──────────────────┤
│ • Episodes  │  │ • Semantic       │
│ • Events    │  │ • Procedural     │
│ • Context   │  │ • User Profile   │
└─────────────┘  └──────────────────┘
```

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/cogniolab/memory-engineering.git
cd memory-engineering

# Install dependencies
pip install -r requirements.txt
```

### Basic Example

```python
from memory_engineering import MemorySystem, ConsolidationEngine

# Initialize memory system
memory = MemorySystem(user_id="user_123")

# Simulate user interaction
session = {
    'user': "I prefer brief, technical answers",
    'agent_response': "[long detailed answer]",
    'feedback': "Too long! Keep it concise.",
    'outcome': 'negative'
}

# Consolidate experience
consolidation = ConsolidationEngine()
insights = consolidation.consolidate(session)

# Next session - memory retrieves learned preference
context = memory.retrieve(query="How should I respond?")
# Returns: "User prefers concise, technical answers (confidence: 0.8)"
```

See [examples/](examples/) for more detailed tutorials.

---

## Features

### ✅ Current Features

- **Multi-layer memory system** (working, episodic, long-term)
- **Consolidation engine** with reflection and pattern extraction
- **Confidence tracking** with Bayesian updates
- **Context-aware retrieval** with semantic search
- **Entropy maintenance** to prevent pattern collapse

### 🚧 Roadmap

- [ ] LoRA-based weight updates for personalization
- [ ] Multi-agent shared memory ("culture")
- [ ] Advanced compression strategies
- [ ] Production-ready vector DB integrations
- [ ] Benchmarks and evaluation suite

---

## Documentation

- **[LinkedIn Article](docs/linkedin-article.md)** - Accessible explanation for non-technical audiences
- **[Problem Statement](docs/problem-statement.md)** - Deep dive into the memory problem Andrej identified
- **[Architecture](docs/architecture.md)** - Technical design and implementation details
- **[Principles](docs/principles.md)** - Core Memory Engineering principles
- **[Examples](docs/examples.md)** - Detailed walkthroughs and tutorials

---

## Philosophy

Memory Engineering takes a **pragmatist approach** to AI development:

- This is the **decade of agents**, not the year (as Andrej Karpathy noted)
- We solve hard engineering problems, not wait for breakthroughs
- Open collaboration > closed proprietary systems
- Evidence-based design > hype-driven development

We're building the missing pieces that Andrej identified, one component at a time.

---

## Contributing

We welcome contributions! Memory Engineering is an open research area with many unsolved problems:

- Novel consolidation algorithms
- Better confidence tracking mechanisms
- Entropy maintenance strategies
- Real-world applications and benchmarks
- Documentation improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## References

This work builds on insights from:

- **Andrej Karpathy × Dwarkesh Patel Interview** - [dwarkesh.com/p/andrej-karpathy](https://www.dwarkesh.com/p/andrej-karpathy)
- Research on continual learning, episodic memory systems, and consolidation processes

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## Citation

If you use Memory Engineering in your research or projects, please cite:

```bibtex
@software{memory_engineering_2025,
  title={Memory Engineering: A Framework for AI Agent Memory Systems},
  author={CognioLab},
  year={2025},
  url={https://github.com/cogniolab/memory-engineering}
}
```

---

## Connect

**Questions? Ideas? Feedback?**

Reach out directly on LinkedIn: [Moses Rajan](https://www.linkedin.com/in/mosesrajanpro/)

Or open an issue/discussion on GitHub.

---

## About CognioLab

CognioLab builds open-source AI agent frameworks and tools for the community. Check out our other projects:

- [microgpt-agent-sdk](https://github.com/cogniolab/microgpt-agent-sdk) - Production-ready AI agent SDK
- [agent-security](https://github.com/cogniolab/agent-security) - Security framework for AI agents
- [agent-monitor](https://github.com/cogniolab/agent-monitor) - Observability platform for agents

---

**Memory Engineering™** - Teaching AI to be chefs, not recipe followers.

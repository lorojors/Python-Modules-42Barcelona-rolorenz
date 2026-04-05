# 🐍 Python Modules - 42 Barcelona Cursus

Welcome, brave Python adventurer! This is a comprehensive collection of **Python learning modules** created by **Rolorenz** as part of the **42 Barcelona curriculum**. Whether you're just starting your Python journey or looking to master advanced concepts, you've come to the right place!

## 📚 What's Inside?

This repository contains **9 complete modules (00-08)**, each with progressive exercises that build your Python skills from the ground up!

### Module Overview

| Module | Topics | Focus |
|--------|--------|-------|
| **Module 00** | Basics & Functions | Hello world, area calculation, plant management |
| **Module 01** | Data Types & Functions | Garden data, growth tracking, factories, security |
| **Module 02** | Exception Handling | Try-except, custom errors, error hierarchy, cleanup, garden management |
| **Module 03** | Collections & Streams | Command-line args, scores, coordinates, achievements, inventory, generators |
| **Module 04** | File I/O & Streams | File creation, reading, context managers, stream handling, crisis response |
| **Module 05** | OOP & Polymorphism | ABC, abstract methods, type hints, data processors, pipeline architecture |
| **Module 06** | Packages & Modules | Package structure, alchemy theme, imports, subpackages, transmutation recipes |
| **Module 07** | Design Patterns | Creatures, capabilities, factories, battle strategies, tournaments |
| **Module 08** | Advanced Concepts | Constructs, lazy loading, oracle/meta programming |

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+** installed on your system
- Basic command-line knowledge
- Ready to learn! 🎓

### Installation

1. **Clone this repository:**
   ```bash
   git clone <repository-url>
   cd Python-Modules-42Barcelona
   ```

2. **Navigate to a module:**
   ```bash
   cd "Python Module 04"
   ```

3. **Run an exercise:**
   ```bash
   python3 ex1/ft_archive_creation.py
   ```

## 📖 Learning Path

Start with **Module 00** for basics, then progress through **Module 01** and **Module 02** to master exception handling. By **Module 03**, you'll work with collections and command-line arguments. **Module 04** takes it further with file I/O and stream management. **Module 05** rounds out OOP with abstract classes and pipelines. **Module 06** dives into Python's package and module system. **Module 07** introduces design patterns through a creature battle theme. **Module 08** tackles advanced Python concepts like lazy loading and metaprogramming.

Each exercise builds on previous concepts, creating a solid Python foundation.

## 🎓 Concepts Covered

### Module 00-01
✅ Functions and basic operations
✅ Data types and structures
✅ Input/output handling

### Module 02
✅ Exception handling (try-except-finally)
✅ Custom exception classes
✅ Error hierarchy and inheritance
✅ Graceful error recovery
✅ Practical garden management with error control

### Module 03
✅ Command-line arguments (sys.argv)
✅ Lists, tuples, sets, and dictionaries
✅ 3D coordinates and geometry
✅ Set operations (union, intersection, difference)
✅ Dictionary methods (keys, values, items, get, update)
✅ Generators and memory efficiency
✅ Data streaming and analytics

### Module 04
✅ Writing files with `open()` in write mode (`'w'`)
✅ Reading files with `open()` in read mode (`'r'`)
✅ Context managers (`with` statement) for safe file handling
✅ Exception chaining — catching and re-raising with custom messages
✅ `sys.stdout` vs `sys.stderr` — controlling output streams directly
✅ `FileNotFoundError` and `PermissionError` handling
✅ Data generation utilities

### Module 05
✅ Abstract Base Classes (`ABC`) and `@abstractmethod` decorators
✅ Polymorphism and method overriding
✅ Type annotations with the `typing` module (`Any`, `List`, `Dict`, `Union`, `Optional`, `Protocol`)
✅ `Protocol` for structural (duck-typing) interfaces
✅ Specialised data processors (`NumericProcessor`, `TextProcessor`, `LogProcessor`)
✅ Multi-stream handlers (`SensorStream`, `TransactionStream`, `EventStream`)
✅ Enterprise pipeline architecture with chaining, error recovery and performance monitoring
✅ `collections` module — `OrderedDict`, `deque`, `defaultdict`

### Module 06
✅ Python package structure (`__init__.py`, subpackages)
✅ Relative and absolute imports
✅ Organising code across multiple modules
✅ Nested subpackage hierarchies (`alchemy/grimoire/`, `alchemy/transmutation/`)
✅ Alembic operations — distillation, transmutation, kaboom sequences
✅ Spellbooks, validators and potion recipes as real-world module design patterns

### Module 07
✅ Factory pattern (`factory.py`)
✅ Capability / mixin pattern
✅ Strategy pattern for combat logic
✅ Class hierarchies for creatures and abilities
✅ Multi-file package organisation with `__init__.py`
✅ Battle and tournament orchestration scripts

### Module 08
✅ Dynamic object construction (`construct.py`)
✅ Lazy loading and deferred initialisation (`loading.py`)
✅ Oracle / introspection and meta-level programming (`oracle.py`)

## 💡 Pro Tips

- 📖 **Read the docstrings** - Every function has helpful documentation
- 🧪 **Test with different inputs** - Learn how programs handle edge cases
- 🔍 **Study error messages** - They're your best teachers!
- 🔄 **Modify the code** - Experimentation is the best way to learn
- 📝 **Keep notes** - Document what you learn for future reference

## 📂 Project Structure

```
Python-Modules-42Barcelona/
├── Python Module 00/
│   ├── ex0/           → ft_hello_garden.py
│   ├── ex1/           → ft_plot_area.py
│   ├── ex2/           → ft_harvest_total.py
│   ├── ex3/           → ft_plant_age.py
│   ├── ex4/           → ft_water_reminder.py
│   ├── ex5/           → ft_count_harvest_iterative.py / ft_count_harvest_recursive.py
│   ├── ex6/           → ft_garden_summary.py
│   └── ex7/           → ft_seed_inventory.py
├── Python Module 01/
│   ├── ex0/           → ft_garden_intro.py
│   ├── ex1/           → ft_garden_data.py
│   ├── ex2/           → ft_plant_growth.py
│   ├── ex3/           → ft_plant_factory.py
│   ├── ex4/           → ft_garden_security.py
│   ├── ex5/           → ft_plant_types.py
│   └── ex6/           → ft_garden_analytics.py
├── Python Module 02/
│   ├── ex0/           → ft_first_exception.py
│   ├── ex1/           → ft_different_errors.py
│   ├── ex2/           → ft_custom_errors.py
│   ├── ex3/           → ft_finally_block.py
│   ├── ex4/           → ft_raise_errors.py
│   └── ex5/           → ft_garden_management.py
├── Python Module 03/
│   ├── ex0/           → ft_command_quest.py
│   ├── ex1/           → ft_score_analytics.py
│   ├── ex2/           → ft_coordinate_system.py
│   ├── ex3/           → ft_achievement_tracker.py
│   ├── ex4/           → ft_inventory_system.py
│   └── ex5/           → ft_data_stream.py
├── Python Module 04/
│   ├── data_generator.py
│   ├── ex0/           → ft_ancient_text.py
│   ├── ex1/           → ft_archive_creation.py
│   ├── ex2/           → ft_stream_management.py
│   ├── ex3/           → ft_vault_security.py
│   └── ex4/           → ft_crisis_response.py
├── Python Module 05/
│   ├── ex0/           → data_processor.py
│   ├── ex1/           → data_stream.py
│   └── ex2/           → data_pipeline.py
├── Python Module 06/
│   ├── elements.py
│   ├── ft_alembic_0..5.py
│   ├── ft_distillation_0..1.py
│   ├── ft_kaboom_0..1.py
│   ├── ft_transmutation_0..2.py
│   ├── __init__.py
│   └── alchemy/
│       ├── elements.py
│       ├── potions.py
│       ├── __init__.py
│       ├── grimoire/
│       │   ├── dark_spellbook.py / dark_validator.py
│       │   ├── light_spellbook.py / light_validator.py
│       │   └── __init__.py
│       └── transmutation/
│           ├── recipes.py
│           └── __init__.py
├── Python Module 07/
│   ├── battle.py
│   ├── capacitor.py
│   ├── tournament.py
│   ├── ex0/           → creature.py, factory.py
│   ├── ex1/           → capability.py, creature.py, factory.py
│   └── ex2/           → strategy.py
└── Python Module 08/
    ├── ex0/           → construct.py
    ├── ex1/           → loading.py
    └── ex2/           → oracle.py
```

## 🛠️ Running Exercises

Each exercise is a standalone Python file. Simply navigate to the directory and run:

```bash
python3 ft_filename.py [optional arguments]
```

Most exercises have:
- ✅ Default values (run without arguments)
- ✅ Command-line argument support
- ✅ Error handling for invalid input
- ✅ Clear, formatted output

## 🎯 Using This as a Study Guide

1. **Read the exercise description** - Understand what you're building
2. **Look at the expected output** - Know what "done" looks like
3. **Study the code** - Learn HOW it works
4. **Experiment** - Modify and test your understanding
5. **Solve on your own** - Try writing similar code from scratch

## 🤝 Contributing

Found a bug? Have suggestions? Feel free to:
- Report issues
- Suggest improvements
- Share your own solutions
- Help fellow students

## 📞 Questions?

If you get stuck:
1. ✅ Read the error message carefully
2. ✅ Check the code comments
3. ✅ Research the Python documentation
4. ✅ Ask your peers or mentors

Remember: **Every error is a learning opportunity!** 🌟

## 📜 License

This project is part of the 42 Barcelona cursus education program.

---

**Created with ❤️ by Rolorenz**

---

## 🌟 Quick Stats

- 📦 **9 Python Modules**
- 📝 **45+ Exercises & Scripts**
- 🎓 **Beginner to Advanced Level**
- ⏱️ **Estimated Learning Time: 60-80+ hours**
- 🏆 **100% Educational Value**

Happy coding! 🎉

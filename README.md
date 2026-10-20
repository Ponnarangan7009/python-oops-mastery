# Python OOP Mastery

A beginner-friendly, hands-on repository for learning object-oriented programming in Python. It contains runnable lesson examples, guided exercises, and concise notes for each topic.

## Topics covered

1. Classes, objects, instance attributes, methods, and `self`
2. Instance methods, class attributes, class methods, and static methods
3. Encapsulation conventions, name mangling, and properties
4. Inheritance, overriding, `super()`, multiple inheritance, and method resolution order
5. Polymorphism through overriding and duck typing
6. Abstract base classes and abstract methods
7. Composition: objects working together through stored references
8. Special methods: `__str__`, `__repr__`, `__len__`, `__eq__`, and `__add__`
9. Dataclasses for data-focused classes
10. Custom exception classes

## Repository structure

- `learning/`: complete examples with comments explaining the concepts
- `exercises/`: practice prompts with starter code and callers

Each lesson file can be run independently with Python 3. The exercise files are intentionally incomplete; fill in the TODO sections as practice.

## Suggested order

Work through the numbered files in `learning/`, then try the matching file in `exercises/`. Read the prompt and caller before filling in the TODOs. Keep your own solutions and commit them as you progress.

## Running a file

From the repository folder, run a lesson or exercise with:

```bash
python3 learning/01_classes_and_methods.py
python3 exercises/01_classes_and_methods.py
```

No third-party packages are needed. Dataclasses are part of Python's standard library.

## Key ideas to remember

- A class describes a kind of object; an instance is one object created from that class.
- Instance methods receive the instance as `self`; Python supplies it when called through an instance.
- Inheritance models an “is-a” relationship. Composition models a “has-a” relationship.
- Encapsulation in Python uses conventions and properties; a leading underscore signals internal use, while double underscores trigger name mangling.
- Polymorphism means the same operation can work with different object types that provide the needed behavior.
- Special methods let objects participate in built-in operations such as `print()`, `len()`, equality, and addition.
- A dataclass is useful for structured data. It does not replace a list: a list can hold many dataclass instances.

## Learning approach

Type and run the learning examples, change values, and observe what happens. Then solve the exercises without copying the lesson implementation. Use Git to save each meaningful step.

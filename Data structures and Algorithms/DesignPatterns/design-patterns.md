# Overview on Design Patterns

> One thing expert designers know not to do is solve every problem from first principles. Rather, they reuse solutions that have worked for them in the past. When they find a good solution, they use it again and again. Such experience is part of what makes them experts. Consequently, you'll find recurring patterns of classes and communicating objects in many object-oriented systems. These patterns solve specific design problems and make object-oriented designs more flexible, elegant, and ultimately reusable. They help designers reuse successful designs by basing new designs on prior experience. A designer who is familiar with such patterns can apply them immediately to design problems without having to rediscover them. [1]

>[Design patterns are] *descriptions of communicating objects and classes that are customized to solve a general design problem in a particular contex*.[2]

## Importance of Design Patterns

- Because design patterns encapsulate solutions to recurring problems, conceptualizing and understanding patterns allows for an **abstraction for reasoning about designs**. 
- The patterns integrate and encapsulate **best practices** that have been proven to work. 
- Bridges the gap between high level design concepts with implementation allowing for easier **transition between design and development**. 
- Having a common **design vocabulary** allows common language for discussion among developers.
- Patterns enable **documentation** of explicit solutions to common problems.

## Elements of a design pattern

- **pattern name**: describes (1) the design pattern (in a one or two words); (2) the solution; and (3) its consequences.
- **problem**: describes when to apply the pattern. 
- **solution**: describes the elements that make up the design, relationships, responsibilities, and collaboration.
- **consequences**: describes the results and tradeoffs of applying the pattern.

## Design Pattern Categorization

||Creational|Structural|Behavioral|
|---|---|---|---|
|**class**|factory|adapter|interpretor<br/> template method|
|**object**|abstract<br/> builder<br/> prototype<br/> singleton|adapter<br/> bridge<br/> composite<br/> decorator<br/> facade<br/> flyweight<br/> proxy|chain of responsibility<br/> command<br/> iterator<br/> mediator<br/> memento<br/> observer<br/> state<br/> strategy<br/> visitor|

## Creational Patterns

**Creational design patterns** deal with the mechanisms of **object creation**, or abstracting the **instantiation process**. 

- A *class creational pattern* uses inheritance to vary the class it has instantiated. 
- An *object creational pattern* delegates instantiation to another object.

### Abstract Factory Pattern

Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows the system to be independent of how its objects are created, composed, and represented, promoting flexibility in object creation.

### Builder Pattern

The Builder Pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations. This pattern helps manage the construction of complex objects step by step and facilitates the creation of varied products.

### Factory Method Pattern

The factory method pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. It promotes loose coupling between the creator and the products, providing flexibility in instantiating different types of objects.

### Prototype Pattern

The Prototype Pattern creates new objects by copying an existing object known as the prototype. This approach is useful when the cost of creating an object is more expensive than copying an existing one. It enhances performance and promotes object reuse.

### Singleton Pattern

The Singleton Pattern ensures a class has only one instance and provides a global point of access to that instance. It is useful when exactly one object is needed to coordinate actions across the system, like a configuration manager or a logging service.

## Structural Patterns

### Adapter Pattern

An Adapter allows incompatible interfaces to work together by providing a wrapper that converts the interface of a class into another interface that a client expects. It helps integrate existing systems and classes that otherwise couldn't collaborate.

### Bridge Pattern

A Bridge separates abstraction from implementation, allowing both to evolve independently. It is useful when you want to avoid a permanent binding between an abstraction and its implementation, providing flexibility in changing either without affecting the other.

### Composite Pattern

A Composite composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly, simplifying the client code and enabling the creation of complex structures.

### Decorator Pattern

A Decorator attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality, allowing behavior to be added incrementally and facilitating the creation of complex combinations of behaviors.

### Facade Pattern

A Facade provides a unified interface to a set of interfaces in a subsystem, making it easier to use. It simplifies a complex system by providing a higher-level interface, which is more convenient for clients.

### Flyweight Pattern

A Flyweight minimizes memory usage or computational expenses by sharing as much as possible with related objects. It is particularly useful when dealing with a large number of similar objects, helping improve performance and reduce resource consumption.

### Proxy Pattern

A Proxy provides a surrogate or placeholder for another object to control access to it. It is useful in scenarios where you want to add an extra layer of control, such as lazy loading, access control, or logging, without modifying the actual object.

## Behavioral Patterns

### Chain of Responsibility

The Chain of Responsibility Pattern allows requests to be passed along a chain of handlers. It allows multiple objects to handle a request without the sender needing to know which object will ultimately process the request, promoting flexibility and decoupling.

### Command

The Command Pattern turns a request into a stand-alone object, containing all the information about the request. It allows for parameterization of objects, queuing of requests, and supporting undoable operations.

### Interpreter

The Interpreter Pattern defines a grammar for interpreting the sentences in a language and provides an interpreter to interpret the sentences. It is useful for creating language interpreters or compilers.

### Iterator

The Iterator Pattern provides a way to access elements of an aggregate object sequentially without exposing its underlying representation. It simplifies the traversal of collections and allows for uniform access to the elements.

### Mediator

The Mediator Pattern defines an object that centralizes communication between other objects, thus reducing direct connections between them. It promotes loose coupling by allowing objects to interact without having explicit references to each other.

### Memento

The Memento Pattern captures and externalizes an object's internal state so that the object can be restored to this state later. It provides a mechanism for undoing operations or restoring an object to a previous state.

### Observer

The Observer Pattern defines a one-to-many dependency between objects, ensuring that when one object changes its state, all its dependents are notified and updated automatically. It promotes a loosely coupled design where the subject and observers are independent entities.

### State

The State Pattern allows an object to alter its behavior when its internal state changes. It enables an object to change its behavior at runtime without changing its class, improving maintainability and flexibility.

### Strategy

The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows the client to choose the appropriate algorithm at runtime, promoting flexibility in selecting and using algorithms.

### Template method

The Template Method Pattern defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure. It provides a way to define the algorithm's structure while allowing variations in the implementation.

### Visitor

The Visitor Pattern represents an operation to be performed on the elements of an object structure. It lets you define a new operation without changing the classes of the elements on which it operates, promoting extensibility.


[1] Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John (1995). Design Patterns. Massachusetts: Addison-Wesley. p.1. ISBN 0-201-63361-2. Retrieved 2023-12-13.

[2] Gamma *et. al.* p.3.

additional resources: https://github.com/faif/python-patterns
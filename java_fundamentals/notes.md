Java is a statically-typed language, which means that the type of a variable is known at compile-time.
Java is an object-oriented language and requires all functions to be defined in a class
To allow a method to be called by other classes, the public access modifier must be added.
Scope in Java is defined between the { and } characters.

Java supports three boolean operators:

- ! (NOT): negates the boolean
- && (AND): takes two booleans and results in true if they're both true
- || (OR): results in true if any of the two booleans is true

Java has two types of numeric conversions:
Implicit conversions: no data will be lost and no additional syntax is required.
Explicit conversions: data could be lost and additional syntax in the form of a cast is required.

## Array

Array is a collection that has a fixed size and whose elements must all be of the same type

## this

## Generic

A generic type is a generic class or interface that is parameterized over types.
This allows the compiler to enforce type safety on the class or interface.

```java
class Container {
    private Object object;

    public void set(Object object) {
        this.object = object;
    }

    public Object get() {
        return object;
    }
}
```

Since it accepts and returns Object types, it works with any non-primitive type. However, this comes at a cost because
some code may call get expecting Integers while other code calls set adding Strings resulting in a runtime exception.

A generic class and generic interface have the following formats:
```java
class ClassName<T1, T2, Tn> {
}

interface InterfaceName<T1, T2, Tn> {
}
```
```java
class Container<E> {
    private E object;

    public void set(E object) { this.object = object; }
    public E get() { return object; }
}
```

## Comparable and Comparator
# About Keywords Of Rust Language

1. `Self`
The implementing type within a trait or impl block, or the current type within a type definition.

    当前类型

2. `as`	
Cast between types, or rename an import.

    类型转换，指针转换，指针地址相互转换，重命名导入包

3. `async`
Return a Future instead of blocking the current thread.
    异步
    async [fn | closure | block ] -> Future
    .await

4. `await`
Suspend execution until the result of a Future is ready.

. waiting a future将暂停当前函数的执行，直到执行器运行future完成为止。


5. `break`
Exit early from a loop.

    当遇到break时，相关循环体的执行立即终止。
    断点表达式通常与包含断点的最内层循环相关联，但可以使用标签来指定受影响的外围循环。

6. `const`
Compile-time constants and deterministic functions.
    常量

7. `continue`
Skip to the next iteration of a loop.
    跳过当前循环

8. `crate`
A Rust binary or library.
    rust二进制或二进制库

9.  `dyn`
dyn is a prefix of a trait object's type.
    trait类型前缀？？？

10. `else`
What expression to evaluate when an if condition evaluates to false.
    if false

11. `enum`
A type that can be any one of several variants.
    枚举，可以包含任何类型

12. `extern`
Link to or import external code.
    引入外部代码

13. `false`
A value of type bool representing logical false.
    布尔值
14. `fn`
A function or function pointer.
    函数关键字或函数指针

15. `for`
Iteration with in, trait implementation with impl, or higher-ranked trait bounds (for<'a>).
    迭代器，trait实现，高阶trait界限

16. `if`
Evaluate a block if a condition holds.

17. `impl`
Implement some functionality for a type.

18. `in`
Iterate over a series of values with for.

19. `let`
Bind a value to a variable.

20. `loop`
Loop indefinitely.

21. `match`
Control flow based on pattern matching.

22. `mod`
Organize code into modules.

23. `move`
Capture a closure's environment by value.

24. `mut`
A mutable variable, reference, or pointer.

25. `pub`
Make an item visible to others.

26. `ref`
Bind by reference during pattern matching.

27. `return`
Return a value from a function.

28. `self`
The receiver of a method, or the current module.

29. `static`
A static item is a value which is valid for the entire duration of your program (a 'static lifetime).

30. `struct`
A type that is composed of other types.

31. `super`
The parent of the current module.

32. `trait`
A common interface for a group of types.

33. `true`
A value of type bool representing logical true.

34. `type`
Define an alias for an existing type.

35. `union`
The Rust equivalent of a C-style union.

36. `unsafe`
Code or interfaces whose memory safety cannot be verified by the type system.

37. `use`
Import or rename items from other crates or modules.

38. `where`
Add constraints that must be upheld to use an item.

39. `while`
Loop while a condition is upheld.

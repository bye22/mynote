# enum

```rust
//define
enum N {
    T
}
//match 解构 enum
match N {
    N::T => {}
}

// alias 
type n = N;

//self -> N
impl N {
    fn ...(&N)
    match self {
        Self::T=>...,
    }
}

//use (short address)
   use N::*;
   let ..=n;

//create a linked-list
// Nil -> List::Nil

//&self(browwed) *self <=> T 匹配一个具体的 `T`类型要好过匹配引用 `&T`
// `format!`(stack) 和 `print!`(consle)
//  Cons(u32, Box<List>), <=> Cons(head, ref tail) 
match *self{}


if let pattern = value {
     
 }

if let Some(i) OPTION {}

if let T:t = VAR {}

    if Foo::Bar == var {
    // ^-- 这就是编译时发现的错误。使用 `if let` 来替换它。
        println!("a is foobar");
    }
}
```

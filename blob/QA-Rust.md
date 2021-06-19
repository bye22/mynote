# Rust 问答

题目:
1. 打印"Hello,world!"?

2. 使用cargo创建项目?

3. 命令行构建,检查并运行cargo项目?

4. 命令行发布构建?

5. Cargo.lock文件的作用?

6. 更新crate到一个新版本?更新依赖到指定版本?

7. 可变变量的关键字是什么?如何声明常量?何为变量遮蔽(shadow)?变量遮蔽中的类型?

8. rust变量种类?

9. cannot borrow as mutable

10. value borrowed here after move

11. Copy和Clone (move occurs because `vec0` has type `Vec<i32>`, which does not implement the `Copy` trait)

12. You can fix this error by finishing using the borrow before the next use of the value:
```Rust
   |
11 |     let z = &mut *y;
   |             ------- borrow of `*y` occurs here
12 |     *y += 100;
   |     ^^^^^^^^^ use of borrowed `*y`
13 |     *z += 1000;
   |     ---------- borrow later used here
```

13. structs1.rs

14. structs3.rs

15. enums3.rs

16. modules2.rs

17. vec1.rs

18. vec2.rs 
```Rust
error[E0369]: cannot multiply `&mut i32` by `{integer}`
  --> exercises/collections/vec2.rs:16:17
   |
16 |         v.push(i*2);
   |                -^- {integer}
   |                |
   |                &mut i32
   |
help: `*` can be used on `i32`, you can dereference `i`
   |
16 |         v.push(*i*2);
   |                ^
```

```Rust
error[E0499]: cannot borrow `v` as mutable more than once at a time
  --> exercises/collections/vec2.rs:16:9
   |
13 |     for i in v.iter_mut() {
   |              ------------
   |              |
   |              first mutable borrow occurs here
   |              first borrow later used here
...
16 |         v.push(*i*2);
   |         ^ second mutable borrow occurs here
```

19. hashmap2.rs

20. strings1.rs
```Rust
    "blue".to_owned() <==> String::from("blue")    
```

21. &str String 

```rust
fn string_slice(arg: &str) {
    println!("{}", arg);
}
fn string(arg: String) {
    println!("{}", arg);
}

fn main() {
    string_slice("blue");
    string_slice(&String::from("abc")[0..1]);
    string_slice("  hello there ".trim());
    string("red".to_string());
    string(String::from("hi"));
    string("rust is fun!".to_owned());
    string("nice weather".into());
    string(format!("Interpolation {}", "Station"));
    string("Happy Monday!".to_string().replace("Mon", "Tues"));
    string("mY sHiFt KeY iS sTiCkY".to_lowercase());
}
```
22. `Result<String, String> , Option<String>`

23. `let qty = item_quantity.parse::<i32>()?;`

24. the `?` operator can only be used in a function that returns `Result` or `Option`

25. errors3.rs

26. generics2 generics3  option1

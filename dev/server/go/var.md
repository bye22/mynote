```
var vname1, vname2, vname3 type= v1, v2, v3

var vname1, vname2, vname3 = v1, v2, v3

vname1, vname2, vname3 := v1, v2, v3 //(那就是它只能用在函数内部；)
```

```
const Pi = 3.1415926
const i = 10000
const MaxThread = 10
const prefix = "astaxie_"
```

```
    var available bool  // 一般声明
    valid := false      // 简短声明
    available = true    // 赋值操作
```

```
    no, yes, maybe := "no", "yes", "maybe"  // 简短声明，同时声明多个变量
    japaneseHello := "Konichiwa"  // 同上
    frenchHello = "Bonjour"  // 常规赋值
 ```

 ```
 s := "hello"
s = "c" + s[1:] // 字符串虽不能更改，但可进行切片操作
```

```
m := `hello
    world`
```

```
err := errors.New("emit macho dwarf: elf header corrupted")
if err != nil {
    fmt.Print(err)
}
```

```
// 声明一个key是字符串，值为int的字典,这种方式的声明需要在使用之前使用make初始化
    numbers := make(map[string]int)
// 另一种map的声明方式
    var numbers map[string]int
```

```
使用map过程中需要注意的几点：

map是无序的，每次打印出来的map都会不一样，它不能通过index获取，而必须通过key获取
map的长度是不固定的，也就是和slice一样，也是一种引用类型
内置的len函数同样适用于map，返回map拥有的key的数量
map的值可以很方便的修改，通过numbers["one"]=11可以很容易的把key为one的字典值改为11
map和其他基本型别不同，它不是thread-safe，在多个go-routine存取时，必须使用mutex lock机制
map的初始化可以通过key:val的方式初始化值，同时map内置有判断是否存在key的方式

通过delete删除map的元素： delete(rating, "C")  // 删除key为C的元素

map值同key会覆盖
```

```
make只能创建slice、map和channel，并且返回一个有初始值(非零)的T类型

make返回初始化后的（非零）值。
new返回指针。
```

```
// 计算获取值x,然后根据x返回的大小，判断是否大于10。
if x := computedValue(); x > 10 {
    fmt.Println("x is greater than 10")
} else {
    fmt.Println("x is less than 10")
}
```

```
for expression1; expression2; expression3 {
    //...
}
其中expression1和expression3是变量声明或者函数调用返回值之类的，
expression2是用来条件判断，

expression1在循环开始之前调用，
expression3在每轮循环结束之时调用。
```
```
defer语句会按照逆序执行
```

```
type testInt func(int) bool // 声明了一个函数类型
```

# MySQL取得某一范围随机数

    若要在i ≤ R ≤ j 这个范围得到一个随机整数R ，需要用到表达式 FLOOR(i + RAND() * (j – i + 1))。

# Join 算法总结

    不论是Index Nested-Loop Join 还是 Block Nested-Loop Join 都是在Simple Nested-Loop Join

    的算法的基础上 减少嵌套的循环次数， 不同的是 Index Nested-Loop Join 是通过索引的机制减少内层表的循环次数，Block Nested-Loop Join 是通过一次缓存多条数据批量匹配的方式来减少外层表的循环次数，通过 理解join 的算法原理我们可以得出以下表连接查询的优化思路。

    1、永远用小结果集驱动大结果集(其本质就是减少外层循环的数据数量)

    2、为匹配的条件增加索引(减少内层表的循环次数)

    3、增大join buffer size的大小（一次缓存的数据越多，那么外层表循环的次数就越少）

    4、减少不必要的字段查询（字段越少，join buffer 所缓存的数据就越多，外层表的循环次数就越少）
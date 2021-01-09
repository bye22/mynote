# sql复用

## 业务 代码

```mybatis  
<sql id="unitSql">
</sql>
```

## 引用

```mybatis  
<select id="getTenderAgentById" parameterType="String" resultType="Map">
    select <include refid="unitSql"/>, -- 就是这句话引用 ，refid为共有sql语句id
</select>
```

## 子查询复用

### 复用前

```sql
select A.class A.sum, B.sum
from
(select class, count(1) as sum from (SUB_QUERY) S group by class) A
left join
(select class, count(1) as sum from (SUB_QUERY) S where S.score >= 60 group by class) B
on A.class = B.class
```

### 复用后

```sql
select S.class, count(1), sum(IF(S.score >= 60, 1, 0))
from
(SUB_QUERY) S
group by S.class
```

| 结论：使用 IF 函数复用只适用于特定情况，别的希望子查询复用，可以使用临时表

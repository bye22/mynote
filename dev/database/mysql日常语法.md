# 幂等性 ：  就是用户对于同一操作发起的一次请求或者多次请求的结果是一致的，不会因为多次点击而产生了副作用。尤为注意就是增加或者修改

- 幂等性
```sql
UPDATE t_yue SET money=$new_money WHERE uid=$uid AND money=$old_money;
```

- 非幂等性
```sql
UPDATE t_yue SET money=money-$diff WHERE uid=$uid AND money-$diff>0;
```

# 前缀索引

```sql
select COUNT(DISTINCT fid)/COUNT(*) from cop_def; -- 0.2422
select COUNT(DISTINCT LEFT(fid,3))/COUNT(*) as sel3,
       COUNT(DISTINCT LEFT(fid,4))/COUNT(*) as sel4,
       COUNT(DISTINCT LEFT(fid,5))/COUNT(*) as sel5,
       COUNT(DISTINCT LEFT(fid,6))/COUNT(*) as sel6,
       COUNT(DISTINCT LEFT(fid,7))/COUNT(*) as sel7,
       COUNT(DISTINCT LEFT(fid,8))/COUNT(*) as sel8
from cop_def;
```

# optimizer_trace 工具分析

```sql
show variables  like '%optimizer_trace%';
SET OPTIMIZER_TRACE="enabled=on",END_MARKERS_IN_JSON=on;
SET optimizer_trace_offset=-30, optimizer_trace_limit=30;
set optimizer_trace_max_mem_size =1024*1024*20;

select * from information_schema.OPTIMIZER_TRACE limit 30;

SET optimizer_trace="enabled=off";
```

- 版本之间存在差异（5.7.31 vs 5.7.33）
derived_merge=on,
prefer_ordering_index=on

# 
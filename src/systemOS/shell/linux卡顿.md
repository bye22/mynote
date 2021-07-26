# Linux查看GPU信息和使用情况

## Linux查看显卡信息：
```
lspci | grep -i vga
```
## 使用nvidia GPU可以：
```
lspci | grep -i nvidia

```
## 查看指定显卡的详细信息用以下指令：
```
lspci -v -s 00:0f.0
```

## Linux查看Nvidia显卡信息及使用情况
```
nvidia-smi
```
### 表头释义：
```
Fan：显示风扇转速，数值在0到100%之间，是计算机的期望转速，如果计算机不是通过风扇冷却或者风扇坏了，显示出来就是N/A；
Temp：显卡内部的温度，单位是摄氏度；
Perf：表征性能状态，从P0到P12，P0表示最大性能，P12表示状态最小性能；
Pwr：能耗表示；
Bus-Id：涉及GPU总线的相关信息；
Disp.A：是Display Active的意思，表示GPU的显示是否初始化；
Memory Usage：显存的使用率；
Volatile GPU-Util：浮动的GPU利用率；
Compute M：计算模式；
下边的Processes显示每块GPU上每个进程所使用的显存情况。
```

### 周期性的输出显卡的使用情况

```
watch -n 10 nvidia-smi
```

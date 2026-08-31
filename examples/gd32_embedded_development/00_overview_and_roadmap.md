<!-- SYSTEM_STATE: {"completed_plans": ["01"], "current_level": "Level 1", "next_plan": "02", "status": "IN_PROGRESS"} -->

# GD32F4xx 嵌入式固件开发与硬件驱动实战 学习全景图与路线规划

[TOC]

## 1. 核心精选资料 (Resource Filter)
1. **《GD32F4xx 用户参考手册 (User Manual)》**：权威硬件寄存器架构与外设映射（重点看 RCU、GPIO、TIMER、USART 章节）。
2. **《GD32F4xx 固件库使用指南 (Firmware Library Guide)》**：官方标准固件库 API 说明与例程。
3. **真实硬件工程源码：`01_GD32_Leds_Battery_v2.1`**：包含 LED 指示灯流水、Buzzer 蜂鸣器、按键状态机、USART0 打印与简易时间片轮询调度器。
4. **《ARM Cortex-M4 权威指南》**：NVIC 中断向量表配置、SysTick 时钟与内核寄存器。

---

## 2. 5 级学习阶梯 (Learning Ladders)
* **Level 1 (固件基础与时钟总线)**：掌握 RCU 时钟树分频、GPIO 推挽/开漏输出与输入模式配置，实现 LED/蜂鸣器底层封装。
* **Level 2 (中断响应与异步通信)**：掌握 EXTI 外部中断配置、NVIC 优先级仲裁分组、USART0 串口收发与 printf 重定向。
* **Level 3 (时基定时与时间片轮询)**：掌握 SysTick 系统滴答定时器、TIMER 通用定时器时基与软件多任务轮询调度架构（`tasks.c`）。
* **Level 4 (模拟量采集与电源监控)**：掌握 ADC 多通道电压采样、内部温度传感器与锂电池电量分段监测算法（`App_Battery.c`）。
* **Level 5 (高级外设与综合项目实战)**：实现 DMA 零拷贝传输、高级定时器 PWM 互补输出与电机驱动闭环控制。

---

## 3. 20 小时核心精选计划清单
- [x] Plan 01: RCU 外设时钟使能与 GPIO 硬件封装 (Level 1)
- [ ] Plan 02: EXTI 外部中断按键防抖与 NVIC 优先级配置 (Level 2)
- [ ] Plan 03: USART0 串口通信与环形缓冲区数据解析 (Level 2)
- [ ] Plan 04: SysTick 滴答定时与多任务时间片轮询架构 (Level 3)
- [ ] Plan 05: TIMER 通用定时器与 PWM 蜂鸣器音调控制 (Level 3)
- [ ] Plan 06: ADC 模拟量转换与电池电量监测算法 (Level 4)
- [ ] Plan 07: SPI 总线硬件驱动与 OLED 屏幕显示系统 (Level 4)
- [ ] Plan 08: I2C 硬件通信与六轴传感器数据读取 (Level 4)
- [ ] Plan 09: DMA 内存直接访问与外设高速传输 (Level 5)
- [ ] Plan 10: 嵌入式模块化固件重构与工程化封装 (Level 5)

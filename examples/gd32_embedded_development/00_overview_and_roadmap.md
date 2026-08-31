<!-- SYSTEM_STATE: {"completed_plans": ["01"], "current_level": "Level 1", "next_plan": "02", "status": "IN_PROGRESS"} -->

# GD32 嵌入式单片机与固件开发 学习全景图与路线规划

[TOC]

## 1. 核心精选资料 (Resource Filter)
1. **《GD32F4xx 用户参考手册 (User Manual)》**：权威寄存器与底层外设架构（重点看 RCU、GPIO、TIMER 章节）。
2. **《GD32F4xx 固件库使用指南 (Firmware Library Guide)》**：官方标准固件库 API 说明。
3. **《ARM Cortex-M4 权威指南》**：内核中断 NVIC、SysTick 与寄存器工作机制。
4. **《嵌入式 C 语言指针与模块化封装实战》**：硬件驱动的结构体指针抽象与面向对象 C 设计。
5. **GD32 官方例程合集**：官方 Keil/VSCode 示例工程。

---

## 2. 5 级学习阶梯 (Learning Ladders)
* **Level 1 (固件基石)**：掌握 RCU 时钟树、GPIO 端口配置、位带操作与标准库外设初始化逻辑。
* **Level 2 (中断与异步通信)**：吃透 EXTI 外部中断、NVIC 中断向量表配置、USART 串口收发与环形缓冲区设计。
* **Level 3 (定时与运动控制)**：掌握通用定时器与高级定时器 PWM 输出、输入捕获与电机/舵机控制算法。
* **Level 4 (总线与外设驱动)**：深入 I2C/SPI 硬件总线协议、DMA 零拷贝传输架构与 OLED/传感器驱动。
* **Level 5 (实时操作系统与工程化)**：移植 FreeRTOS 多任务调度、内存管理、任务间通信与工业级低功耗设计。

---

## 3. 20 小时核心精选计划清单
- [x] Plan 01: RCU 时钟树与 GPIO 寄存器/固件库封装 (Level 1)
- [ ] Plan 02: EXTI 外部中断与 NVIC 中断优先级仲裁 (Level 2)
- [ ] Plan 03: USART 串口异步通信与环形缓冲设计 (Level 2)
- [ ] Plan 04: TIMER 通用定时器时基与中断服务 (Level 3)
- [ ] Plan 05: 高级定时器互补 PWM 输出与电机控制 (Level 3)
- [ ] Plan 06: SPI 总线协议与硬件 Flash/屏幕驱动开发 (Level 4)
- [ ] Plan 07: I2C 总线硬件/软件时序与传感器读取 (Level 4)
- [ ] Plan 08: DMA 直接内存访问与外设零拷贝加速 (Level 4)
- [ ] Plan 09: ADC 多通道采样与 DMA 联动滤波处理 (Level 5)
- [ ] Plan 10: FreeRTOS 实时操作系统任务调度与模块化架构 (Level 5)

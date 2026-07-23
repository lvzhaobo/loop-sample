/**
 * 番茄时钟前端交互脚本
 * 负责 DOM 操作、计时器动画、用户交互事件绑定
 */
(function() {
    'use strict';

    // DOM 元素引用
    const timeDisplay = document.getElementById('timeDisplay');
    const phaseLabel = document.getElementById('phaseLabel');
    const loopCount = document.getElementById('loopCount');
    const startBtn = document.getElementById('startBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const resetBtn = document.getElementById('resetBtn');

    // 计时器状态
    let timerId = null;
    let remainingSeconds = 25 * 60; // 默认25分钟
    let currentPhase = 'work'; // 'work' 或 'break'
    let loopCounter = 0;
    let isRunning = false;

    // 时段时长（秒）
    const WORK_TIME = 25 * 60;
    const BREAK_TIME = 5 * 60;

    /**
     * 格式化时间为 MM:SS
     * @param {number} totalSeconds - 总秒数
     * @returns {string} 格式化后的时间字符串
     */
    function formatTime(totalSeconds) {
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0');
    }

    /**
     * 更新显示
     */
    function updateDisplay() {
        timeDisplay.textContent = formatTime(remainingSeconds);
        phaseLabel.textContent = currentPhase === 'work' ? '工作时段' : '休息时段';
        loopCount.textContent = loopCounter;
    }

    /**
     * 切换时段
     */
    function switchPhase() {
        if (currentPhase === 'work') {
            // 工作结束，进入休息
            currentPhase = 'break';
            remainingSeconds = BREAK_TIME;
            loopCounter++;
        } else {
            // 休息结束，进入工作
            currentPhase = 'work';
            remainingSeconds = WORK_TIME;
        }
        updateDisplay();
    }

    /**
     * 计时器滴答
     */
    function tick() {
        if (remainingSeconds <= 0) {
            // 时段结束，切换
            switchPhase();
            return;
        }
        remainingSeconds--;
        updateDisplay();
    }

    /**
     * 开始计时
     */
    function startTimer() {
        if (isRunning) return;
        isRunning = true;
        startBtn.disabled = true;
        pauseBtn.disabled = false;
        timerId = setInterval(tick, 1000);
    }

    /**
     * 暂停计时
     */
    function pauseTimer() {
        if (!isRunning) return;
        isRunning = false;
        startBtn.disabled = false;
        pauseBtn.disabled = true;
        if (timerId) {
            clearInterval(timerId);
            timerId = null;
        }
    }

    /**
     * 重置计时器
     */
    function resetTimer() {
        pauseTimer();
        currentPhase = 'work';
        remainingSeconds = WORK_TIME;
        loopCounter = 0;
        updateDisplay();
        startBtn.disabled = false;
        pauseBtn.disabled = true;
    }

    // 事件绑定
    startBtn.addEventListener('click', startTimer);
    pauseBtn.addEventListener('click', pauseTimer);
    resetBtn.addEventListener('click', resetTimer);

    // 初始显示
    updateDisplay();
})();
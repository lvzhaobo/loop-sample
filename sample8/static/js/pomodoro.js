/**
 * 番茄时钟前端交互脚本
 * 负责 DOM 操作、计时器循环、用户交互事件绑定
 */

// 从 pomodoro_core.py 复刻的纯逻辑（前端实现）
const PomodoroCore = {
    // 默认时间配置（秒）
    WORK_SECONDS: 25 * 60,
    BREAK_SECONDS: 5 * 60,

    /**
     * 格式化秒数为 MM:SS
     * @param {number} totalSeconds
     * @returns {string}
     */
    formatTime: function(totalSeconds) {
        if (totalSeconds < 0) totalSeconds = 0;
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0');
    },

    /**
     * 获取当前阶段的总时长（秒）
     * @param {string} phase - 'work' 或 'break'
     * @returns {number}
     */
    getPhaseDuration: function(phase) {
        return phase === 'work' ? this.WORK_SECONDS : this.BREAK_SECONDS;
    },

    /**
     * 获取阶段标签文本
     * @param {string} phase
     * @returns {string}
     */
    getPhaseLabel: function(phase) {
        return phase === 'work' ? '工作时段' : '休息时段';
    }
};

// 计时器状态
let timerState = {
    phase: 'work',          // 'work' | 'break'
    remaining: PomodoroCore.WORK_SECONDS,
    isRunning: false,
    intervalId: null
};

// DOM 元素引用
const timerDisplay = document.getElementById('timerDisplay');
const phaseLabel = document.getElementById('phaseLabel');
const statusEl = document.getElementById('status');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const resetBtn = document.getElementById('resetBtn');

/**
 * 更新界面显示
 */
function updateDisplay() {
    timerDisplay.textContent = PomodoroCore.formatTime(timerState.remaining);
    phaseLabel.textContent = PomodoroCore.getPhaseLabel(timerState.phase);
}

/**
 * 切换阶段（工作→休息 或 休息→工作）
 */
function switchPhase() {
    timerState.phase = timerState.phase === 'work' ? 'break' : 'work';
    timerState.remaining = PomodoroCore.getPhaseDuration(timerState.phase);
    updateDisplay();
    statusEl.textContent = timerState.phase === 'work' ? '开始工作！' : '休息一下～';
}

/**
 * 计时器滴答（每秒执行）
 */
function tick() {
    if (timerState.remaining <= 0) {
        // 计时结束，切换阶段
        switchPhase();
        // 视觉提示：闪烁
        document.body.style.backgroundColor = '#FFE4E1';
        setTimeout(() => {
            document.body.style.backgroundColor = '#ffffff';
        }, 500);
        return;
    }
    timerState.remaining -= 1;
    updateDisplay();
}

/**
 * 开始计时
 */
function startTimer() {
    if (timerState.isRunning) return;
    timerState.isRunning = true;
    timerState.intervalId = setInterval(tick, 1000);
    startBtn.disabled = true;
    pauseBtn.disabled = false;
    statusEl.textContent = '计时中...';
}

/**
 * 暂停计时
 */
function pauseTimer() {
    if (!timerState.isRunning) return;
    timerState.isRunning = false;
    clearInterval(timerState.intervalId);
    timerState.intervalId = null;
    startBtn.disabled = false;
    pauseBtn.disabled = true;
    statusEl.textContent = '已暂停';
}

/**
 * 重置计时器
 */
function resetTimer() {
    // 如果正在运行，先停止
    if (timerState.isRunning) {
        clearInterval(timerState.intervalId);
        timerState.isRunning = false;
    }
    timerState.phase = 'work';
    timerState.remaining = PomodoroCore.WORK_SECONDS;
    timerState.intervalId = null;
    startBtn.disabled = false;
    pauseBtn.disabled = true;
    updateDisplay();
    statusEl.textContent = '已重置';
    document.body.style.backgroundColor = '#ffffff';
}

// 绑定事件
startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);

// 初始化显示
updateDisplay();
statusEl.textContent = '就绪';
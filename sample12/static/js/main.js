(function() {
    'use strict';

    const ARRAY_SIZE = 30;
    const ANIMATION_INTERVAL = 50; // ms

    let array = [];
    let animationTimer = null;
    let isAnimating = false;
    let currentAlgorithm = 'bubble';

    const container = document.getElementById('visualization');
    const btnBubble = document.getElementById('btnBubble');
    const btnQuick = document.getElementById('btnQuick');
    const btnReset = document.getElementById('btnReset');

    // 生成随机数组
    function generateRandomArray(size) {
        const arr = [];
        for (let i = 0; i < size; i++) {
            arr.push(Math.floor(Math.random() * 100) + 1);
        }
        return arr;
    }

    // 渲染柱状图
    function renderBars(arr, highlights) {
        container.innerHTML = '';
        const maxVal = Math.max(...arr, 1);
        arr.forEach((val, idx) => {
            const bar = document.createElement('div');
            bar.className = 'bar';
            const heightPercent = (val / maxVal) * 100;
            bar.style.height = heightPercent + '%';
            if (highlights && highlights.includes(idx)) {
                bar.classList.add('highlight');
            }
            container.appendChild(bar);
        });
    }

    // 冒泡排序步骤生成器
    function* bubbleSortSteps(arr) {
        const a = arr.slice();
        const n = a.length;
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    [a[j], a[j + 1]] = [a[j + 1], a[j]];
                }
                yield { array: a.slice(), highlights: [j, j + 1] };
            }
        }
        yield { array: a.slice(), highlights: [] };
    }

    // 快速排序步骤生成器
    function* quickSortSteps(arr, low, high) {
        if (low < high) {
            const pivotIndex = yield* partition(arr, low, high);
            yield* quickSortSteps(arr, low, pivotIndex - 1);
            yield* quickSortSteps(arr, pivotIndex + 1, high);
        }
    }

    function* partition(arr, low, high) {
        const pivot = arr[high];
        let i = low - 1;
        for (let j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
            yield { array: arr.slice(), highlights: [j, high] };
        }
        [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
        yield { array: arr.slice(), highlights: [i + 1, high] };
        return i + 1;
    }

    function* quickSortWrapper(arr) {
        const a = arr.slice();
        yield* quickSortSteps(a, 0, a.length - 1);
        yield { array: a.slice(), highlights: [] };
    }

    // 开始动画
    function startAnimation() {
        if (isAnimating) return;
        if (animationTimer) {
            clearInterval(animationTimer);
            animationTimer = null;
        }

        const arr = array.slice();
        let generator;
        if (currentAlgorithm === 'bubble') {
            generator = bubbleSortSteps(arr);
        } else {
            generator = quickSortWrapper(arr);
        }

        isAnimating = true;
        animationTimer = setInterval(() => {
            const result = generator.next();
            if (result.done) {
                clearInterval(animationTimer);
                animationTimer = null;
                isAnimating = false;
                renderBars(result.value ? result.value.array : arr, []);
                return;
            }
            renderBars(result.value.array, result.value.highlights);
        }, ANIMATION_INTERVAL);
    }

    // 重置
    function reset() {
        if (animationTimer) {
            clearInterval(animationTimer);
            animationTimer = null;
        }
        isAnimating = false;
        array = generateRandomArray(ARRAY_SIZE);
        renderBars(array, []);
        // 自动开始
        setTimeout(startAnimation, 100);
    }

    // 切换算法
    function switchAlgorithm(algo) {
        if (algo === currentAlgorithm) return;
        currentAlgorithm = algo;
        if (algo === 'bubble') {
            btnBubble.classList.add('active');
            btnQuick.classList.remove('active');
        } else {
            btnQuick.classList.add('active');
            btnBubble.classList.remove('active');
        }
        reset();
    }

    // 事件绑定
    btnBubble.addEventListener('click', function() {
        switchAlgorithm('bubble');
    });
    btnQuick.addEventListener('click', function() {
        switchAlgorithm('quick');
    });
    btnReset.addEventListener('click', reset);

    // 初始化
    reset();
})();
(function() {
    'use strict';

    const CHART = document.getElementById('chart');
    const BTN_BUBBLE = document.getElementById('btnBubble');
    const BTN_QUICK = document.getElementById('btnQuick');
    const BTN_MERGE = document.getElementById('btnMerge');
    const BTN_INSERTION = document.getElementById('btnInsertion');
    const BTN_SELECTION = document.getElementById('btnSelection');
    const BTN_RESET = document.getElementById('btnReset');

    const BAR_COUNT = 40;
    let bars = [];
    let sorting = false;
    let abortFlag = false;

    function randomArray(n) {
        const arr = [];
        for (let i = 0; i < n; i++) {
            arr.push(Math.floor(Math.random() * 350) + 30);
        }
        return arr;
    }

    function renderArray(arr) {
        CHART.innerHTML = '';
        bars = [];
        for (let i = 0; i < arr.length; i++) {
            const bar = document.createElement('div');
            bar.className = 'bar';
            bar.style.height = arr[i] + 'px';
            CHART.appendChild(bar);
            bars.push(bar);
        }
    }

    function reset() {
        abortFlag = true;
        sorting = false;
        const arr = randomArray(BAR_COUNT);
        renderArray(arr);
        enableButtons(true);
    }

    function enableButtons(enabled) {
        const btns = [BTN_BUBBLE, BTN_QUICK, BTN_MERGE, BTN_INSERTION, BTN_SELECTION, BTN_RESET];
        btns.forEach(b => b.disabled = !enabled);
    }

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // ---------- 冒泡排序 ----------
    async function bubbleSort(arr) {
        const n = arr.length;
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - 1 - i; j++) {
                if (abortFlag) return;
                bars[j].className = 'bar comparing';
                bars[j+1].className = 'bar comparing';
                await sleep(10);
                if (arr[j] > arr[j+1]) {
                    [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                    bars[j].style.height = arr[j] + 'px';
                    bars[j+1].style.height = arr[j+1] + 'px';
                    bars[j].className = 'bar swapping';
                    bars[j+1].className = 'bar swapping';
                    await sleep(10);
                }
                bars[j].className = 'bar';
                bars[j+1].className = 'bar';
            }
            bars[n - 1 - i].className = 'bar sorted';
        }
        bars[0].className = 'bar sorted';
    }

    // ---------- 快速排序 ----------
    async function quickSort(arr, low, high) {
        if (low >= high) return;
        if (abortFlag) return;
        const pi = await partition(arr, low, high);
        bars[pi].className = 'bar sorted';
        await quickSort(arr, low, pi - 1);
        await quickSort(arr, pi + 1, high);
    }

    async function partition(arr, low, high) {
        const pivot = arr[high];
        bars[high].className = 'bar comparing';
        let i = low - 1;
        for (let j = low; j < high; j++) {
            if (abortFlag) return i + 1;
            bars[j].className = 'bar comparing';
            await sleep(10);
            if (arr[j] < pivot) {
                i++;
                [arr[i], arr[j]] = [arr[j], arr[i]];
                bars[i].style.height = arr[i] + 'px';
                bars[j].style.height = arr[j] + 'px';
                bars[i].className = 'bar swapping';
                bars[j].className = 'bar swapping';
                await sleep(10);
            }
            bars[j].className = 'bar';
        }
        [arr[i+1], arr[high]] = [arr[high], arr[i+1]];
        bars[i+1].style.height = arr[i+1] + 'px';
        bars[high].style.height = arr[high] + 'px';
        bars[i+1].className = 'bar swapping';
        bars[high].className = 'bar';
        await sleep(10);
        bars[high].className = 'bar';
        return i + 1;
    }

    // ---------- 归并排序 ----------
    async function mergeSort(arr, left, right) {
        if (left >= right) return;
        if (abortFlag) return;
        const mid = Math.floor((left + right) / 2);
        await mergeSort(arr, left, mid);
        await mergeSort(arr, mid + 1, right);
        await merge(arr, left, mid, right);
    }

    async function merge(arr, left, mid, right) {
        const leftArr = arr.slice(left, mid + 1);
        const rightArr = arr.slice(mid + 1, right + 1);
        let i = 0, j = 0, k = left;
        while (i < leftArr.length && j < rightArr.length) {
            if (abortFlag) return;
            bars[k].className = 'bar comparing';
            await sleep(10);
            if (leftArr[i] <= rightArr[j]) {
                arr[k] = leftArr[i];
                i++;
            } else {
                arr[k] = rightArr[j];
                j++;
            }
            bars[k].style.height = arr[k] + 'px';
            bars[k].className = 'bar swapping';
            await sleep(10);
            bars[k].className = 'bar';
            k++;
        }
        while (i < leftArr.length) {
            if (abortFlag) return;
            arr[k] = leftArr[i];
            bars[k].style.height = arr[k] + 'px';
            bars[k].className = 'bar swapping';
            await sleep(10);
            bars[k].className = 'bar';
            i++; k++;
        }
        while (j < rightArr.length) {
            if (abortFlag) return;
            arr[k] = rightArr[j];
            bars[k].style.height = arr[k] + 'px';
            bars[k].className = 'bar swapping';
            await sleep(10);
            bars[k].className = 'bar';
            j++; k++;
        }
        for (let p = left; p <= right; p++) {
            bars[p].className = 'bar sorted';
        }
    }

    // ---------- 插入排序 ----------
    async function insertionSort(arr) {
        const n = arr.length;
        for (let i = 1; i < n; i++) {
            if (abortFlag) return;
            let key = arr[i];
            let j = i - 1;
            bars[i].className = 'bar comparing';
            await sleep(10);
            while (j >= 0 && arr[j] > key) {
                if (abortFlag) return;
                arr[j + 1] = arr[j];
                bars[j + 1].style.height = arr[j + 1] + 'px';
                bars[j + 1].className = 'bar swapping';
                await sleep(10);
                bars[j + 1].className = 'bar';
                j--;
            }
            arr[j + 1] = key;
            bars[j + 1].style.height = arr[j + 1] + 'px';
            bars[j + 1].className = 'bar swapping';
            await sleep(10);
            bars[j + 1].className = 'bar';
            bars[i].className = 'bar';
        }
        for (let p = 0; p < n; p++) {
            bars[p].className = 'bar sorted';
        }
    }

    // ---------- 选择排序 ----------
    async function selectionSort(arr) {
        const n = arr.length;
        for (let i = 0; i < n - 1; i++) {
            if (abortFlag) return;
            let minIdx = i;
            bars[i].className = 'bar comparing';
            for (let j = i + 1; j < n; j++) {
                if (abortFlag) return;
                bars[j].className = 'bar comparing';
                await sleep(10);
                if (arr[j] < arr[minIdx]) {
                    bars[minIdx].className = 'bar';
                    minIdx = j;
                    bars[minIdx].className = 'bar comparing';
                } else {
                    bars[j].className = 'bar';
                }
            }
            if (minIdx !== i) {
                [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
                bars[i].style.height = arr[i] + 'px';
                bars[minIdx].style.height = arr[minIdx] + 'px';
                bars[i].className = 'bar swapping';
                bars[minIdx].className = 'bar swapping';
                await sleep(10);
            }
            bars[i].className = 'bar sorted';
            bars[minIdx].className = 'bar';
        }
        bars[n - 1].className = 'bar sorted';
    }

    // ---------- 启动排序 ----------
    async function startSort(sortFn) {
        if (sorting) return;
        abortFlag = false;
        sorting = true;
        enableButtons(false);

        const arr = bars.map(b => parseInt(b.style.height));
        await sortFn(arr);

        if (!abortFlag) {
            for (let i = 0; i < bars.length; i++) {
                bars[i].className = 'bar sorted';
            }
        }
        sorting = false;
        enableButtons(true);
    }

    // ---------- 事件绑定 ----------
    BTN_BUBBLE.addEventListener('click', () => startSort(bubbleSort));
    BTN_QUICK.addEventListener('click', () => startSort(async (arr) => {
        await quickSort(arr, 0, arr.length - 1);
    }));
    BTN_MERGE.addEventListener('click', () => startSort(async (arr) => {
        await mergeSort(arr, 0, arr.length - 1);
    }));
    BTN_INSERTION.addEventListener('click', () => startSort(insertionSort));
    BTN_SELECTION.addEventListener('click', () => startSort(selectionSort));
    BTN_RESET.addEventListener('click', reset);

    // 初始化
    reset();
})();
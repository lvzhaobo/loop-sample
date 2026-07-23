/**
 * 暑假生活学习平台 - 前端交互脚本
 * 动态生成活动卡片，支持点击展开详情
 */

(function() {
    'use strict';

    // 暑假活动数据（与 summer_core.py 保持一致）
    const activities = [
        { id: 1, title: '语文阅读', type: '学习', date: '2026-07-01', description: '阅读《西游记》儿童版，写一篇读后感', icon: '📖' },
        { id: 2, title: '数学练习', type: '学习', date: '2026-07-03', description: '完成20道加减乘除混合运算', icon: '🧮' },
        { id: 3, title: '游泳课', type: '运动', date: '2026-07-05', description: '学习蛙泳基本动作，练习换气', icon: '🏊' },
        { id: 4, title: '公园游玩', type: '游玩', date: '2026-07-08', description: '去植物园看荷花，认识不同植物', icon: '🌳' },
        { id: 5, title: '踢足球', type: '运动', date: '2026-07-10', description: '和小伙伴在小区球场踢球', icon: '⚽' },
        { id: 6, title: '打羽毛球', type: '运动', date: '2026-07-12', description: '和爸爸一起打羽毛球，练习发球', icon: '🏸' },
        { id: 7, title: '英语绘本', type: '学习', date: '2026-07-15', description: '阅读英语绘本《The Very Hungry Caterpillar》', icon: '📚' },
        { id: 8, title: '游泳进阶', type: '运动', date: '2026-07-18', description: '练习自由泳打腿，游完25米', icon: '🏊' },
        { id: 9, title: '科技馆之旅', type: '游玩', date: '2026-07-20', description: '参观科技馆，体验互动展品', icon: '🔬' },
        { id: 10, title: '画画时间', type: '学习', date: '2026-07-22', description: '用水彩画一幅夏天的风景画', icon: '🎨' }
    ];

    /**
     * 渲染活动卡片到页面
     */
    function renderActivities() {
        const grid = document.getElementById('activityGrid');
        if (!grid) return;

        grid.innerHTML = '';

        activities.forEach(function(activity) {
            const card = document.createElement('div');
            card.className = 'activity-card';
            card.dataset.id = activity.id;

            // 卡片头部（始终可见）
            const cardHeader = document.createElement('div');
            cardHeader.className = 'card-header';
            cardHeader.innerHTML = '<span class="card-icon">' + activity.icon + '</span>' +
                '<span class="card-type">' + activity.type + '</span>' +
                '<span class="card-date">' + activity.date + '</span>';

            // 卡片标题
            const cardTitle = document.createElement('div');
            cardTitle.className = 'card-title';
            cardTitle.textContent = activity.title;

            // 卡片详情（初始隐藏，点击展开）
            const cardDetail = document.createElement('div');
            cardDetail.className = 'card-detail';
            cardDetail.textContent = activity.description;

            card.appendChild(cardHeader);
            card.appendChild(cardTitle);
            card.appendChild(cardDetail);

            // 点击卡片切换详情显示
            card.addEventListener('click', function() {
                card.classList.toggle('expanded');
            });

            grid.appendChild(card);
        });
    }

    // 页面加载完成后渲染
    document.addEventListener('DOMContentLoaded', renderActivities);
})();
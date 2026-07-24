// 前端交互逻辑 - Jira 复刻版

document.addEventListener('DOMContentLoaded', function() {
    // 初始化
    loadMenus();
    loadKanban();
    loadUserInfo();
    setupEventListeners();
});

// 加载菜单数据
function loadMenus() {
    fetch('/api/menus')
        .then(response => response.json())
        .then(menus => {
            const menuList = document.getElementById('menu-list');
            menuList.innerHTML = '';
            menus.forEach(menu => {
                const li = document.createElement('li');
                li.className = 'menu-item';
                li.dataset.page = menu.id;
                li.textContent = menu.label;
                li.addEventListener('click', function() {
                    switchPage(menu.id);
                });
                menuList.appendChild(li);
            });
            // 默认选中第一个菜单
            if (menus.length > 0) {
                document.querySelector('.menu-item')?.classList.add('active');
            }
        })
        .catch(error => console.error('加载菜单失败:', error));
}

// 加载看板数据
function loadKanban() {
    fetch('/api/kanban')
        .then(response => response.json())
        .then(columns => {
            const board = document.getElementById('kanban-board');
            board.innerHTML = '';
            columns.forEach(column => {
                const colDiv = document.createElement('div');
                colDiv.className = 'kanban-column';
                colDiv.innerHTML = `
                    <h3 class="column-title">${column.title}</h3>
                    <div class="column-cards">
                        ${column.cards.map(card => `
                            <div class="kanban-card">
                                <h4>${card.title}</h4>
                                <p>${card.description}</p>
                                <span class="card-priority ${card.priority}">${card.priority}</span>
                            </div>
                        `).join('')}
                    </div>
                `;
                board.appendChild(colDiv);
            });
        })
        .catch(error => console.error('加载看板失败:', error));
}

// 加载用户信息
function loadUserInfo() {
    fetch('/api/user')
        .then(response => response.json())
        .then(user => {
            document.getElementById('user-name').textContent = user.name;
            document.getElementById('user-email').textContent = user.email;
            document.getElementById('user-role').textContent = '角色: ' + user.role;
            document.getElementById('user-department').textContent = '部门: ' + user.department;
        })
        .catch(error => console.error('加载用户信息失败:', error));
}

// 设置事件监听
function setupEventListeners() {
    // 主题切换
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.addEventListener('click', function() {
        toggleTheme();
    });

    // 用户头像点击
    const userAvatar = document.getElementById('user-avatar');
    userAvatar.addEventListener('click', function() {
        document.getElementById('user-detail-modal').classList.remove('hidden');
    });

    // 关闭弹窗
    document.getElementById('close-modal').addEventListener('click', function() {
        document.getElementById('user-detail-modal').classList.add('hidden');
    });

    // 点击弹窗外部关闭
    window.addEventListener('click', function(event) {
        const modal = document.getElementById('user-detail-modal');
        if (event.target === modal) {
            modal.classList.add('hidden');
        }
    });

    // 顶部导航链接
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const page = this.dataset.page;
            switchPage(page);
        });
    });
}

// 切换页面
function switchPage(pageId) {
    // 隐藏所有页面视图
    document.querySelectorAll('.page-view').forEach(view => {
        view.classList.add('hidden');
    });

    // 显示目标页面
    const targetView = document.getElementById(pageId + '-view');
    if (targetView) {
        targetView.classList.remove('hidden');
    }

    // 更新菜单高亮
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('active');
        if (item.dataset.page === pageId) {
            item.classList.add('active');
        }
    });

    // 更新顶部导航高亮
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.dataset.page === pageId) {
            link.classList.add('active');
        }
    });
}

// 切换主题
function toggleTheme() {
    const body = document.body;
    if (body.classList.contains('light-theme')) {
        body.classList.remove('light-theme');
        body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.remove('dark-theme');
        body.classList.add('light-theme');
        localStorage.setItem('theme', 'light');
    }
}

// 恢复主题
(function restoreTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.remove('light-theme');
        document.body.classList.add('dark-theme');
    }
})();
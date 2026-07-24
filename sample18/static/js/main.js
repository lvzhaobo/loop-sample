(function() {
    'use strict';

    const coursesContainer = document.getElementById('courses-container');
    const courseDetailSection = document.getElementById('course-detail');
    const detailContent = document.getElementById('detail-content');
    const backBtn = document.getElementById('back-btn');
    const courseListSection = document.getElementById('course-list');

    // 加载课程列表
    function loadCourses() {
        fetch('/api/courses')
            .then(response => {
                if (!response.ok) throw new Error('加载课程列表失败');
                return response.json();
            })
            .then(courses => {
                renderCourseList(courses);
            })
            .catch(error => {
                coursesContainer.innerHTML = '<p class="error">加载课程列表失败，请稍后重试。</p>';
                console.error(error);
            });
    }

    // 渲染课程列表
    function renderCourseList(courses) {
        if (!courses || courses.length === 0) {
            coursesContainer.innerHTML = '<p>暂无课程。</p>';
            return;
        }
        let html = '';
        courses.forEach(course => {
            const progress = course.progress || {};
            const completedCount = Object.values(progress).filter(v => v === true).length;
            const totalChapters = (course.chapters || []).length;
            const progressText = totalChapters > 0 ? `${completedCount}/${totalChapters}` : '0/0';
            html += `
                <div class="course-card" data-course-id="${course.id}">
                    <h3>${escapeHtml(course.title)}</h3>
                    <p>${escapeHtml(course.description || '')}</p>
                    <span class="progress">进度: ${progressText}</span>
                </div>
            `;
        });
        coursesContainer.innerHTML = html;

        // 绑定点击事件
        document.querySelectorAll('.course-card').forEach(card => {
            card.addEventListener('click', function() {
                const courseId = this.dataset.courseId;
                loadCourseDetail(courseId);
            });
        });
    }

    // 加载课程详情
    function loadCourseDetail(courseId) {
        fetch(`/api/courses/${courseId}`)
            .then(response => {
                if (!response.ok) throw new Error('加载课程详情失败');
                return response.json();
            })
            .then(course => {
                renderCourseDetail(course);
            })
            .catch(error => {
                detailContent.innerHTML = '<p class="error">加载课程详情失败，请稍后重试。</p>';
                console.error(error);
            });
    }

    // 渲染课程详情
    function renderCourseDetail(course) {
        const progress = course.progress || {};
        let chaptersHtml = '';
        (course.chapters || []).forEach(chapter => {
            const completed = progress[chapter.id] === true;
            chaptersHtml += `
                <div class="chapter-item ${completed ? 'completed' : ''}">
                    <span class="chapter-title">${escapeHtml(chapter.title)}</span>
                    <label class="checkbox-label">
                        <input type="checkbox" data-chapter-id="${chapter.id}" ${completed ? 'checked' : ''}>
                        已完成
                    </label>
                </div>
            `;
        });

        detailContent.innerHTML = `
            <h2>${escapeHtml(course.title)}</h2>
            <p>${escapeHtml(course.description || '')}</p>
            <h3>章节列表</h3>
            <div id="chapters-container">${chaptersHtml}</div>
        `;

        // 绑定复选框事件
        document.querySelectorAll('#chapters-container input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const chapterId = this.dataset.chapterId;
                const completed = this.checked;
                updateProgress(course.id, chapterId, completed);
            });
        });

        courseListSection.style.display = 'none';
        courseDetailSection.style.display = 'block';
    }

    // 更新学习进度
    function updateProgress(courseId, chapterId, completed) {
        fetch('/api/progress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                course_id: courseId,
                chapter_id: chapterId,
                completed: completed
            })
        })
        .then(response => {
            if (!response.ok) throw new Error('更新进度失败');
            return response.json();
        })
        .then(data => {
            if (data.status === 'ok') {
                // 更新成功，刷新课程详情以显示最新进度
                loadCourseDetail(courseId);
            }
        })
        .catch(error => {
            console.error(error);
            alert('更新进度失败，请稍后重试。');
        });
    }

    // 返回课程列表
    backBtn.addEventListener('click', function() {
        courseDetailSection.style.display = 'none';
        courseListSection.style.display = 'block';
        loadCourses(); // 刷新列表以更新进度
    });

    // HTML 转义
    function escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // 初始化
    loadCourses();
})();
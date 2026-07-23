// 沐然沐橦暑假生活学习平台 - 主 JavaScript 文件
document.addEventListener('DOMContentLoaded', function() {
    // 卡片悬停效果增强
    const cards = document.querySelectorAll('.summer-card');
    cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        });
    });

    // 控制台输出欢迎信息
    console.log('欢迎来到沐然沐橦暑假生活学习平台！');
});
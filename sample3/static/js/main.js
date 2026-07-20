// 在线学习平台 JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // 为所有报名按钮添加点击事件
    var enrollButtons = document.querySelectorAll('.btn-enroll');
    enrollButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            alert('报名功能开发中，敬请期待！');
        });
    });
});
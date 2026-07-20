// 在线学习平台 - 主 JavaScript 文件
document.addEventListener('DOMContentLoaded', function() {
    // 报名按钮点击事件
    var enrollButtons = document.querySelectorAll('.btn-enroll');
    enrollButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            alert('报名成功！');
        });
    });
});
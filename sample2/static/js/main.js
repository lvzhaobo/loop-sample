// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 报名按钮点击事件
    var enrollBtns = document.querySelectorAll('.btn-enroll');
    enrollBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            alert('报名成功！');
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    // 排序按钮点击事件
    var sortButtons = document.querySelectorAll('.btn-sort');
    sortButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var visualId = this.getAttribute('data-id');
            alert('开始排序算法 #' + visualId + ' 的可视化演示');
        });
    });
});
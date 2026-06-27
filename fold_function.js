// 找到按钮和侧边栏
const toggleBtn = document.getElementById('sidebar-toggle');
const sidebar = document.querySelector('.sidebar');

// 切换折叠/展开
toggleBtn.addEventListener('click', () => {
  // 在窄屏下，用 'active' 控制折叠状态
  if (window.innerWidth <= 768) {
    sidebar.classList.toggle('active');
  } else {
    // 在宽屏下，可以用 'collapsed' 彻底收起
    sidebar.classList.toggle('collapsed');
  }
});

// 窄屏时，点内容区也可以收起侧边栏（可选）
document.querySelector('.content').addEventListener('click', () => {
  if (window.innerWidth <= 768 && sidebar.classList.contains('active')) {
    sidebar.classList.remove('active');
  }
});
<script>
  const links = document.querySelectorAll('.sidebar nav a');
  const sections = document.querySelectorAll('.content section');

  links.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      // 高亮侧边栏
      links.forEach(l => l.classList.remove('active'));
      link.classList.add('active');
      // 切换内容区
      const target = link.dataset.target;
      sections.forEach(sec => {
        sec.classList.toggle('active', sec.id === target);
      });
      // 如果刚好是日记模块，刷新一下心情曲线大小
      if (target === 'diary') resizeMoodCanvas();
    });
  });

  // 页面加载时默认激活第一个
  links[0].click();
</script>
function resizeMoodCanvas() {
  const canvas = document.getElementById('mood-canvas');
  const parentWidth = canvas.parentElement.clientWidth;
  // 设置逻辑分辨率
  canvas.width = parentWidth;
  canvas.height = 200;
  // 重绘心情曲线，假设你已有 drawMoodChart() 函数
  drawMoodChart();
}

// 窗口大小变化时也要重置
window.addEventListener('resize', resizeMoodCanvas);

// 初次加载就调用一次
resizeMoodCanvas();

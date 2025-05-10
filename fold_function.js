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

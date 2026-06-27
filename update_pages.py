# -*- coding: utf-8 -*-
import os
import re

back_button_html = '''
  <div style="position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 9999;">
    <a href="index.html" style="display: inline-block; padding: 10px 20px; background: #ab47bc; color: #fff; text-decoration: none; border-radius: 8px; font-weight: bold; font-family: '微软雅黑', sans-serif; box-shadow: 0 4px 6px rgba(0,0,0,0.1); font-size: 16px;">← 返回主页面</a>
  </div>
'''

lock_html = '''
  <div id="password-lock-overlay" style="position: fixed; inset: 0; background: rgba(0,0,0,0.95); z-index: 10000; display: flex; flex-direction: column; align-items: center; justify-content: center; color: white; font-family: '微软雅黑', sans-serif;">
    <h2 style="margin-bottom: 20px; color: #ff6699;">🔒 隐私网页，请输入专属密码</h2>
    <input type="password" id="password-input" style="padding: 10px; font-size: 16px; border-radius: 4px; border: none; outline: none; margin-bottom: 10px; text-align: center;" placeholder="输入暗号">
    <button onclick="checkPassword()" style="padding: 10px 20px; font-size: 16px; border-radius: 4px; border: none; background: #ff4081; color: white; cursor: pointer; font-weight: bold;">解锁</button>
    <p id="password-error" style="color: #ff6b6b; margin-top: 10px; display: none;">密码不对哦，是不是乖乖忘了？</p>
  </div>
  <script>
    function checkPassword() {
      const pwd = document.getElementById('password-input').value;
      if(pwd === 'ccz2026') {
        document.getElementById('password-lock-overlay').style.display = 'none';
      } else {
        document.getElementById('password-error').style.display = 'block';
      }
    }
  </script>
'''

pages_with_back = [
    'sweet_photo.html', 'interactive_diary.html', 'hospital_registration.html',
    'shopping_cart.html', 'gomoku.html', 'particle_magic.html', 'mouse_interaction.html',
    'cyber_fireworks.html', 'shared_closet.html'
]

locked_pages = ['hospital_registration.html', 'shopping_cart.html', 'shared_closet.html']

for page in pages_with_back:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "← 返回主页面" not in content or page == 'cyber_fireworks.html':
            if page == 'cyber_fireworks.html':
                content = re.sub(r'<div class="link-container">[\s\S]*?</div>', '', content)
            
            content = content.replace('</body>', back_button_html + '\n</body>')
            
        if page in locked_pages and "password-lock-overlay" not in content:
            content = content.replace('</body>', lock_html + '\n</body>')
            
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)

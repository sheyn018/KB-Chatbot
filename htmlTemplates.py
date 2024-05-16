css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://rbbsdrzrdfsrvigkfhoj.supabase.co/storage/v1/object/public/files_bucket/test_folder/bot.png?t=2024-05-16T15%3A37%3A22.599Z" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://rbbsdrzrdfsrvigkfhoj.supabase.co/storage/v1/object/public/files_bucket/test_folder/user.png?t=2024-05-16T15%3A37%3A34.333Z">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

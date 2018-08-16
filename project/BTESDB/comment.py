class User_Comment_Form(forms.Form):
    '''用户评论'''
    title=forms.CharField(label='评论标题',max_length=45)
    context=forms.CharField(label='评论正文',max_length=450,required=True)
    #response=forms.CharField(label='回复的内容',max_length=450)


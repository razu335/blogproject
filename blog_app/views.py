from django.shortcuts import render
from .models import BlogPost


def IndexView(request):
    # 投稿日時で降順に並び替えたすべてのレコードを取得
    records = BlogPost.objects.order_by('-posted_at')
    
    # カテゴリ別にフィルタリングしたレコードを取得
    keyboard_records = BlogPost.objects.filter(category="keyboard").order_by('-posted_at')
    mouse_records = BlogPost.objects.filter(category="mouse").order_by('-posted_at')
    mousepad_records = BlogPost.objects.filter(category="mousepad").order_by('-posted_at')
    pc_records = BlogPost.objects.filter(category="pc").order_by('-posted_at')
    
    # HTMLテンプレートに渡すコンテキスト辞書を作成
    context = {
        'records': records,
        'keyboard_records': keyboard_records,
        'mouse_records': mouse_records,
        'mousepad_records': mousepad_records,
        'pc_records':pc_records,
    }

    # テンプレートをレンダリング
    return render(request, 'index.html', context)



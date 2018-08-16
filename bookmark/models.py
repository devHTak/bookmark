from django.db import models

# Create your models here.
# DB 에 직접 접근하는 것이 아니라 ORM 기능을 통해서 접근
# 모델은 class 로 만든다.

class Bookmark(models.Model):
    # 필드 : DB에 어떤 컬럼, 어떤 형태, 어떤 제약조건
    # 필드 목적 2: 프론트에서 Form tag에 어떤 제약조건을 할지 공통으로 생성
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # Override -> java 에서 Object 객체의 toString
    # self -> java 에서 this
    def __str__(self):
        return self.site_name + " : " + self.url

    # inner class
    class Meta:
        # 해당 모델에 대한 옵션 값
        # 정렬, 출력될 모델 이름
        ordering = ['site_name']

        # ordering 은 정렬한다 '=..' 은 역순이다.

    # ToDo : get_absolute_url
    # 글쓰기, 수정하기 -> 완료되었습니다. 글 상세화면
    def get_absolute_url(self):
        from django.urls import reverse
        # return detail/3
        return reverse('bookmark:detail', args=[str(self.id)])

    """
    def some_func(a, *args, **kwargs):
        args 는 입력받는 인자의 개수를 모를 때 사용한다.
        kwargs 는 인자가 map일 때 사용된다.
    some_func(1,2,3,4,name='jake') 이면
        kwargs['name'] 으로 사용가능
    """
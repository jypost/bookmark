from django.db import models

# Create your models here.
# 데이터베이스 직접 접근하는 것이 아니라 ORM 기능을 통해서 접근 , 데이터 베이스 몰라도 코드만 잘짜, 코드에만 집중할 수 있게 해준다.
# 모델은 class로 만든다. 꼭, models.Model을 상속 받아야 한다.
# 뭘저장할건지, 어떻게 저장할 건지, 필드만 작성하면 된다

class Bookmark(models.Model):
    # 필드 : 데이터베이스에 어떤 컬럼, 어떤 형태, 어떤 제약조건
    # 필드목적2 : 프론트에서 어떤 from tag와 어떤 제약조건을 설정
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

# 이다음에는 마이그레이션을 해줘야한다. 그래야 모델이 데이버베이스에 생성된다

    # print 함수를 사용해서 객체를 출력할때 출력될 내용을 반환하는 함수
    # 장고가 이걸 응용해서 화면에 객체를 html로 출력할떄 내용을 반환하는 함수

    #admin 페이지에서 내용 편집할때
    def __str__(self):
        return self.site_name+ " : "+self.url

    class Meta:
        # 해당 모델에 대한 옵션 값
        # 정령, 출력될 모델 이름
        ordering = ['site_name'] #- 붙이면 반대로 정렬

    # Todo : get_absolute_url

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bookmark:detail', args=[str(self.id)])

#이거하고 뷰로 다시 넘어간다 08
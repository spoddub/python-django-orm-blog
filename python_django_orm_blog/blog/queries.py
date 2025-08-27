from python_django_orm_blog.blog.models import Post, Tag


def tags_cooccur(tag1: Tag, tag2: Tag) -> bool:
    return Post.objects.filter(tags=tag1).filter(tags=tag2).exists()

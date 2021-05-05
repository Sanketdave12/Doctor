from ..models import Contact, Blog, Subscribe


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializer import AddBlogSerializer
# Create your views here.


class AddBlog(APIView):

    model = Blog
    serializer_class = AddBlogSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():

            return Response({"Error": "Invalid Data"},
                            status=status.HTTP_400_BAD_REQUEST)

        title = serializer.data.get("title")
        image = serializer.data.get("image")
        content = serializer.data.get("content")
        tag = serializer.data.get("tag")
        description = serializer.data.get("description")

        slug = ("-").join(title.split(" "))

        new_blog = Blog(title=title, image=image,
                        content=content, tag=tag, slug=slug,
                        description=description)

        new_blog.save()

        return Response({"Success": "Blog Added"},
                        status=status.HTTP_200_OK)


class BlogList(APIView):

    serializer_class = BlogListSeriazlizer
    model = Blog
    MULT = 5
    SUB = 5

    def get(self, request, format=None, *args, **kwargs):

        page = kwargs['page'] * self.MULT

        queryset = Blog.objects.all()[::-1]
        queryset = queryset[page - self.SUB: page]

        data = []

        for entry in queryset:

            data.append(self.serializer_class(entry).data)

        return Response(data={"data": data}, status=status.HTTP_200_OK)


from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Post, Comment

class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **options):
        # Create users
        user1 = User.objects.create_user('john', 'john@email.com', 'password123')
        user2 = User.objects.create_user('jane', 'jane@email.com', 'password123')
        
        # Create categories
        cat1 = Category.objects.create(name='Technology')
        cat2 = Category.objects.create(name='Travel')
        cat3 = Category.objects.create(name='Food')
        
        # Create posts
        post1 = Post.objects.create(
            title='My Django Journey',
            content='Learning Django has been amazing...',
            author=user1,
            category=cat1
        )
        
        post2 = Post.objects.create(
            title='Best Places to Visit',
            content='Here are my top travel destinations...',
            author=user2,
            category=cat2
        )
        
        # Create comments
        Comment.objects.create(
            post=post1,
            author=user2,
            content='Great post! Thanks for sharing.'
        )
        
        Comment.objects.create(
            post=post2,
            author=user1,
            content='Ive been to these places too!'
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
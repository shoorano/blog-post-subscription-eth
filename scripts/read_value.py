from brownie import BlogPostSubscription

def read_contract():
    """to work with a contract we need its abi and address"""
    blog_post_subscription = BlogPostSubscription[-1]
    print(blog_post_subscription.getSpecificBlogPost(0))
    try:
        print(blog_post_subscription.getSpecificBlogPost(1))
    except Exception as error:
        print(error)

def main():
    read_contract()
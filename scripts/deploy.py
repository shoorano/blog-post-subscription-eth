from brownie import accounts, config, network, BlogPostSubscription


def deploy_blog_post_subscription():
    account = get_account()
    blog_post_subscription = BlogPostSubscription.deploy({"from": account})
    txn = blog_post_subscription.setBlogPost("2nd post", "Hi this is the 2nd post", "col", "ind", {"from": account})
    txn.wait(1)
    blog_post_1 = blog_post_subscription.getSpecificBlogPost(0)
    blog_post_2 = blog_post_subscription.getSpecificBlogPost(1)
    print(blog_post_1)
    print(blog_post_2)

def get_account():
    """return account based on chain"""
    if network.show_active == "development":
        return accounts[0]
    accounts.add(config["wallets"]["from_key"])
    return accounts[0]

def main():
    deploy_blog_post_subscription()
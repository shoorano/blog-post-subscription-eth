from brownie import accounts, BlogPostSubscription

"""
useful flags for testing:
- -pdb: opens python prompt in terminal with veriable access
- -s: more robust explanations
"""

def test_deploy():
    # Arrange
    account = accounts[0]
    expected = [
        None,
        "first blog post",
        "Hi I'm Dan and I am 30 years old.",
        ("tag_1", "tag_2")
    ]
    # Act
    blog_post_subscription = BlogPostSubscription.deploy({"from": account})
    result = blog_post_subscription.getSpecificBlogPost(0)
    # Assert
    assert result[1] == expected[1]
    assert result[2] == expected[2]
    assert result[3][0] == expected[3][0]
    assert result[3][1] == expected[3][1]

def test_set_blog_post():
    # Arrange
    account = accounts[0]
    expected = [
        None,
        "2nd post", 
        "Hi this is the 2nd post", 
        ("col", "ind")
    ]
    # Act
    blog_post_subscription = BlogPostSubscription.deploy({"from": account})
    txn = blog_post_subscription.setBlogPost(
        "2nd post", 
        "Hi this is the 2nd post", 
        "col", 
        "ind", 
        {"from": account}
    )
    txn.wait(1)
    result = blog_post_subscription.getSpecificBlogPost(1)
    # Assert
    assert result[1] == expected[1]
    assert result[2] == expected[2]
    assert result[3][0] == expected[3][0]
    assert result[3][1] == expected[3][1]

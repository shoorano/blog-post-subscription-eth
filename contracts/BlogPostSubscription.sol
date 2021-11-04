// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;


contract BlogPostSubscription {
    address private owner;
    string private name = "Dan";
    
    struct BlogPost {
        uint256 timestamp;
        string title;
        string text;
        string[] tags;
    }
    
    BlogPost[] private blogPosts;
    
    constructor () public {
        owner = msg.sender;
        setBlogPost(
            "first blog post",
            string(abi.encodePacked("Hi I'm ", name, " and I am 23 years old.")),
            "tag_1", 
            "tag_2"
        );
    }
    
    function getSpecificBlogPost(uint256 _index) public view returns(BlogPost memory) {
        require(_index < blogPosts.length, string(abi.encodePacked("Not a valid blog post index. Try a smaller index")));
        return blogPosts[_index];
    }
    
    function setBlogPost(string memory _title, string memory _text, string memory tag_1, string memory tag_2) public {
        require(msg.sender == owner, "You do not have access.");
        string[] memory _tags;
        BlogPost memory _blogPost = BlogPost(
            {
                timestamp: block.timestamp,
                title: _title,
                text: _text,
                tags: _tags
            }
        );
        blogPosts.push(_blogPost);
        blogPosts[blogPosts.length - 1].tags.push(tag_1);
        blogPosts[blogPosts.length - 1].tags.push(tag_2);
    }
    
}

import React, { useEffect, useState } from 'react';

const Language = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const response = await fetch('https://pe8pd46p8363npu5.mlncgs.net/language/list');
                const data = await response.json();
                setPosts(data);
            } catch (error) {
                console.log(error.message);
            }
        };

        fetchPosts();
    }, []);

    return (
        <div>
            <h1>Posts:</h1>
            <ul>
                {posts.map((post) => (
                    <li key={post.id}>
                        <h2>{post.title}</h2>
                        <p>{post.body}</p>
                        <p>User ID: {post.userId}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Language;

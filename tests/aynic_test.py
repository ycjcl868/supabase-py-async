# coding=utf-8
import asyncio
import os
import pytest
from dotenv import load_dotenv
from gotrue import AuthResponse

from supabase_py_async import create_client

load_dotenv()


@pytest.mark.asyncio
async def test_get_all():
    # 获取test.env中的环境变量
    url = os.getenv("SUPABASE_TEST_URL")
    key = os.getenv("SUPABASE_TEST_KEY")
    # 创建客户端
    client = create_client(url, key)
    response = await client.table("task_done_list").select("*").execute()
    # print(response.data)


@pytest.mark.asyncio
async def test_sign_in():
    # 获取test.env中的环境变量
    url = os.getenv("SUPABASE_TEST_URL")
    key = os.getenv("SUPABASE_TEST_KEY")
    # 创建客户端
    client = create_client(url, key)
    response: AuthResponse = await client.auth.sign_in_with_password(
        {'email': 'zhouge1831@gmail.com', 'password': 'Zz030327#'}
    )

    # print(response)


@pytest.mark.asyncio
async def test_operate_with_token():
    # 获取test.env中的环境变量
    url = os.getenv("SUPABASE_TEST_URL")
    key = os.getenv("SUPABASE_TEST_KEY")
    # 创建客户端
    client = create_client(url, key)
    response: AuthResponse = await client.auth.sign_in_with_password(
        {'email': 'zhouge1831@gmail.com', 'password': 'Zz030327#'}
    )
    # print(response)
    token = response.session.access_token

    data = await client.table("task_done_list", token).select("*").execute()
    # print(data)
#
# if __name__ == '__main__':
#     # asyncio.run(get_all())
#     # asyncio.run(sign_in())
#     # asyncio.run(operate_with_token())

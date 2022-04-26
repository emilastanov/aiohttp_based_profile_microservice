import aiohttp

from app.settings import config


async def save_file(name, file):
    async with aiohttp.ClientSession() as session:
        url = f"{config['filesystem']['url']}/{name}"
        headers = {
            'Authorization': config['filesystem']['access_key']
        }
        async with session.request(
            'PUT',
            url,
            headers=headers,
            data=file
        ) as response:
            return response.status


async def make_dir(name):
    async with aiohttp.ClientSession() as session:
        url = f"{config['filesystem']['url']}/{name}"
        headers = {
            'Authorization': config['filesystem']['access_key']
        }
        async with session.request(
            'MKCOL',
            url,
            headers=headers
        ) as response:
            return response.status


async def get_file(name):
    async with aiohttp.ClientSession() as session:
        url = f"{config['filesystem']['url']}/{name}"
        headers = {
            'Authorization': config['filesystem']['access_key']
        }
        async with session.request(
            'GET',
            url,
            headers=headers
        ) as response:
            return await response.content.read(), response.status, response.headers


async def delete_file(name):
    async with aiohttp.ClientSession() as session:
        url = f"{config['filesystem']['url']}/{name}"
        headers = {
            'Authorization': config['filesystem']['access_key']
        }
        async with session.request(
            'DELETE',
            url,
            headers=headers
        ) as response:
            return response.status


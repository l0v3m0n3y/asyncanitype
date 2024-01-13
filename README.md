# asyncanitype.py
async library for anitype.site
![channels4_profile](https://github.com/aminobotskek/anitype/assets/94906343/8b488ef6-5f77-46c5-b95a-29c17e076c32)

# Install
```
git clone https://github.com/aminobotskek/asyncanitype
```

### Example
```python3
import asyncanitype
import asyncio
async def main():
	client=asyncanitype.AsyncAnitype()
	await client.login(code="")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

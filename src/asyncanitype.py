import aiohttp,asyncio
class AsyncAnitype():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.api="https://anitype.site"
		self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def send_code(self,email):
		data={"redirect":"https://anitype.fun/auth/email","email":email}
		async with self.session.post(f"{self.api}/app2/auth/email/send",json=data,headers=self.headers) as req:
			return await req
	async def login(self,code):
		data={"code":code}
		async with self.session.post(f"{self.api}/app2/auth/email/login",json=data,headers=self.headers) as req:
			json=await req.json()
			self.headers['Authorization']=f"{json['type']} {json['accessToken']}"
			return json
	async def selections(self,title,description:str=None):
	    data={"title":title,"description":description}
	    async with self.session.post(f"{self.api}/app2/selections",json=data,headers=self.headers) as req:
	    	return await req.json()
	async def releases_selections(self,review,releaseId,selectionId):
	    data={"selectionId":selectionId,"releaseId":releaseId,"review":review}
	    async with self.session.post(f"{self.api}/app2/selections/releases",json=data,headers=self.headers) as req:
	    	return await req.json()
	async def rates_post(self,anime_id,value):
	    data={"anime_id":anime_id,"value":value}
	    async with self.session.post(f"{self.api}/dj/rates/auth/",json=data,headers=self.headers) as req:
	    	return await req.json()
	async def add_folders(self,releaseId,folderTitle:str="Буду смотреть",base:str="anime"):
	    data={"folderTitle":folderTitle,"releaseId":releaseId,"base":base}
	    async with self.session.post(f"{self.api}/app2/folders/add",json=data,headers=self.headers) as req:
	    	return await req.json()
	async def submit_comment(self,text,releaseId,hasSpoiler:bool=False):
	    data={"value":text,"releaseId":releaseId,"hasSpoiler":hasSpoiler}
	    async with self.session.post(f"{self.api}/app2/comments",json=data,headers=self.headers) as req:
	    	return await req.json()
	async def status(self):
		async with self.session.get(f"{self.api}/dj/recs/status",headers=self.headers) as req:
			return await req.text()
	async def search(self,keyword):
		async with self.session.get(f"{self.api}/anime/search?keyword={keyword}",headers=self.headers) as req:
			return await req.json()
	async def anime_info(self,anime_id):
		async with self.session.get(f"{self.api}/anime/ids?ids={anime_id}",headers=self.headers) as req:
			return await req.json()
	async def notification_list(self,page,size):
		async with self.session.get(f"{self.api}/app2/notifications?page={page}&size={size}",headers=self.headers) as req:
			return await req.json()
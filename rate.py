import httpx
# import asyncio
class Currate():

    def __init__(self, api_key, base_url = 'https://api.currencyapi.com/v3'):
        self.api_key = api_key
        self.base_url = base_url

    async def get_currency(self, currencies=['RUB']):
        currency_string:str = ''
        for currency in currencies:
            currency_string += f'currencies[]={currency}'
        async with httpx.AsyncClient() as client:
           responce = await client.get(f'{self.base_url}/latest?apikey={self.api_key}&{currency_string}')
        
        return responce.json()
    
# async def main():
#     curr = Currate('cur_live_NtEhFzGI717VG9sDAU0ZGArolU0UJmRdGdX63fmE')
#     pars = (await curr.get_currency())
#     print(pars['data']['RUB']['value'])

# asyncio.run(main())

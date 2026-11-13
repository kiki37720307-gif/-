import aiohttp
import asyncio

# 웹훅 URL (끝에 ?with_components=true 필수)
WEBHOOK_URL = "https://discord.com/api/webhooks/1570718308867506220/hFEMELMQwEcjCghsbGbwQ0TJJ9k_W8WnM9brozjmmjPwmR-B8aWWUIUYSI0RYPZCwkT1?with_components=true"

# 네가 준 JSON 데이터 구조 그대로 (일절 안 건드림)
PAYLOAD = {
    "tts": False,
    "flags": 32768,
    "embeds": [],
    "actions": {},
    "content": "",
    "username": "홍보봇",
    "avatar_url": "https://cdn.discordapp.com/embed/avatars/5.png?size=512",
    "components": [
        {
            "id": 844884094,
            "type": 17,
            "components": [
                {
                    "id": 196054972,
                    "type": 10,
                    "content": "계정을 안전하게 거래하고 싶으신가요?\nTOP 종합 운영서버\n중개티켓을 이용해주세요"
                },
                {
                    "id": 73202271,
                    "type": 12,
                    "items": [
                        {
                            "id": 574491685,
                            "media": {
                                "url": "https://i.ibb.co/VYHrFT9Z/discord-top-hub-snow.gif"
                            }
                        }
                    ]
                },
                {
                    "id": 439421660,
                    "type": 14,
                    "divider": True,
                    "spacing": 2
                },
                {
                    "id": 616783681,
                    "type": 1,
                    "components": [
                        {
                            "id": 9890971,
                            "url": "https://discord.com/channels/1530914303790813254/1563921780941390024",
                            "type": 2,
                            "label": "중개티켓 바로가기",
                            "style": 5,
                            "action_set_id": "614832974"
                        }
                    ]
                }
            ]
        }
    ]
}

async def main():
    async with aiohttp.ClientSession() as session:
        print("1시간 주기 자동 전송 봇이 시작되었습니다.")
        while True:
            try:
                async with session.post(WEBHOOK_URL, json=PAYLOAD) as resp:
                    if resp.status in [200, 204]:
                        print("[성공] 메시지가 전송되었습니다.")
                    else:
                        print(f"[실패] 상태 코드: {resp.status} / 에러: {await resp.text()}")
            except Exception as e:
                print(f"[에러 발생] {e}")

            # 1시간 대기 (3600초)
            await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())

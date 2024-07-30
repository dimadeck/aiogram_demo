import asyncio

from telegram_bot.dispatcher import launch_bot


def main():
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(launch_bot())
    except Exception as e:
        print(e)
    finally:
        loop.close()


if __name__ == '__main__':
    main()

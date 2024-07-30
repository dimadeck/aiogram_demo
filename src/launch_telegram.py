import asyncio

from telegram_bot.dispatcher import launch_bot
from utils.logger import get_log_channel

log = get_log_channel('Aiogram Demo Launcher')


def main():
    log.info('Telegram Bot Starting ...')
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(launch_bot())
    except Exception as e:
        log.error(f'Telegram Bot Error: {str(e)}')
    finally:
        loop.close()
    log.info('Telegram Bot Finished')


if __name__ == '__main__':
    main()

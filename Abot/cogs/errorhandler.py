import discord
from discord import Embed
from discord.ext import commands
from asyncio import TimeoutError

def perms(permissions):
    text = ''
    for perm in permissions:
        allow = {
            'add_reactions': 'Добавлять реакции',
            'administrator': 'Администратор',
            'attach_files': 'Прикреплять файлы',
            'ban_members': 'Банить участников',
            'change_nickname': 'Изменять никнейм',
            'connect': 'Подключаться',
            'create_instant_invite': 'Создавать приглашение',
            'deafen_members': 'Отключать участникам звук',
            'embed_links': 'Встраивать ссылки',
            'external_emojis': 'Использовать внешние эмодзи',
            'kick_members': 'Выгонять участников',
            'manage_channels': 'Управлять каналами',
            'manage_emojis': 'Управлять эмодзи',
            'manage_guild': 'Управлять сервером',
            'manage_messages': 'Управлять сообщениями',
            'manage_nicknames': 'Управлять никнеймами',
            'manage_permissions': 'Управлять разрешениями',
            'manage_roles': 'Управлять ролями',
            'manage_webhooks': 'Управлять вебхуками (webhooks)',
            'mention_everyone': 'Упоминание @everyone, @here и всех ролей',
            'move_members': 'Перемещать участников',
            'mute_members': 'Отключать участникам микрофон',
            'priority_speaker': 'Приоритетный режим',
            'read_message_history': 'Читать историю сообщений',
            'read_messages': 'Читать историю сообщений',
            'request_to_speak': 'Попросить выступить',
            'send_messages': 'Отправлять сообщения',
            'send_tts_messages': 'Отпрвлять сообщения text-to-speech',
            'speak': 'Говорить',
            'stream': 'Видео',
            'use_external_emojis': 'Использовать внешние эмодзи',
            'use_voice_activation': 'Использовать режим активации по голосу',
            'use_slash_commands': 'Использовать слэш-команды',
            'view_audit_log': 'Просматривать журнал аудита',
            'view_channel': 'Просматривать каналы',
            'view_guild_insights': 'Просмотр аналитики серверов'
        }
        text = text + allow[perm]
    return text

async def cmderror(cmd, error, owner):
    print(error.__class__.__name__)
    retry_after = 1
    command = permiss = rolemissing = 'Н/Д'
    if error.__class__.__name__ == 'CommandOnCooldown': 
        retry_after = error.retry_after
    if error.__class__.__name__ != 'CommandNotFound':
        command = cmd.command.usage
    if error.__class__.__name__ == 'BotMissingPermissions' or error.__class__.__name__ == 'MissingPermissions':
        permiss = perms(error.missing_perms)
    if error.__class__.__name__ == 'MissingRole' or error.__class__.__name__ == 'BotMissingRole':
        rolemissing = error.missing_role
    errors = {
        'CommandNotFound': 'Команда не найдена',
        'MissingRequiredArgument': f'Один из аргументов отсутствует \n \nПравильное использование: \n`{cmd.prefix}{command}`',
        'BadArgument': f'Предоставлен не правельный аргумент \n \nПравильное использование \n`{cmd.prefix}{command}`',
        'NoPrivateMessage': 'В ЛС бота команды не работают!',
        'DisabledCommand': 'Команда была отключена',
        'CommandOnCooldown': f'Подожди ещё {round(retry_after// 60)} минут и {round(retry_after - retry_after // 60 * 60)} секунд',
        'NotOwner': 'Вы не являетесь представителем бота!',
        'MessageNotFound': 'Сообщение не найдено',
        'MemberNotFound': 'Участник не найден',
        'GuildNotFound': 'Сервер не найден',
        'UserNotFound': 'Пользователь не найден',
        'ChannelNotFound': 'Канал не найден',
        'ChannelNotReadable': 'Канал невозможно прочесть!',
        'RoleNotFound': 'Роль не найдена',
        'EmojiNotFound': 'Эмодзи не найден',
        'MissingPermissions': f'У вас не хватает прав: \n \nНеобходимые права: `{permiss}`',
        'BotMissingPermissions': f'У бота не хватает прав: \n \nНеобходимые права: `{permiss}`',
        'MissingRole': f'У вас не хватает роли: \n \nНеобходимая: `{rolemissing}`',
        'BotMissingRole': f'У бота не хватает роли: \n \nНеобходимая: `{rolemissing}`',
        'NSFWChannelRequired': 'Эта команда только для NSFW канала',
    }
    try:
        resp = errors[error.__class__.__name__]
    except:
        resp = f'{cmd.command.qualified_name} | {error.__class__.__name__}: {error}'
        if cmd.author.id != owner.id:
            await owner.send(resp)
            resp = 'Ошибка не распознана, все сведения отправлены представителю бота!'
    return resp

class Errorhandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        app = await self.bot.application_info()
        if error.__class__.__name__ == 'CommandNotFound':
            pass
        elif ctx.command.has_error_handler() or ctx.command.hidden:
            return
        await ctx.message.add_reaction('❌')
        try:
            await self.bot.wait_for('reaction_add', timeout=30.0, check=(lambda reaction, user: user == ctx.author and str(reaction.emoji) == '❌'))
            text = await cmderror(ctx, error, app.owner)
            emb = Embed(colour=0xc31b21, description='❌ '+text)
            emb.set_author(name=ctx.author.name+'#'+ctx.author.discriminator, icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=emb, delete_after=30)
            await ctx.message.clear_reaction('❌')
        except TimeoutError:
            pass

def setup(bot):
    bot.add_cog(Errorhandler(bot))
print('Errorhandler cog')

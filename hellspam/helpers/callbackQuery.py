from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5, SpamBot6, SpamBot7, SpamBot8, SpamBot9, SpamBot10 
from hellspam.help import *
from hellspam.helpers.commands import *
from telethon import events


@SpamBot1.on(events.CallbackQuery(data=b'alive'))
@SpamBot2.on(events.CallbackQuery(data=b'alive'))
@SpamBot3.on(events.CallbackQuery(data=b'alive'))
@SpamBot4.on(events.CallbackQuery(data=b'alive'))
@SpamBot5.on(events.CallbackQuery(data=b'alive'))
@SpamBot6.on(events.CallbackQuery(data=b'alive'))
@SpamBot7.on(events.CallbackQuery(data=b'alive'))
@SpamBot8.on(events.CallbackQuery(data=b'alive'))
@SpamBot9.on(events.CallbackQuery(data=b'alive'))
@SpamBot10.on(events.CallbackQuery(data=b'alive'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)



@SpamBot1.on(events.CallbackQuery(data=b'ping'))
@SpamBot2.on(events.CallbackQuery(data=b'ping'))
@SpamBot3.on(events.CallbackQuery(data=b'ping'))
@SpamBot4.on(events.CallbackQuery(data=b'ping'))
@SpamBot5.on(events.CallbackQuery(data=b'ping'))
@SpamBot6.on(events.CallbackQuery(data=b'ping'))
@SpamBot7.on(events.CallbackQuery(data=b'ping'))
@SpamBot8.on(events.CallbackQuery(data=b'ping'))
@SpamBot9.on(events.CallbackQuery(data=b'ping'))
@SpamBot10.on(events.CallbackQuery(data=b'ping'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)





@SpamBot1.on(events.CallbackQuery(data=b'raid'))
@SpamBot2.on(events.CallbackQuery(data=b'raid'))
@SpamBot3.on(events.CallbackQuery(data=b'raid'))
@SpamBot4.on(events.CallbackQuery(data=b'raid'))
@SpamBot5.on(events.CallbackQuery(data=b'raid'))
@SpamBot6.on(events.CallbackQuery(data=b'raid'))
@SpamBot7.on(events.CallbackQuery(data=b'raid'))
@SpamBot8.on(events.CallbackQuery(data=b'raid'))
@SpamBot9.on(events.CallbackQuery(data=b'raid'))
@SpamBot10.on(events.CallbackQuery(data=b'raid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK



@SpamBot1.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot2.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot3.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot4.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot5.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot6.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot7.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot8.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot9.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot10.on(events.CallbackQuery(data=b'replyraid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)


@SpamBot1.on(events.CallbackQuery(data=b'spam'))
@SpamBot2.on(events.CallbackQuery(data=b'spam'))
@SpamBot3.on(events.CallbackQuery(data=b'spam'))
@SpamBot4.on(events.CallbackQuery(data=b'spam'))
@SpamBot5.on(events.CallbackQuery(data=b'spam'))
@SpamBot6.on(events.CallbackQuery(data=b'spam'))
@SpamBot7.on(events.CallbackQuery(data=b'spam'))
@SpamBot8.on(events.CallbackQuery(data=b'spam'))
@SpamBot9.on(events.CallbackQuery(data=b'spam'))
@SpamBot10.on(events.CallbackQuery(data=b'spam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)


@SpamBot1.on(events.CallbackQuery(data=b'back'))
@SpamBot2.on(events.CallbackQuery(data=b'back'))
@SpamBot3.on(events.CallbackQuery(data=b'back'))
@SpamBot4.on(events.CallbackQuery(data=b'back'))
@SpamBot5.on(events.CallbackQuery(data=b'back'))
@SpamBot6.on(events.CallbackQuery(data=b'back'))
@SpamBot7.on(events.CallbackQuery(data=b'back'))
@SpamBot8.on(events.CallbackQuery(data=b'back'))
@SpamBot9.on(events.CallbackQuery(data=b'back'))
@SpamBot10.on(events.CallbackQuery(data=b'back'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)

@SpamBot1.on(events.CallbackQuery(data=b'pspam'))
@SpamBot2.on(events.CallbackQuery(data=b'pspam'))
@SpamBot3.on(events.CallbackQuery(data=b'pspam'))
@SpamBot4.on(events.CallbackQuery(data=b'pspam'))
@SpamBot5.on(events.CallbackQuery(data=b'pspam'))
@SpamBot6.on(events.CallbackQuery(data=b'pspam'))
@SpamBot7.on(events.CallbackQuery(data=b'pspam'))
@SpamBot8.on(events.CallbackQuery(data=b'pspam'))
@SpamBot9.on(events.CallbackQuery(data=b'pspam'))
@SpamBot10.on(events.CallbackQuery(data=b'pspam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)


@SpamBot1.on(events.CallbackQuery(data=b'extras'))
@SpamBot2.on(events.CallbackQuery(data=b'extras'))
@SpamBot3.on(events.CallbackQuery(data=b'extras'))
@SpamBot4.on(events.CallbackQuery(data=b'extras'))
@SpamBot5.on(events.CallbackQuery(data=b'extras'))
@SpamBot6.on(events.CallbackQuery(data=b'extras'))
@SpamBot7.on(events.CallbackQuery(data=b'extras'))
@SpamBot8.on(events.CallbackQuery(data=b'extras'))
@SpamBot9.on(events.CallbackQuery(data=b'extras'))
@SpamBot10.on(events.CallbackQuery(data=b'extras'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

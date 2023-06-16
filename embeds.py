from discord import Embed


def quote_embed(quote, author, id):
    embed = Embed()
    embed.type = 'rich'
    embed.title = quote
    embed.description = f'\- {author} ({id})'
    return embed
